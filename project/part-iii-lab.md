# Part III — Hands-on Lab (25 minutes)

## Is it a security policy block or a tooling failure?
**Audience:** New Socket SE, TAM, or Support engineer  
**Duration:** 25 minutes (maximum 30)  
**Format:** Guided individual lab using actual sanitized ActivityPulse scan evidence, with a terminal when the lab organization is available  
**Prerequisites:** Socket CLI v1.15.x, read access to the exercise's historical scan IDs, and optional org-scoped token allowing `full-scans:list` + `security-policy:read`. No token values included. **Do not change organization-wide policies during this lab.**

### Outcome
Given two failing scan situations, the learner determines whether Socket blocked a dependency under policy or whether the scan failed before evaluation, substantiates the classification from evidence, and recommends a safe next action.

### Learning contract
- A **policy block** means the scan completed its analysis and the current policy produced an enforceable finding.
- An **authentication/tooling failure** means the scanner could not complete its intended operation; it is not evidence that a dependency was judged unsafe.
- A process exit code is a clue, **not enough alone** to diagnose an arbitrary failure. Correlate the message, scan health, policy action, and operation stage.
- Historical scans can preserve evaluations made under prior policy settings. The organization's current Balanced policy is restored to Inherit; **do not reconfigure it** to reproduce the earlier block.
- All example outputs below are condensed from firsthand tests. No package code is executed or malicious dependency installed.

## Learner workflow

### 0–3 min — Orient
1. Identify the two execution paths: manual macOS `socket scan` (npm Socket CLI 1.15.0) and GitHub Actions Python `socketcli` (socketsecurity 2.12.2). They are different executables.
2. Open [Part I evidence brief](part-i-briefing.md) for the scan IDs, and [GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628) for runner logs.
3. Confirm read-only investigation: do not share tokens, change global policy, or rerun a failing CI job with credentials not provisioned for the lab.

### 3–10 min — Case A: Policy-enforced block (hands-on CLI)
**Evidence ID:** `1a1190d3-8b85-4692-9f01-310c3cc406bf`

If the CLI and authorized read token are available, inspect the saved report:

```bash
socket scan report 1a1190d3-8b85-4692-9f01-310c3cc406bf --json --fold=version --no-banner
```

**Expected from prior verified run:** PyYAML 6.0.2 `potentialVulnerability` with `policy: error`; scan `healthy:false`; earlier combined create/report command returned exit code **1**. If report access is unavailable, use the historical evidence table in [Part I brief §3](part-i-briefing.md) rather than claiming a new live verification.

**Learner records:** package/version, finding type, action, health, and what specifically distinguishes the alert from an API/auth error.

**Question:** Why is `healthy:false` meaningful here, and what should a customer review before allowing a dependency?

### 10–15 min — Case B: Warning, not a block (hands-on CLI)
**Evidence ID:** `46093b05-bcd0-438a-9592-4e2a8f045ef3`

```bash
socket scan report 46093b05-bcd0-438a-9592-4e2a8f045ef3 --json --fold=version --report-level=warn --no-banner
```

**Expected from prior verified run:** Same PyYAML finding but `policy: warn`, `healthy:true`; original scan command returned **0**. **Important:** Without `--report-level=warn`, a report at Error threshold may display no alerts. The historical Warn action was later restored to inherited Ignore.

**Learner records:** Which flag exposed the warning? Why does the warning not fail this scan? Does a current policy setting necessarily rewrite the old scan's output?

### 15–21 min — Case C: Tooling/authentication failure (GitHub hands-on)
Open [Actions run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628), inspect the **failed first attempt** and the successful third/fourth attempts. On the failed attempt, checkout and Python installation worked, then Python Socket CLI returned **401 Unauthorized** at `/v0/python-cli-runs` and `/v0/organizations` with process exit **3**; the scanner never completed dependency evaluation.

**Verified fix:** The repository secret initially contained a different `SHA512-...==` value. Using the actual `sktsec_...` token as the GitHub secret resolved 401 and scans completed. **Never paste either value into a log, issue, or support ticket.** An expanded-scope token was also created during troubleshooting, so **do not claim scopes alone fixed the 401**.

Compare successful attempt 4: `No issues found`; preferred diff-scan operation still returned insufficient permissions and fell back to **streaming** comparison. This fallback did **not** make the job fail.

**Learner records:** first failing operation, diagnostic message, what evidence rules out a policy block, and one safe credential-validation step.

### 21–25 min — Customer handoff
For each case, write a two-sentence customer update: (1) established facts and (2) next safe action. Categorize:
- A: policy-enforced security finding
- B: allowed warning
- C: API authentication/tooling failure

**Deliverable:** Completed mini evidence table below and two customer-facing sentences per case.

| Case | Execution completed? | Finding / API error | Health / exit code (observed) | Classification | Recommended next action |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| C | | | | | |

### Facilitator reference / assessment
- **A:** Analysis reached policy evaluation, specific package alert action **error/Block**, unhealthy, command exit 1; investigate dependency behavior and applicable policy, not secret rotation.
- **B:** Analysis reached evaluation, **Warn**, healthy and exit 0; lower report threshold reveals the warning.
- **C:** Python CLI returned **401** before scan analysis, exit 3; validate GitHub repository secret's actual token format, scope and intended environment without revealing the value; don't label dependency malicious.
- **Bonus:** Distinguish CI diff-scan fallback (successful, limited comparison mode) from 401 failure; tell customer when to escalate a missing permission rather than call the entire job failed.

### Accessibility / contingencies
If the historical scan IDs are inaccessible to participants in other orgs, **do not move or publish sensitive organization data**. The facilitator can provide the short sanitized observations above as case cards, and learners still navigate GitHub logs and fill the evidence table. A separately provisioned sandbox may be used for live demonstrations only after explicit instructor authorization. The exercise teaches diagnosis rather than requiring an org-wide policy modification.

**Source evidence:** [Part I briefing](part-i-briefing.md), [Part I walkthrough](part-i-walkthrough.md), [GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).