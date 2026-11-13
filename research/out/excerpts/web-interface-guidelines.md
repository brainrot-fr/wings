# Repo: vercel-labs__web-interface-guidelines
HEADER: path=/home/syed-jalal/dev/wings/research/repos/vercel-labs__web-interface-guidelines/README.md | commit=434b7f91364665f2f733b310ec54809bf8f37937 | license=LICENSE

## Interactions

- **Keyboard works everywhere.** All flows are keyboard-operable and follow the WAI-ARIA Authoring Patterns.
- **Clear focus.** Every focusable element shows a visible, unobscured focus ring. Prefer `:focus-visible` over `:focus`.
- **Manage focus.** Use focus traps, move & return focus according to the WAI-ARIA Patterns.
- **Match visual & hit targets.** Exception: if the visual target is < 24px, expand its hit target to ≥ 24px.
- **URL as state.** Persist state in the URL so share, refresh, Back/Forward navigation work.
- **No dead zones.** If part of a control looks interactive, it should be interactive.

