# Socket Technical Enablement Exercise — Current Project Status

**Reviewed:** November 23, 2026. Part III updated for the Widgets Mfg demo lab. Part II evidence was recorded November 22.

**Panel:** **Tuesday, November 24, 2026 at 1:00 PM Eastern** (confirmed by recruiting).

**Submission target:** **Monday, November 23 by 1:00 PM Eastern** as the working target based on the original 24-hour instruction. Recruiting has not separately confirmed the revised submission time.

## Executive status

| Assignment area | Status | Evidence and remaining work |
|---|---|---|
| **Part I: Scan and interpret** | **Complete / verified** | Functioning two-runtime ActivityPulse app; full baseline and PyYAML scans; nuanced finding interpretation. [Part I briefing](part-i-briefing.md), [walkthrough](part-i-walkthrough.md). |
| **Part I: GitHub integration paths** | **Complete / verified** | GitHub App detects `picocolors` change on [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1); Actions Python CLI run passed after correcting token. Duplicate bot comments verified; automated CI PR trigger intentionally disabled on feature branch, App retained. |
| **Part I: Block vs Warn enforcement** | **Complete / verified** | PyYAML potentialVulnerability Block scan unhealthy / combined command exit 1; Warn healthy / exit 0. Policy returned to Inherit per user confirmation. |
| **Part I: Explain decisions, friction and evidence** | **Complete / documented** | [Briefing](part-i-briefing.md), [friction log](friction-log.md), [AI-use log](ai-use-and-verification.md). Interview rehearsal remains. In Attempt 4, the preferred diff scan fell back to streaming after a permission denial. The job succeeded. |
| **Part II: Socket Firewall registry mode** | **Enforcement verified** | Firewall served isolated npm clients. An allowed install and policy-driven tarball 403 were recorded. [Results and live-demo checklist](part-ii-firewall-results.md). |
| **Part III: Hands-on lab ≤30 min** | **Packaged** | [Widgets Mfg demo lab](part-iii-lab.md), GitHub template, shared dependency patch, CI workflow starter, and saved comparison results. |
| **Part III: One-page customer talk track** | **One-page layout verified** | [PDF](part-iii-talk-track.pdf) · [Text version](part-iii-talk-track.md). Covers both engineer workflows and customer objections. |
| **Part III: Practical readiness assessment** | **Five-minute demo gate ready to run; extended field assessment proposed** | [Assessment](part-iii-readiness-check.md) preserves the in-lab demo check and adds a separate 50–60-minute field assessment design. Timed learner trials, evaluator calibration, and field validation remain pending. |
| **Extra: Socket CLI Permissions Explorer** | **Working reference** | [Socket CLI Permissions Explorer](https://docs.google.com/spreadsheets/d/1iQLzZkCqyz8XxqFjk2UQPY5TDkvVa1a49uHQ3eLOBPY/edit?usp=sharing) covers documented CLI scopes and suggests mappings by role, persona, and use case. Untested API paths still require validation. |
| **Extra: Package Scores documentation rewrite** | **Draft / pending human review** | [Repository draft](package-scores-rewrite.md). Additional enablement work outside the required Part III package. |

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
- [x] PR #1 left open for interview. **Important:** current `main` does not include `picocolors` or the Actions workflow; they remain on the open feature branch. GitHub requires the workflow file on the default branch for manual dispatch.

### 3. Policy demonstration and teaching
- [x] Temporarily set Potential vulnerability rule to Block; fresh scan `1a1190d3-8b85-4692-9f01-310c3cc406bf` unhealthy, error action, original command exit 1.
- [x] Switched to Warn; fresh scan `46093b05-bcd0-438a-9592-4e2a8f045ef3` healthy, exit 0; warning visible using `--report-level=warn`.
- [x] Reverted override to **Inherit** per user confirmation.
- [x] Explanation of org/capability scopes, narrow alert resolution versus broader policy rule and potential consequences.
- [x] Firsthand friction log with docs recommendations and separate AI verification notes.
- [ ] Quick 5–8-minute Part I demo rehearsal; no need to change live policy again.

## Part II — if time permits

Mason ran the registry-mode demo November 22. Firewall responded over TLS, resolved the interview organization, allowed a monitored npm install, and blocked the test fixture’s artifact with HTTP 403 under the existing policy. The original npm error matched the Firewall event by request ID. The service was up at the last check.

The [Part II results](part-ii-firewall-results.md) preserve the sanitized observations, local evidence inventory and panel readiness checklist. The evidence includes verified screenshots and masked terminal excerpts. Two original local clips are available for the panel.

## Part III artifact inventory and content assessment

### Widgets Mfg demo lab

- The [30-minute lab](part-iii-lab.md) starts with a buyer’s workflow question and ends with a two-view demo and recommendation.
- The [public template](https://github.com/mlddragon/activitypulse-demo-template) generated two private training repos. The shared patch applied cleanly and the patched app ran locally. A fresh [verification PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) produced successful CI and App results on the pre-authorized exercise repo. The shared starter is verified there. A live run with two isolated integrations depends on access for those training repos.
- The [one-page talk track](part-iii-talk-track.pdf) and [five-minute in-lab readiness check](part-iii-readiness-check.md) use the same buyer scenario. The same assessment file proposes a separate field-performance check and a five-minute panel explanation; that extended check has not been run with learners. Timing with a new learner remains to be measured.

### Extra documentation improvement
- [x] [Package Scores rewrite draft](package-scores-rewrite.md) added, linked to Google Doc. Provenance clearly marks it AI-assisted and awaiting editorial review.
- [ ] Review, correct any claims not fully validated, decide whether to use as a friction-log discussion sample or share separately. Not part of mandatory three-deliverable package.

## Prioritized next actions

1. Review the three [Part III teaching materials](teaching-package.md) and rehearse the five-minute assessment.
2. Prepare the formal Part III submission separately. Use **Monday, November 23 at 1:00 PM Eastern** as the working target unless recruiting confirms a different deadline.
3. Rehearse the Part I walkthrough using saved reports and PR #1.
4. Recheck Firewall health before the panel and open the local Part II evidence as a fallback.

The [root README](../README.md) is the reviewer entry point. The [project index](README.md) separates current deliverables from historical planning. This repository is available for progress review. The formal submission is still pending.
