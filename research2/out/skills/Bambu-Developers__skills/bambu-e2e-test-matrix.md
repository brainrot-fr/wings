# Bambu-Developers/skills / bambu-e2e-test-matrix
SOURCE: commit `b91cd017d9304968f8642866685be62ef666738d` | MIT, root `LICENSE` | 1,073 skill-folder lines; `find ... -type f -print0 | xargs -0 wc -l`
FRONTMATTER: `name: bambu-e2e-test-matrix`; `description: Genera y ejecuta matrices de pruebas funcionales E2E manuales (flujo, usabilidad, vista/visual y casos borde) para cualquier aplicación web usando Playwright MCP, y opcionalmente compara contra Figma y/o corre análisis de seguridad SAST (OWASP Top 10, CWE Top 25, secretos, CVEs de dependencias). Ejecuta por lotes (un módulo por sub-agente; el orquestador solo coordina, nunca navega), graba video continuo por módulo, corre hasta completar todos los casos aprobados con gate de completitud (checkpoint/retomado si se corta) y cierra con una calificación/ranking final. Úsala cuando el usuario pida una "matriz de pruebas E2E", "pruebas de flujo/usabilidad", "probar un sitio", "evidencias de pruebas (video)", "comparar la UI contra Figma" o "análisis de seguridad/SAST del código". Es genérica: pregunta primero la URL del sistema, el repositorio y si hay diseño en Figma antes de empezar. NO modifica el código del proyecto.`
FILES READ:
| Path | Lines | Role |
|---|---:|---|
| `bambu-e2e-test-matrix/SKILL.md`; `README.md` | 336; 123 | Workflow; install |
| `bambu-e2e-test-matrix/references/accessibility-testing.md`; `agentic-browser-testing.md`; `playwright-automation.md`; `seguridad-sast.md`; `visual-testing.md` | 44; 43; 58; 57; 42 | Guides |
| `bambu-e2e-test-matrix/references/agents/e2e-explorer.md`; `e2e-runner.md`; `e2e-security-sast.md`; `e2e-visual-figma.md` | 47; 70; 79; 28 | Four agents |
| `bambu-e2e-test-matrix/assets/templates/ESTADO-CORRIDA.md`; `matriz-pruebas.csv`; `reporte.md`; `scripts/setup.sh` | 18; 6; 36; 86 | State; matrix; report; setup |
FILES UNREAD: None.
JOB: Web E2E matrix, optional Figma/SAST; no app-code edits. [V] (`bambu-e2e-test-matrix/SKILL.md:L17-L27`, `L254-L264`)
PROCEDURE:
1. Intake; matrix in `Fase 1`; explicit approval gates `Fase 2`. [V] (`bambu-e2e-test-matrix/SKILL.md:L99-L157`)
2. `Fase 2` runs batches, videos, timecodes and checkpoints; requires zero pending. [V] (`bambu-e2e-test-matrix/SKILL.md:L159-L251`)
3. Optional `Fase 3` appends SAST findings. [V] (`bambu-e2e-test-matrix/SKILL.md:L254-L264`)
DECISION RULES: Batch 12 default, 20–25 ceiling; two concurrent; `interactive`/`corrido`; scores Passed/Blocked/Failed = 100/50/0, priority 3/2/1. [V] (`bambu-e2e-test-matrix/SKILL.md:L114-L123`, `L174-L184`, `L311-L330`)
ARTIFACT SHAPE: CSV fields `ID,Modulo,Titulo,Tipo,Prioridad,Precondiciones,Pasos,Datos,Resultado_esperado,Estado,Video,Marca_Tiempo,Evidencia,Notas`; checkpoint/auth/evidence/report. [V] (`bambu-e2e-test-matrix/SKILL.md:L130-L157`, `L204-L214`)
QUESTION PROTOCOL: Intake, OTP, approval, module confirmation. [V] (`bambu-e2e-test-matrix/SKILL.md:L99-L123`, `L159-L160`, `L235-L247`)
VALIDATION: Human-judged; pending count. Setup checks deps/registers MCP. [V] (`bambu-e2e-test-matrix/SKILL.md:L249-L251`, `bambu-e2e-test-matrix/scripts/setup.sh:L31-L85`)
AGENT FEATURES REQUIRED: MCP, agents; optional tools.
STATE ON DISK: CSV/checkpoint, auth state, evidence. [V] (`bambu-e2e-test-matrix/SKILL.md:L204-L214`, `L285-L305`)
VOCABULARY: `E2E-<MODULO>-###`; Alta/Media/Baja; four statuses. [V] (`bambu-e2e-test-matrix/SKILL.md:L135-L157`)
NON-OBVIOUS TECHNIQUES:
 - Per-case video start/failure timecodes. [V] (`bambu-e2e-test-matrix/SKILL.md:L143-L151`)
 - Reuse `.auth/session.json` across batches; resume via checkpoint. [V] (`bambu-e2e-test-matrix/SKILL.md:L186-L198`, `L285-L305`)
 - Close only when pending count is zero. [V] (`bambu-e2e-test-matrix/SKILL.md:L249-L251`)
FAILURE MODE FOUGHT: Lost progress, repeated OTP, unfinished runs. [I] (`bambu-e2e-test-matrix/SKILL.md:L159-L198`, `L238-L251`)
BAGGAGE: Setup/tool dependency. [V] (`bambu-e2e-test-matrix/SKILL.md:L28-L66`)
RISKS: Setup replaces existing Playwright MCP, invokes `npx`, and may copy agents globally. [V] (`bambu-e2e-test-matrix/scripts/setup.sh:L40-L68`). Auth state persists locally. [V] (`bambu-e2e-test-matrix/SKILL.md:L186-L207`)
FIT: testing: **ADAPT** approval/matrix/checkpoint/evidence; no req IDs. [I] (`bambu-e2e-test-matrix/SKILL.md:L130-L157`)
CONFLICTS: MCP/subagents/downloads conflict with universal/no-binary rules. [V] (`bambu-e2e-test-matrix/scripts/setup.sh:L43-L44`)
KEY QUOTES: None.
CONFIDENCE: High.
