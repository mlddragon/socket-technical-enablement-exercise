# Socket Technical Enablement Exercise — Part I Briefing

**Prepared:** November 19, 2026  
**Candidate:** Mason Dillon  
**Exercise repository:** [mlddragon/socket-technical-enablement-exercise](https://github.com/mlddragon/socket-technical-enablement-exercise)  
**Status:** Part I demonstrations complete. Panel rehearsal remains.

**Purpose:** Interview-ready narrative and evidence index. This is **not** a claim that every optional investigation or documentation improvement has been implemented.

## 1. Approach and environment

I built **ActivityPulse**, a small, functioning two-runtime CLI instead of a synthetic manifest-only project. Node.js handles terminal output and invokes a Python reporting script; Python loads anonymized activity records from CSV or YAML and aggregates counts. The working demo processes **117 CSV records** (27 applications, 16 follow-ups, 4 interviews, 4 job-readiness activities and 66 other activities). YAML support uses **PyYAML 6.0.2** and `yaml.safe_load`; the later PR adds **picocolors 1.1.1** for a small improvement to terminal output. Tests confirmed the CSV summary and a three-entry YAML fixture.

**Environment:** Local macOS ARM64; Node.js 24.21.0, Python 3.12.16, Socket npm CLI **1.15.0** (`socket`). GitHub Actions used Ubuntu, Python 3.12 and Python `socketsecurity` CLI **2.12.2** (`socketcli`). The two Socket executables are different products/interfaces and should not be represented as having identical flags or permission requirements.

**Authentication:** A local organization token with `full-scans:create`, `full-scans:list` and `security-policy:read` was sufficient for the demonstrated manual scans. The CI workflow used a **separate** token stored as the GitHub Actions repository secret `SOCKET_SECURITY_API_KEY`, exposed to the Python process as `SOCKET_SECURITY_API_TOKEN`. Neither token value is in the repository.

## 2. First scan and interpreting results

| Observation | Evidence | Meaning |
|---|---|---|
| Baseline before third-party dependencies | Scan `ea295308-005a-4aeb-87f4-f525861e2fb4`: healthy, no alert records | An empty dependency result can be expected when manifests declare no external packages; it does not establish broad security coverage. |
| After adding PyYAML | Scan `1d9db0a0-20e8-4508-8255-b8ec0c353027`; `pypi/pyyaml/6.0.2` | Raw data contained **53 release-artifact records for one package**, not 53 independent dependencies. |
| Detected signals versus policy decisions | Raw scan showed potential-vulnerability, filesystem-access, native-code and other indicators; policy evaluations were Ignore | A finding's presence, relevance to this application and organization's chosen action are distinct. App uses `yaml.safe_load`, reducing the relevance of unsafe-constructor behavior to our actual ingestion path. |
| Local scan completion | `socket scan create --no-banner --repo=socket-technical-enablement-exercise --branch=main --default-branch --report .` | Local CLI supports explicit, reproducible full scans and policy evaluation; use `--no-banner` in live commands. |

When discussing the raw scan, avoid treating alert **occurrences**, distinct alert **types/keys**, release **artifacts**, and unique **dependencies** as interchangeable counts. Likewise, no published CVE does not imply zero other supply-chain signals.

## 3. Security-policy experiment: Ignore → Block → Warn → Inherit

The exercised alert type was **Potential vulnerability**, initially **Ignore (inherited)** in the organization's **Balanced** policy preset. A temporary org-wide override was deliberately used, then restored; this was a controlled test of an **alert type**, not a package-specific exception.

| Effective policy at scan creation | Scan ID | CLI outcome |
|---|---|---|
| Ignore (inherited), prior scan | `1d9db0a0-20e8-4508-8255-b8ec0c353027` | Healthy, no actionable alerts at default Error threshold |
| **Block** (CLI reports `policy: error`) | `1a1190d3-8b85-4692-9f01-310c3cc406bf` | **Unhealthy; exit code 1** |
| **Warn** | `46093b05-bcd0-438a-9592-4e2a8f045ef3` | **Healthy; exit code 0**; warning visible with `--report-level=warn` |
| Restore | User confirmed override returned to **Inherit** | Expected effective policy: Ignore (inherited); a separate post-restoration scan/screenshot was not recorded |

**Teaching point:** Policy changes altered the result of newly created scans; the already-created scan retained its previously reported evaluation when inspected in our experiment. Do not generalize this observation to all scan retention or reevaluation behavior without further testing. A **Warn** is visible in the appropriate report level but does not fail this CLI scan; a **Block** fails it.

## 4. Integration comparison: CLI vs GitHub App vs GitHub Actions

**Controlled test:** [Pull request #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) introduced `npm/picocolors@1.1.1` and used it to style the ActivityPulse heading. It also provided a controlled place to compare GitHub App and Actions on one PR; the PR was kept open for evidence collection.

| Dimension | Local npm Socket CLI | Socket GitHub App | GitHub Actions Python Socket CLI |
|---|---|---|---|
| Start during comparison | Manual terminal command | Connected App installed for **selected repository only**; automatic PR event | `pull_request` workflow; runner supplied by GitHub |
| Auth | Socket org-scoped token | GitHub App repository authorization | Socket token in GitHub Actions secret, plus GitHub-provided PR token |
| Primary evidence | CLI report, scan IDs, health, exit codes | [Socket bot comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620), PR checks and [dependency diff report (Socket organization access)](https://socket.dev/dashboard/org/mason-dillon-interview/diff-scan/b7326217-a2c7-4130-84ae-026912813e8c?tab=dependencies) | [Actions run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628), runner logs, [Actions bot comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7014418426) |
| Verified result | Manual dependency and policy evaluations successful | Detected newly added picocolors; supplied summary scores and successful PR/project checks | **Attempt 4 passed**; one added artifact; “No issues found” |
| Limitations | Must be triggered and interpreted by operator | Package category scores shown without package-specific explanation of deductions in reviewed views | Setup more involved; initial credential failures; preferred diff scan still falls back to streaming |

The GitHub App's PR overview for picocolors reported Supply Chain Security **100**, Vulnerability **100**, Quality **72**, Maintenance **80**, and License **100**. These are scores, not independent vulnerability counts. The user could inspect a package summary and public scoring-methodology page but not a concrete decomposition explaining the two lower scores.

### CI failure investigation and verified resolution

1. First Python CLI Actions run returned **HTTP 401 Unauthorized** for `/v0/python-cli-runs` and `/v0/organizations` (process exit **3**), despite successful checkout, Python setup and installation.
2. Switching the workflow environment-variable name did not resolve it. Creating a separate, more broadly scoped CI token also did not resolve it **while the wrong secret value was supplied**.
3. The effective fix was to place the actual **`sktsec_...` API token string** in the GitHub secret instead of a separate `SHA512-...==` value. Authentication and full scan then succeeded. **Do not conclude that broader scopes alone fixed the 401**.
4. A subsequent full rerun after adding `diff-scans:create` and `diff-scans:list` also **passed** (run #44557864628, **attempt 4**, November 19); however, logs **still** said `APIAccessDenied(Insufficient permissions)` for preferred diff-scan comparison and `effective=streaming` fallback. The precise remaining authorization reason is **unresolved** and does **not** invalidate the successful streaming scan.
5. GitHub runner warned that `actions/checkout@v4` and `actions/setup-python@v5` target deprecated Node 20 and were forced to run on Node 24. Non-blocking workflow-maintenance concern, not a Socket security finding.

**Concurrent reporting experiment:** Both `socket-security[bot]` and `github-actions[bot]` posted dependency-overview comments to PR #1. This reproduces the duplicate-feedback cost Socket warns about when GitHub App and CI PR reporting are used together. **Recommendation for normal use:** retain the GitHub App as the easiest default onboarding path and disable or narrow automatic Actions PR reporting after the experiment; retain CLI/CI as alternatives for explicit automation or independent pipeline gates. **Closure verified:** On PR #1 feature head `293b739b07cf5cfc081dd59982afaa02dc4e7599`, the Actions workflow trigger was changed to manual `workflow_dispatch` with a `pr_number` input. GitHub returned **no Actions workflow runs for the new head** after the update; PR #1 remains open, with both historical bot comments preserved. Socket GitHub App remains connected; fresh App behavior after this edit has not been independently re-tested. The manual workflow normally becomes dispatchable after it is present on the default branch.

## 5. Technical judgment questions

**Why organization-scoped and capability-scoped tokens?** Organization scope binds a credential to the correct tenancy; capability scope limits which operations that credential may invoke. This supports least privilege and independent rotation/revocation of local, CI and other credentials. GitHub App authorization is a **separate** trust boundary from Socket API-token scopes. The working local three-scope token and distinct CI token made that distinction concrete.

**When resolve an alert versus add a policy rule?** Use a **narrow resolution** for a specific reviewed finding (e.g., verified false positive or documented tolerable risk) bounded by repository, artifact/version and alert identity where possible. Use a **policy rule** to set intentional treatment for a **class of findings** across an agreed scope (Block/Warn/Monitor/Ignore). Avoid broad permanent resolutions that unintentionally suppress new versions or unrelated findings. The Block/Warn test altered an org-wide **policy**, not an alert resolution; no actual resolution lifecycle test was performed. [Conceptual reference notes](part-i-conceptual-notes.md) preserve official-source nuance.

## 6. Friction, documentation improvements and first-week teaching

The [firsthand friction log](friction-log.md) contains detailed observations and distinguishes confirmed product behavior from hypotheses. Prioritize these in discussion:

1. **Credential and CI onboarding:** The distinction between an actual `sktsec_` API token and other values was not obvious to the learner. The 401 error did not point to the corrective action. A task-based credential example, secret-value diagram, and troubleshooting flow would have shortened the failure. The preferred diff-scan authorization remained unclear despite adding documented scopes.
2. **Permissions discoverability:** Manual scan permissions were spread across command docs; the CI/CD guide described a broader permission set without making the preferred diff-scan requirements readily apparent. The [Socket CLI Permissions Explorer](https://docs.google.com/spreadsheets/d/1iQLzZkCqyz8XxqFjk2UQPY5TDkvVa1a49uHQ3eLOBPY/edit?usp=sharing) is a working Google Sheets reference with filters by customer role, persona, and use case, plus a deduplicated **Scopes to tick** list. It covers documented CLI commands and variants. Validate untested API paths before using it to provision tokens. Native CI diff-scan authorization remains unresolved in this exercise, and GitHub App authorization is separate from CLI token scopes.
3. **Package-score explainability:** The PR report displays five scores, but in the inspected views the user could not see package-specific reasons for Quality **72** and Maintenance **80**. Provide a “what it means → why this package scored this way → what to do” drill-down written for developer and analyst personas, with accessible evidence and examples. Do **not** speculate about whether the article was written by AI.
4. **Integration overlap:** Two bot comments on the same PR created avoidable review noise. Teach customers to choose one routine PR feedback path, with a bounded comparison only when there is a reason to test both.
5. **First-login ambiguity:** Earlier onboarding initially presented an unclear invitation versus new-organization flow; access was later confirmed. Add an explicit membership and organization-entitlement checkpoint.

**Recommended onboarding sequence for a new SE:** (a) verify account/org/repo access; (b) learn the package/finding/policy distinction with a known dependency; (c) perform one scoped local CLI scan; (d) connect the GitHub App to one selected repository and inspect a real PR; (e) add CI only when customer pipeline requirements justify it; (f) demonstrate Block vs Warn with a reversible policy adjustment; (g) explain resolution vs rule. Start with the **GitHub App** for a customer seeking fastest ongoing PR value; start with the CLI for a learner who needs to understand scan mechanics and policy enforcement.

## 7. Demo order, evidence and handoff decisions

**Suggested 5–8-minute Part I walkthrough:** Show ActivityPulse working; summarize baseline-versus-PyYAML scan; show Block/Warn result table; open [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) and point out App review plus Actions comment; show passing [Actions run attempt 4](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628), noting streaming fallback; conclude with one customer-onboarding recommendation and one concrete documentation improvement. Favor captured evidence over changing org policy live during the panel.

**Primary evidence index:** The public PR comments, Actions run, and [lab screenshots](part-iii-lab.md) provide evidence without access to the Socket organization.

- [Detailed execution history](part-i-walkthrough.md) — commands, scan IDs, observed results and caveats
- [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) — direct dependency change and both bots
- [Successful Actions run, attempt 4](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628) — job logs and permissions fallback
- [Friction log](friction-log.md) — firsthand product/docs assessment
- [Integration comparison protocol](integration-comparison.md) and [conceptual notes](part-i-conceptual-notes.md)
- [AI-use and verification log](ai-use-and-verification.md) — assistance and independent checks

**Minimal remaining Part I decisions:**
- [x] **End deliberate overlap:** user approved retention of GitHub App and suspension of automatic Actions PR scanning; changed feature-branch workflow to manual `workflow_dispatch` and observed no Actions run for new head. App remains installed. Future manual dispatch normally requires the workflow on the default branch.
- [x] **Keep PR #1 open through interview:** user explicitly selected this; GitHub verified PR state remains open at head `293b739`.
- [x] **Token decision:** user explicitly chose to **retain** the dedicated CI token after the interview; no token revoked, rotated or inspected.
- [ ] **Interview rehearsal:** choose one documentation improvement and one first-week teaching sequence; no requirement to polish every historical planning file.

**Submission interpretation:** The assignment's Part I involves hands-on demonstrations, conceptual answers and a friction log. This document serves as a compact discussion/evidence brief; the explicit advance-submission requirement is for **Part III** materials, not an assumed standalone Part I PDF. Do not assume this briefing has been emailed to the panel.
