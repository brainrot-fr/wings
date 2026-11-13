#!/usr/bin/env python3
"""Read-only verifier for research2/out; writes only verify-report.md."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "out"
REPOS = BASE.parent / "research" / "repos"
REPORT = OUT / "verify-report.md"

CITATION = re.compile(
    r"(?P<path>[A-Za-z0-9_./-]+\.[A-Za-z0-9_-]+):L"
    r"(?P<start>\d+)(?:-L?(?P<end>\d+))?"
)

SKILL_FIELDS = (
    "SOURCE:",
    "FRONTMATTER:",
    "FILES READ:",
    "FILES UNREAD:",
    "JOB:",
    "PROCEDURE:",
    "DECISION RULES:",
    "ARTIFACT SHAPE:",
    "QUESTION PROTOCOL:",
    "VALIDATION:",
    "AGENT FEATURES REQUIRED:",
    "STATE ON DISK:",
    "VOCABULARY:",
    "NON-OBVIOUS TECHNIQUES:",
    "FAILURE MODE FOUGHT:",
    "BAGGAGE:",
    "RISKS:",
    "FIT:",
    "CONFLICTS:",
    "KEY QUOTES:",
    "CONFIDENCE:",
)

PACKAGING_FIELDS = (
    "SOURCE:",
    "SINGLE SOURCE OF TRUTH:",
    "AGENT TARGETS:",
    "GENERATION:",
    "VALIDATION:",
    "VERSIONING AND RELEASE:",
    "INSTALL FOOTPRINT:",
    "PORTABLE ESSENCE:",
    "BAGGAGE:",
    "CONFIDENCE:",
)

failures: list[str] = []
passes: list[str] = []
skips: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    target = passes if ok else failures
    target.append(f"- {'PASS' if ok else 'FAIL'}: {name}" + (f" — {detail}" if detail else ""))


def repo_for_card(card: Path, text: str) -> Path | None:
    match = re.match(r"^#\s+(.+?)/([^/\s]+)", text)
    if not match:
        return None
    owner = re.sub(r"\s+", "", match.group(1))
    expected = f"{owner}__{match.group(2)}".casefold()
    return next((p for p in REPOS.iterdir() if p.is_dir() and p.name.casefold() == expected), None)


def source_lines(path: Path) -> int:
    return path.read_bytes().count(b"\n")


def file_rows(text: str) -> list[list[tuple[str, int]]]:
    read_section = text.split("FILES READ:", 1)
    if len(read_section) != 2:
        return []
    read_text = read_section[1].split("FILES UNREAD:", 1)[0]
    rows: list[list[tuple[str, int]]] = []
    for row in read_text.splitlines():
        if not row.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "path" or set(cells[0]) <= {"-", ":"}:
            continue
        paths = re.findall(r"`([^`]+)`", cells[0])
        counts = [int(value) for value in re.findall(r"\b\d+\b", cells[1])]
        if not paths:
            continue
        if len(paths) != len(counts):
            failures.append(f"{card_label(text)}: FILES READ row has {len(paths)} paths and {len(counts)} counts: {row.strip()}")
            continue
        rows.append(list(zip(paths, counts, strict=True)))
    return rows


def source_candidates(
    repo: Path,
    raw_path: str,
    skill_dir: Path | None,
    last_parent: Path | None = None,
) -> list[Path]:
    candidates = [repo / raw_path]
    if last_parent is not None:
        candidates.append(last_parent / raw_path)
    if skill_dir is not None:
        candidates.append(skill_dir / raw_path)
    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen and resolved.is_relative_to(repo.resolve()):
            seen.add(resolved)
            unique.append(resolved)
    return unique


def resolve_file_table(
    text: str, repo: Path
) -> tuple[list[tuple[str, int, Path | None]], dict[str, Path], set[str], Path | None]:
    rows = file_rows(text)
    skill_dir: Path | None = None
    for row in rows:
        for raw, _ in row:
            if raw.endswith("SKILL.md"):
                found = next((p for p in source_candidates(repo, raw, None) if p.is_file()), None)
                if found is not None:
                    skill_dir = found.parent
                    break
        if skill_dir is not None:
            break

    entries: list[tuple[str, int, Path | None]] = []
    read_map: dict[str, Path] = {}
    listed_paths: set[str] = set()
    for row in rows:
        last_parent: Path | None = None
        for raw, stated_count in row:
            candidates = source_candidates(repo, raw, skill_dir, last_parent)
            matching = next(
                (p for p in candidates if p.is_file() and source_lines(p) == stated_count),
                None,
            )
            chosen = matching or next((p for p in candidates if p.is_file()), None)
            entries.append((raw, stated_count, chosen))
            if chosen is not None:
                relative = chosen.relative_to(repo.resolve()).as_posix()
                read_map[raw] = chosen
                listed_paths.add(relative)
                last_parent = chosen.parent
    unread_text = text.split("FILES UNREAD:", 1)[1].split("JOB:", 1)[0] if "FILES UNREAD:" in text else ""
    unread_paths = re.findall(r"`([^`]+\.[A-Za-z0-9_-]+)`", unread_text)
    for raw in unread_paths:
        found = next((p for p in source_candidates(repo, raw, skill_dir) if p.is_file()), None)
        if found is not None:
            listed_paths.add(found.relative_to(repo.resolve()).as_posix())
    return entries, read_map, listed_paths, skill_dir


def resolve_citation(
    raw_path: str, repo: Path, skill_dir: Path | None, read_map: dict[str, Path]
) -> Path | None:
    if raw_path in read_map:
        return read_map[raw_path]
    candidates = source_candidates(repo, raw_path, skill_dir)
    return next((p for p in candidates if p.is_file()), None)


def card_label(text: str) -> str:
    return text.splitlines()[0].lstrip("# ").strip()


cards = sorted((OUT / "skills").rglob("*.md")) + sorted((OUT / "packaging").rglob("*.md"))
progress_rows = []
for line in (BASE / "progress.md").read_text(encoding="utf-8").splitlines():
    parts = [part.strip() for part in line.split("|")]
    if len(parts) >= 6 and parts[3] in {"TODO", "READ", "CARDED", "SKIPPED", "FAILED"}:
        progress_rows.append(parts)
expected_cards = sum(row[3] == "CARDED" for row in progress_rows)
record(
    "card inventory",
    len(cards) == expected_cards,
    f"{len(cards)} cards found; {expected_cards} CARDED progress rows",
)

for card in cards:
    text = card.read_text(encoding="utf-8")
    repo = repo_for_card(card, text)
    label = card_label(text)
    is_packaging = "(packaging)" in text.splitlines()[0]
    fields = PACKAGING_FIELDS if is_packaging else SKILL_FIELDS
    positions = [text.find(field) for field in fields]
    record(
        f"{label}: required headings and order",
        all(pos >= 0 for pos in positions) and positions == sorted(positions),
        "all required fields present and ordered" if all(pos >= 0 for pos in positions) and positions == sorted(positions) else "missing or out-of-order fields",
    )
    word_count = int(
        subprocess.run(["wc", "-w"], input=text, capture_output=True, text=True, check=True).stdout.split()[0]
    )
    limit = 600 if is_packaging else 450
    record(f"{label}: word limit", word_count <= limit, f"{word_count}/{limit} words")

    for line_number, line in enumerate(text.splitlines(), start=1):
        if "[V]" in line and not CITATION.search(line):
            failures.append(f"{label}: [V] without citation at card line {line_number}")

    if repo is None:
        skips.append(f"{label}: source repository is not in the selected snapshot; source citations and file links were not checked")
        continue

    file_entries, read_map, listed_files, skill_dir = resolve_file_table(text, repo)
    citation_count = 0
    for citation in CITATION.finditer(text):
        citation_count += 1
        source = resolve_citation(citation.group("path"), repo, skill_dir, read_map)
        start = int(citation.group("start"))
        end = int(citation.group("end") or start)
        if source is None:
            failures.append(f"{label}: cited path does not exist: {citation.group('path')}")
            continue
        total = source_lines(source)
        if start < 1 or end < start or end > total:
            failures.append(f"{label}: invalid cited range {citation.group('path')}:L{start}-L{end} (source lines {total})")
    record(f"{label}: citations", citation_count > 0, f"{citation_count} citation(s) checked")

    read_ok = True
    for source_path, stated_count, source in file_entries:
        if source is None:
            read_ok = False
            failures.append(f"{label}: FILES READ path does not exist: {source_path}")
            continue
        actual_count = source_lines(source)
        if actual_count != stated_count:
            read_ok = False
            failures.append(f"{label}: FILES READ count mismatch for {source_path}: stated {stated_count}, actual {actual_count}")
    record(f"{label}: FILES READ line counts", read_ok, f"{len(file_entries)} file entries checked")

    skill_entries = [entry for entry, _, _ in file_entries if entry.endswith("SKILL.md")]
    references_ok = True
    for skill_entry in skill_entries[:1]:
        skill_file = read_map.get(skill_entry)
        if skill_file is None:
            references_ok = False
            continue
        source_text = skill_file.read_text(encoding="utf-8")
        linked: set[str] = set()
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source_text):
            link = link.split("#", 1)[0].split("?", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            candidate = (skill_file.parent / link).resolve()
            if candidate.is_file():
                linked.add(candidate.relative_to(repo.resolve()).as_posix())
        for linked_path in linked:
            if linked_path not in listed_files:
                references_ok = False
                failures.append(f"{label}: linked local file absent from FILES READ/UNREAD: {linked_path}")
    record(f"{label}: local files linked by SKILL.md listed", references_ok)

    quote_section = text.split("KEY QUOTES:", 1)[1].split("CONFIDENCE:", 1)[0] if "KEY QUOTES:" in text else ""
    for quote_line in quote_section.splitlines():
        quote_match = re.search(r"[“\"](.+?)[”\"]", quote_line)
        if not quote_match:
            continue
        quote = quote_match.group(1)
        citations = list(CITATION.finditer(quote_line))
        quote_found = False
        for citation in citations:
            source = resolve_citation(citation.group("path"), repo, skill_dir, read_map)
            if source is None:
                continue
            lines = source.read_text(encoding="utf-8").splitlines()
            start = int(citation.group("start"))
            end = int(citation.group("end") or start)
            if quote in "\n".join(lines[start - 1 : end]):
                quote_found = True
        if not quote_found:
            failures.append(f"{label}: quoted text not found verbatim in cited lines: {quote!r}")

record(
    "quoted strings",
    not any("quoted text not found verbatim" in failure for failure in failures),
    "all quoted strings in KEY QUOTES checked against cited source lines",
)

duplicate_sentences: dict[tuple[str, ...], set[str]] = {}
for card in cards:
    text = card.read_text(encoding="utf-8")
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        words = tuple(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", sentence))
        if len(words) == 10:
            duplicate_sentences.setdefault(tuple(word.casefold() for word in words), set()).add(card.name)
repeated = {sentence: names for sentence, names in duplicate_sentences.items() if len(names) > 1}
record("no repeated 10-word sentence across cards", not repeated, f"{len(repeated)} repeated sentence(s)")
for sentence, names in repeated.items():
    failures.append(f"Repeated 10-word sentence in {', '.join(sorted(names))}: {' '.join(sentence)}")

block_fields = (
    "RANKED CANDIDATES",
    "COMPARISON MATRIX",
    "CONFLICTS",
    "QUESTIONS ANSWERED",
    "GAP EVIDENCE",
    "TECHNIQUES WORTH TAKING",
    "DO NOT TAKE",
    "CATALOG",
)
block_files = sorted((OUT / "blocks").glob("*.md"))
record("block digest inventory", len(block_files) == 6, f"{len(block_files)} digests found")
for digest in block_files:
    text = digest.read_text(encoding="utf-8")
    words = int(
        subprocess.run(["wc", "-w"], input=text, capture_output=True, text=True, check=True).stdout.split()[0]
    )
    record(f"{digest.name}: digest word limit", words <= 2500, f"{words}/2500 words")
    positions = [text.find(field) for field in block_fields]
    record(
        f"{digest.name}: required digest headings",
        all(pos >= 0 for pos in positions) and positions == sorted(positions),
    )

negative_claims_ok = True
for digest in sorted((OUT / "blocks").glob("*.md")):
    text = digest.read_text(encoding="utf-8")
    if re.search(r"\bno (?:reviewed )?skills?\s+(?:does|specifies|provides|includes|requires|defines|gives)\b", text, re.I):
        gap = text.split("## GAP EVIDENCE", 1)
        if len(gap) != 2 or not gap[1].strip():
            negative_claims_ok = False
            failures.append(f"{digest.name}: negative skill claim has no GAP EVIDENCE entry")
record("negative claims have GAP EVIDENCE", negative_claims_ok)

excerpt_results = 0
excerpt_skips = 0
excerpt_files = sorted((OUT / "excerpts").glob("*"))
record("excerpt inventory", 8 <= len(excerpt_files) <= 12, f"{len(excerpt_files)} excerpts found")
for excerpt in excerpt_files:
    content = excerpt.read_bytes()
    header = content.splitlines()[0].decode("utf-8")
    metadata = re.search(
        r"repo: ([^|]+) \| path: ([^|]+) \| lines: (\d+)-(\d+) \| commit: ([^|]+)",
        header,
    )
    marker = b"<!-- SOURCE BODY -->\n"
    if not metadata or marker not in content:
        failures.append(f"{excerpt.name}: missing source metadata or body marker")
        continue
    owner, repository = metadata.group(1).strip().split("/", 1)
    repo_key = f"{owner}__{repository}".casefold()
    source_repo = next((p for p in REPOS.iterdir() if p.is_dir() and p.name.casefold() == repo_key), None)
    if source_repo is None:
        excerpt_skips += 1
        skips.append(f"{excerpt.name}: source repository is not in the selected snapshot; byte comparison skipped")
        continue
    source = source_repo / metadata.group(2).strip()
    start, end = int(metadata.group(3)), int(metadata.group(4))
    excerpt_results += 1
    if not source.is_file():
        failures.append(f"{excerpt.name}: source path does not exist: {metadata.group(2).strip()}")
        continue
    source_bytes = source.read_bytes().splitlines(keepends=True)
    if start < 1 or end < start or end > len(source_bytes) or end - start + 1 > 200:
        failures.append(f"{excerpt.name}: invalid excerpt source range")
        continue
    expected = b"".join(source_bytes[start - 1 : end])
    actual = content.split(marker, 1)[1]
    if actual != expected:
        failures.append(f"{excerpt.name}: body differs from source bytes")
record(
    "verbatim excerpts",
    not any("excerpt" in failure for failure in failures),
    f"{excerpt_results} excerpt(s) checked; {excerpt_skips} skipped (source repository not retained)",
)
cross_files = (
    OUT / "cross" / "license-register.md",
    OUT / "cross" / "risk-register.md",
    OUT / "cross" / "lineage.md",
    OUT / "open-questions.md",
)
record("cross-register and open-question files", all(path.is_file() for path in cross_files))

report = [
    "# Verification report",
    "",
    "Read-only checks over `research2/out`; the verifier writes only this report.",
    "",
    f"**Result:** {'PASS' if not failures else 'FAIL'}",
    f"**Cards:** {len(cards)}",
    f"**Checks passed:** {len(passes)}",
    f"**Checks failed:** {len(failures)}",
    f"**Checks skipped:** {len(skips)}",
    "",
    "## Passed",
    *(passes or ["- None"]),
    "",
    "## Failed",
    *(failures or ["- None"]),
    "",
    "## Skipped",
    *(skips or ["- None"]),
    "",
]
REPORT.write_text("\n".join(report), encoding="utf-8")
print(f"{'PASS' if not failures else 'FAIL'}: {len(passes)} checks passed; {len(failures)} failed; report: {REPORT}")
