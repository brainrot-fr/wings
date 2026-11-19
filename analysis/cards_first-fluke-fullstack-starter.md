### new candidates/first-fluke-fullstack-starter/.agents/skills/_shared/core (18-file group)
- Purpose: Shared agent contracts for review, clarification, verification, routing, and task handoffs.
- Wings block fit: requirements | frontend | sdlc | backend | database | security
- Maturity: rule catalogue
- Core mechanism worth taking:
  - `core/execution-policy.md:5-18` — scope authorization, material-question pauses, and behavior-based verification.
  - `core/common-checklist.md:7-29` — compact correctness, error, security, verification, and change-hygiene checks.
  - `core/clarification-protocol.md:5-21` — ask only when missing information materially changes outcome or authorization.
- Gotchas/defects found: `core/execution-policy.md:18` links to `../runtime/result-contract.md`, which does not resolve in the scoped tree.
- Hard dependencies: Many files assume OMA CLI, `.agents/` configuration/state, skill routing, injected runtime contracts, or MCP capabilities; no explicit Serena reference found.
- Portability: partial — several principles are generic, but dispatch, code intelligence, and evidence storage are OMA-runtime-bound.
- Overlap: all wings blocks; OMA routing overlaps the whole suite.
- Verdict: TAKE-IDEAS — retain portable policy/checklist concepts and rewrite the runtime-specific contracts.
- Confidence in this card: medium

### new candidates/first-fluke-fullstack-starter/.agents/skills/oma-mobile/variants/flutter
- Purpose: Declare a Flutter starter stack and verification commands.
- Wings block fit: frontend | backend | database
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `variants/flutter/stack.yaml:1-18` — records stack choices and syntax/test checks in a shared structured manifest.
  - `variants/flutter/tech-stack.md:36-62` — separates transport from repository-level decoded-data caching.
- Gotchas/defects found: The stack invokes `dart analyze` and `flutter test`; no generic runner is specified (`stack.yaml:14-18`).
- Hard dependencies: Flutter/Dart, their CLIs, and selected packages; versioned choices appear in tech-stack prose.
- Portability: partial — manifest shape transfers; Flutter implementation does not.
- Overlap: Swift iOS and React Native variants; wings frontend/backend/database.
- Verdict: TAKE-IDEAS — reuse stack-decision fields, not platform defaults.
- Confidence in this card: medium

### new candidates/first-fluke-fullstack-starter/.agents/skills/oma-mobile/variants/react-native
- Purpose: Declare a React Native stack and TypeScript/Jest verification.
- Wings block fit: frontend | backend | database
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `variants/react-native/stack.yaml:1-20` — keeps framework, state, navigation, transport, cache, layout, and checks together.
  - `variants/react-native/tech-stack.md:58-72` — separates server state, transport, and persistent cache responsibilities.
- Gotchas/defects found: Verification commands use `npx` and skip when that binary is absent (`stack.yaml:15-20`); the stack is not CLI-free.
- Hard dependencies: React Native ecosystem, Node/npm/npx, TypeScript, Jest; optional Expo/native toolchains.
- Portability: partial — decision-record pattern transfers; ecosystem commands and libraries do not.
- Overlap: Flutter and Swift iOS variants; wings frontend/backend/database.
- Verdict: TAKE-IDEAS — reuse the record shape and layer boundaries, not the fixed stack.
- Confidence in this card: medium

### new candidates/first-fluke-fullstack-starter/.agents/skills/oma-mobile/variants/swift-ios
- Purpose: Declare a SwiftUI stack with OpenAPI generation and SwiftPM verification.
- Wings block fit: frontend | backend | database
- Maturity: vendor-specific
- Core mechanism worth taking:
  - `variants/swift-ios/stack.yaml:1-19` — records API generator/spec alongside storage, cache, structure, and checks.
  - `variants/swift-ios/tech-stack.md:57-78` — separates generated API transport from repository-owned decoded-model caching.
- Gotchas/defects found: The schema allows additional properties (`variants/stack.schema.json:49`), so typos in optional fields are not rejected.
- Hard dependencies: Swift/Xcode/SwiftPM, `swift build`/`swift test`, OpenAPI generator and Cache libraries.
- Portability: partial — manifest fields transfer; Swift tools and code-generation workflow do not.
- Overlap: Flutter and React Native variants; wings frontend/backend/database.
- Verdict: TAKE-IDEAS — use the manifest as a generic stack decision record.
- Confidence in this card: medium
