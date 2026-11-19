# Part I — Continuous hands-on walkthrough

**Status:** Living document; planning completed in part, hands-on execution not started as of November 18, 2026.

**Documentation decision:** Maintain this walkthrough continuously as work occurs. Organize it in actual execution order, not merely the assignment's order, and cross-reference the assignment sections. Capture routine success concisely; preserve additional sanitized evidence for meaningful findings, failures, policy changes, and integration comparisons. Update proactively rather than reconstructing from memory. **Command capture decision:** Record every meaningful command required to reproduce the workflow, with purpose, execution context, and relevant official reference. Preserve full or extended terminal output only where it demonstrates behavior, failure, enforcement, or an important discrepancy; otherwise summarize outcomes. Redact tokens, secrets, and identifying metadata.

**Assignment source:** *Technical Enablement Lead Peer Interview*, Part I, sections 1–5, pages 3–4.

## Before hands-on work — confirmed context and decisions

- Demo repository exists. Current authorization is **documentation only**; no application or scan implementation has been performed through this document.
- Socket Enterprise organization access: owner confirmed login succeeded; scopes/scan capability not yet tested.
- ActivityPulse plan: initial Node.js CLI + Python reporting engine, anonymized CSV records; later YAML/PyYAML dependency PR. Go validation is optional. [PRD](PRD.md).
- CI scan is optional in the assignment, but selected for the comparison. Controlled GitHub App + GitHub Actions overlap is explicitly approved despite possible duplicate PR comments. [Comparison protocol](integration-comparison.md).
- Policy Block → Warn test: prefer an organic finding from ActivityPulse; use a safe deliberate manifest/test dependency only if necessary.
- Final recommendation for which integration to teach first is **deferred until local CLI, App and Actions have been tested and compared**.
- Relevant conceptual research: [Part I §4 notes](part-i-conceptual-notes.md). Known documentation issues and hands-on friction: [friction log](friction-log.md). AI use: [AI verification log](ai-use-and-verification.md).

## Local repository discovery — firsthand observation

- User located a local `socket-project` directory, but `git remote -v` there reported `fatal: not a git repository (or any of the parent directories): .git`. Do not delete or infer its contents.
- User then entered adjacent `socket-technical-enablement-exercise` directory within their local `github` folder. `git remote -v` confirmed `origin` fetch and push target `https://github.com/mlddragon/socket-technical-enablement-exercise.git`.
- This is the correct existing working clone; skip an additional `git clone`. `git status` verified `main` tracking `origin/main`, up to date, with a clean working tree (user-run check). Next: inspect top-level directory layout before creating application files.

## Walkthrough entries (add in actual execution order)

### Entry 001 — Baseline application and manifests
- **Assignment mapping:** Part I §1.1 prerequisites
- **Status:** Planned; not performed
- **Action / commands:** Pending
- **Expected:** Node.js and Python components run, with analyzable manifests.
- **Actual result / sanitized evidence:** Pending
- **References:** [PRD](PRD.md), [Socket CLI docs](https://docs.socket.dev/docs/socket-cli)
- **Friction / follow-up:** Pending

### Entry 002 — Token and first local CLI scan
- **Assignment mapping:** Part I §§1.1–1.2
- **Status:** Planned; not performed
- **Action / commands:** Pending; do not record token values
- **Expected:** Scoped token permits full scan; results describe analysis state.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket scan documentation](https://docs.socket.dev/docs/socket-scan), [Token docs](https://docs.socket.dev/docs/api-keys)
- **Friction / follow-up:** Pending

### Entry 003 — GitHub Actions scan
- **Assignment mapping:** Part I §1.3 (optional)
- **Status:** Selected for planned comparison; not performed
- **Action / commands:** Pending
- **Expected:** Runner scan and attributable CI logs for comparison with local CLI.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket CI guide](https://docs.socket.dev/docs/sca-ci), [Comparison protocol](integration-comparison.md)
- **Friction / follow-up:** Pending

### Entry 004 — GitHub App and dependency-change PR
- **Assignment mapping:** Part I §§2.1–2.2
- **Status:** Planned; not performed
- **Action / commands:** Pending
- **Expected:** GitHub App evaluates real YAML/PyYAML dependency PR; concurrent Actions scan documents comparative outputs and any duplicate feedback.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket integration guide](https://docs.socket.dev/docs/sca-connect), [Comparison protocol](integration-comparison.md)
- **Friction / follow-up:** Pending

### Entry 005 — Policy Block → Warn
- **Assignment mapping:** Part I §§3.1–3.3
- **Status:** Planned; finding not yet selected
- **Action / commands:** Pending
- **Expected:** Observe actual block behavior, CLI health and exit code; change action to Warn and compare.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket policies](https://docs.socket.dev/docs/policies), [Socket scan documentation](https://docs.socket.dev/docs/socket-scan)
- **Friction / follow-up:** Pending

### Entry 006 — Wrap-up and decisions
- **Assignment mapping:** Part I §§2.2–2.3, 4, 5
- **Status:** Deferred until evidence is collected
- **Topics:** CLI/App/CI suitability and failure modes; first-week teaching path; org-scoped tokens; alert resolutions vs policy rules; friction log and public documentation improvement.
- **Actual evidence and conclusions:** Pending
- **References:** [Conceptual notes](part-i-conceptual-notes.md), [friction log](friction-log.md)

## Record format for additional entries

**Date · Step · Assignment mapping · Product/version/environment · Official reference · Expected · Actual · Sanitized evidence link · Friction/insight · Follow-up**.

If the actual order differs from this suggested sequence, preserve true order and renumber or reorganize entries. Do not convert planned expectations to observed facts without evidence. Never publish tokens or private organizational details.
