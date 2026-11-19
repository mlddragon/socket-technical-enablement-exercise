# Socket Technical Enablement Exercise — Current Project Status

**Reviewed:** November 19, 2026, from GitHub `main` tree/commits, open PR #1, the Part I evidence brief, and Part III deliverables.  
**Current main commit:** `a373d71c65c20e4f1a1192db7a1dc46e61daa795`  
**Panel:** **Tuesday, November 24, 2026 at 1:00 PM Eastern** — recruiting coordinator proposed time, candidate accepted, and coordinator confirmed sending invite November 19.  
**Submission target:** **Monday, November 23 by 1:00 PM Eastern** as a conservative working target based on the original 24-hour-before-panel instruction. This is **inferred, not separately confirmed as an explicit revised deadline**.

## Executive status

| Assignment area | Status | Evidence and remaining work |
|---|---|---|
| **Part I: Scan and interpret** | **Complete / verified** | Functioning two-runtime ActivityPulse app; full baseline and PyYAML scans; nuanced finding interpretation. [Part I briefing](part-i-briefing.md), [walkthrough](part-i-walkthrough.md). |
| **Part I: GitHub integration paths** | **Complete / verified** | GitHub App detects `picocolors` change on [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1); Actions Python CLI run passed after correcting token. Duplicate bot comments verified; automated CI PR trigger intentionally disabled on feature branch, App retained. |
| **Part I: Block vs Warn enforcement** | **Complete / verified** | PyYAML potentialVulnerability Block scan unhealthy / combined command exit 1; Warn healthy / exit 0. Policy returned to Inherit per user confirmation. |
| **Part I: Explain decisions, friction and evidence** | **Mostly complete** | [Briefing](part-i-briefing.md), [friction log](friction-log.md), [AI-use log](ai-use-and-verification.md). Rehearsal and final presentation selection outstanding. Native diff-scan preferred mode still falls back to streaming for permission denial despite `diff-scans:create` and `diff-scans:list`; baseline CI scan succeeded. |
| **Part II: Socket Firewall registry mode** | **Not attempted** | Need registry-mode container setup, package-manager proxy configuration, safe policy-block demonstration, actual logs and wrap-up if chosen. No Part II implementation or evidence present on `main`. Optional prioritization: currently behind Part III submission; not completed, not to be represented as such. |
| **Part III: Hands-on lab ≤30 min** | **Substantially drafted / illustrated; not yet dry-run or submitted** | [25-minute Courtney-led lab](part-iii-lab.md), original Block/Warn terminal PNGs, four GitHub Actions PNGs, original side-by-side comparison, self-check and collapsible answer key. Needs learner/usability review, measured timing and screenshot/render checks. |
| **Part III: One-page customer talk track** | **Draft exists; format not validated** | [Talk track](part-iii-talk-track.md) covers three failure modes and customer objections. Confirm it actually fits one page in final submission format and matches final lab narrative. |
| **Part III: Practical readiness check** | **Draft exists; performance test not validated** | [Readiness rubric](part-iii-readiness-check.md) has two scenarios, Warn follow-up, observable readiness/not-ready criteria, safety gates and remediation. Need consistency review and short trial. |
| **Extra: Package Scores documentation rewrite** | **Draft / pending human review** | [Rewrite](package-scores-rewrite.md) and [Google Doc review copy](https://docs.google.com/document/d/1bm8TfSpiRpJJDsCublt_rcPcJtmmN5wza23yOrIHb8Q/edit). Separately useful evidence of documentation/enablement judgment; not an assigned Part III deliverable and not confirmed to have been submitted to Socket. |

## Part I detailed accounting

### 1. Set up and scan
- [x] Functional `prod/cli.js` Node.js → `prod/report.py` Python, 117 sample activity records, YAML import with PyYAML 6.0.2.
- [x] Org-scoped Socket API token with minimum three local scan scopes; Socket CLI v1.15.0 authenticated.
- [x] Baseline no-external-dependency full scan healthy, no alert records.
- [x] PyYAML scan with one package represented by 53 release-artifact records; distinguish findings from policy and actual relevance.
- [x] Reports captured in walkthrough with scan IDs; `--no-banner` in CLI commands.

### 2. Compare integrations
- [x] GitHub App installed for **selected repository** only.
- [x] PR #1 introduced `picocolors@1.1.1` and its real use in the CLI; App posted dependency review and successful checks.
- [x] GitHub Actions CI used `socketsecurity` Python CLI 2.12.2; initial HTTP 401 traced to incorrect secret value; valid `sktsec_` token resolved authentication.
- [x] Full CI run [#44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628), attempt 4 passed; preferred diff-scan had insufficient-permission fallback but streaming scan succeeded.
- [x] Two bot PR comments observed, one App and one Actions.
- [x] User selected GitHub App as routine PR path, disabled automatic Actions triggers on feature branch in commit `293b739`; retained manual workflow and expanded-scope CI token.
- [x] PR #1 left open for interview. **Important:** current `main` does not include `picocolors` or the Actions workflow; they remain on the open feature branch. Manual workflow dispatch is generally only available after the workflow exists on the default branch.

### 3. Policy demonstration and teaching
- [x] Temporarily set Potential vulnerability rule to Block; fresh scan `1a1190d3-8b85-4692-9f01-310c3cc406bf` unhealthy, error action, original command exit 1.
- [x] Switched to Warn; fresh scan `46093b05-bcd0-438a-9592-4e2a8f045ef3` healthy, exit 0; warning visible using `--report-level=warn`.
- [x] Reverted override to **Inherit** per user confirmation.
- [x] Explanation of org/capability scopes, narrow alert resolution versus broader policy rule and potential consequences.
- [x] Firsthand friction log with docs recommendations and separate AI verification notes.
- [ ] Quick 5–8-minute Part I demo rehearsal; no need to change live policy again.

## Part II — if time permits

The assignment's referenced Firewall exercise requests **registry mode in a container**, configuring a package manager to use the proxy, demonstrating an organization-policy block, and capturing terminal evidence. No implementation or recorded proof has been completed. Before claiming Part II ready, require actual: container startup/health, proxy package-manager configuration, a safe blocked request and policy evidence, and short explanation of what was enforced. Docker/Colima readiness from earlier discussion is not the same as a working Firewall.

**Priority decision:** Part III materials first. Then decide whether Part II can be safely completed before the new panel without harming submission quality; otherwise bring honest notes on incomplete Part II.

## Part III artifact inventory and content assessment

### Lab: [part-iii-lab.md](part-iii-lab.md)
- [x] Courtney is ActivityPulse's lead engineer/player-coach; third-person intro/outro and learner second-person instructional sections.
- [x] Four learner activities, each using **what / why / steps / expected result** format.
- [x] Actual saved scans and commands for Block vs Warn; screenshots uploaded to `project/images/part-iii/cli-policy-block.png` and `cli-policy-warn.png`.
- [x] Side-by-side original screenshot comparison embedded in Activity 2; table explicitly compares `healthy:false` / `policy:error` with `healthy:true` / `policy:warn`.
- [x] Activity 3 uses original GitHub Actions screenshots (attempt 1, 401 search, failed-vs-success comparisons) and accessible historical logs plus sanitized excerpts.
- [x] Activity 4 includes worksheet, self-check and expandable answer key.
- [x] Self-contained learner materials; no requirement to consult Part I planning records.
- [ ] **Human verification:** check GitHub rendered layout at desktop and narrow widths, screenshot legibility, image alt text, links to exact Actions attempts, and whether expandable answer key hides correctly; file presence and Markdown references were confirmed from repo, **not pixel-by-pixel rendered inspection**.
- [ ] **Run timed learner walkthrough:** confirm a new engineer can finish in 25 minutes without being given interviewer-only access or the answer key too early. Confirm whether practical readiness assessment is included in 25 min or immediately after (the separate check is 5–7 min, making combined total potentially above 30 min).
- [ ] Optional editorial alignment: the story currently says `Courtney asks a new team member`; previously requested wording was `Courtney has asked you to investigate this.` Ensure learner-facing narrative consistently meets intended voice before finalizing.

### One-page talk track: [part-iii-talk-track.md](part-iii-talk-track.md)
- [x] Draft customer explanation of Block vs Warn vs 401, plus objections and response guidance.
- [ ] Rehearse spoken use, align terminology with lab, then lay out as **one actual page**; raw Markdown title does not prove single-page final format.

### Readiness check: [part-iii-readiness-check.md](part-iii-readiness-check.md)
- [x] Evidence-based classification, safety critical errors, specific ready/not-ready criteria, remediation.
- [ ] Check its standalone instructions, align with lab's Courtney narrative, and perform 5-minute sample assessment. Consider how to include it within the lab's **≤30-minute** envelope if the assignment measures the entire teaching package.

### Extra documentation improvement
- [x] [Package Scores rewrite draft](package-scores-rewrite.md) added, linked to Google Doc. Provenance clearly marks it AI-assisted and awaiting editorial review.
- [ ] Review, correct any claims not fully validated, decide whether to use as a friction-log discussion sample or share separately. Not part of mandatory three-deliverable package.

## Prioritized next actions

1. **Confirm final submission timing** relative to the November 24 1:00 PM ET panel. The candidate accepted this rescheduling and the coordinator said they sent the invite. Use **November 23 1:00 PM ET** as a conservative submission target based on the originally stated 24-hour review rule unless explicitly revised.
2. **Finish a timed review of Part III lab**, with actual screenshot/render checks and minor story/copy fixes. No need for comprehensive historical documentation cleanup.
3. **Ensure talk track really fits one page** and readiness check can be assessed within assigned time. Choose export format (Markdown links, PDF or other explicit requested format) and build a concise shareable package.
4. **Submit Part III package** through the requested channel; verify delivery/receipt. No repository file alone constitutes submission.
5. **Rehearse Part I demonstration** using saved reports and PR #1. Keep policy Inherit; do not expose tokens.
6. **Consider Part II Firewall only after Part III is submission-ready.** Explicitly label any partial attempt.
7. **Post-interview housekeeping:** decide when to merge or close PR #1, whether to move manual workflow to main, and whether to keep connected App/token as already requested. No automatic changes.

## Repository hygiene observations

Several historical planning documents (`README.md`, `project/README.md`, `project/PRD.md`, `project/artifact-inventory.md` and sections of `project/friction-log.md`) still contain dated “planning only,” “no app/scan,” or “experiment not started” language. **They are stale compared with actual commits**, but need not be wholesale rewritten before the interview. Treat this status record and the verified Part I brief as current, while retaining dated planning history.

**Sources reviewed:** GitHub `main` tree/commits through `a373d71c6`; `project/part-iii-lab.md`, talk track, readiness check, teaching package index, Package Scores rewrite, Part I briefing, execution plan, PRD and repository READMEs; GitHub PR #1. Recruiting schedule was verified against the November 19 Socket email thread, not inferred from obsolete planning files.
