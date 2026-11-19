# Socket CLI permissions worksheet — Work-thread handoff

**Status:** Requirements/discussion persisted; spreadsheet NOT built. **Date:** 2026-11-18 (America/Detroit).  
**Purpose:** Allow a separate ChatGPT Work thread to retrieve precise background, then follow the user's **additional, specific spreadsheet-building instructions**. **Do not interpret this document as authorization to build or choose the final platform/layout.**

## User's objective and observed pain point

During Socket Technical Enablement Lead interview exercise Part I §1.1 ("Create your first scan"), user struggled to find the **combined minimum token scopes** needed to complete the whole CLI scan workflow. The Socket CLI reference provides requirements command-by-command and in sub-sections, but there is no clearly surfaced task-oriented "customer wants to do X; which permissions are needed?" guide in the user's experience. User explicitly said **the information is present**, not absent; the deficiency is discoverability, workflow grouping and time-to-answer. The user observed that much of the scan docs appears CLI-help-like without enough practical guidance around end-to-end customer tasks. This is firsthand **documentation friction**, not a demonstrated CLI defect.

User proposed a spreadsheet/worksheet organizing **CLI command + customer use case + permission(s)**. They want to tell the Work thread additional **specific instructions** before any spreadsheet is built. Their aim is a practical enablement/customer-administration aid that helps new SEs, TAMs, Support Engineers and customers provision **least-privileged organization API tokens** without granting broad scopes or hunting through help pages.

Relevant framing: An alphabetically sorted command reference alone is less useful than grouping by *customer outcome/workflow*. A cross-reference can still support command lookup. Ideally a customer can choose a set of tasks and receive a **deduplicated union of necessary scopes**, with each scope attributable to its underlying command. The current chat displayed an illustrative, interactive checklist with three tasks (create full scans; list/inspect/compare scans; evaluate security policy) and computed union; this was a **concept**, not an implemented spreadsheet or a final design selection.

## Seed command / use-case / required-permission matrix

These rows are the initial **scan-command subset**, grounded in the [Socket scan reference](https://docs.socket.dev/docs/socket-scan) and local Socket CLI v1.15.0 help that user inspected. Do **not** present them as an exhaustive CLI-wide permissions inventory.

| Customer use case | CLI command | Minimum documented scope(s) | Notes |
|---|---|---|---|
| Create first/full dependency scan | `socket scan create` | `full-scans:create` | CLI help explicitly reports this permission; may consume scan quota. |
| Review/list existing scans | `socket scan list` | `full-scans:list` | Read-only inventory. |
| Inspect raw scan findings | `socket scan view` | `full-scans:list` | Existing scan. |
| Read scan metadata | `socket scan metadata` | `full-scans:list` | Existing scan. |
| Compare two scans | `socket scan diff` | `full-scans:list` | Existing scans. |
| Evaluate findings against organizational policy | `socket scan report` | `full-scans:list`, `security-policy:read` | The `Report` subsection lists extra permission requirements. |
| Create AND evaluate policy in a single command | `socket scan create --report` | `full-scans:create`, `full-scans:list`, `security-policy:read` | Union of create + report, subject to current documentation/version verification. |

**Workflow union:** For a CLI operator who must create, inspect and policy-evaluate scans, the **three distinct scopes** are `full-scans:create`, `full-scans:list`, `security-policy:read`. Do not add delete, token-administration, or policy-write scopes without an actual workflow need. The user independently located these permission families and identified the task-fragmentation problem.

**Proposed future coverage, NOT YET RESEARCHED/VERIFIED:** common workflows for CI automation, read-only troubleshooting, first-time onboarding, admin/delete operations, GitHub App and other integration contexts, error diagnosis and permission verification. Any expanded row must be traced to official documentation; mark unknowns, conditional scopes and version-specific variations rather than guessing.

**Potential worksheet information architecture (suggestions only; user controls final design):**
- Workflow/use-case view: goal, commands included, combined minimal scope set, optional scopes, expected result, test/verification, common permission failure, official reference.
- Command reference view: CLI command and options, use case, required scopes, conditional scopes, docs URL, verified CLI version/date.
- Token planning selection: select workflows and see deduplicated required scopes; no authorization to build interactive components until user specifies.
- A permission-to-command reverse lookup, if the user's design calls for it.
- Keep distinct concepts separate: `create` vs `report`, CLI tool vs organization token, read vs write operations, GitHub App permissions vs API-token scopes, and an **actual** authorization error vs a hypothesized troubleshooting scenario.

## Known exercise state / constraints

- Public repository: https://github.com/mlddragon/socket-technical-enablement-exercise
- Assignment: Part I §1.1 scoped API token + full scan, §§1.2–1.3 analyze results/optional CI, §2 GitHub App PR and compare, §3 Block→Warn policy.
- [Part I walkthrough](part-i-walkthrough.md), [friction log Entry 004](friction-log.md), [Part I execution plan](part-i-execution-plan.md), [PRD](PRD.md).
- ActivityPulse Node.js/Python five-file functional baseline published on `main` as commit `e078a11` (later documentation commits are expected). It processes 117 anonymized activity records. No external npm/Python dependencies yet; `prod/requirements.txt` is empty.
- Socket CLI installed and verified **v1.15.0**. `socket scan --help` banner: `token: (not set), org: (not set)`; `socket scan create --help` reviewed. **No organization API token has been created and no Socket scan has run**, at the last observed point.
- Current manual next step: go to organization API-token creation page, inspect permissions, select least-privilege required scopes, avoid exposing secret token values.
- The interview assignment's Part III materials are due 24 hours before Friday Nov 20 1:30 PM Eastern panel, i.e. **Thursday Nov 19, 1:30 PM Eastern**. Time is constrained; keep spreadsheet work scoped by user's coming instruction.
- User prefers **one command/action at a time** in hands-on Chat thread, detailed explanation/verification, and **proactive** activity/friction documentation. Do not log unobserved outcomes as completed.
- Previously offered platform choice Google Sheets vs Excel. User asked whether Socket is a Microsoft or Google shop. **Not established**: public references to Google Cloud Platform do *not* prove Google Workspace; public references to Notion/Slack also do not prove office suite. Prior answer suggested Google Sheets *provisionally*, not as a Socket-standard fact. Let user choose final spreadsheet platform.

## Source links

- [Socket scan CLI commands and API-token requirements](https://docs.socket.dev/docs/socket-scan)
- [Socket API keys, organization and capabilities](https://docs.socket.dev/docs/api-keys)
- [Socket CLI](https://docs.socket.dev/docs/socket-cli)
- [Friction log](friction-log.md)
- [Part I walkthrough](part-i-walkthrough.md)

## Handoff rule

**Next Work thread should first read this brief and the user's new instructions; it should not assume the matrix above is the final layout or start constructing a spreadsheet solely from this document.** Confirm official permission applicability for any additional command families and preserve source attribution/unknowns. The handoff must not interrupt or alter the ongoing Socket API-token setup in the Chat thread.
