# Part III — Guided Hands-on Lab: A Red Build Is Not Always a Security Block

**Duration:** 25 minutes (maximum 30)  
**Audience:** New Socket SE, TAM, or Support engineer  
**Project:** [ActivityPulse](https://github.com/mlddragon/socket-technical-enablement-exercise), a Node.js + Python activity-reporting CLI  
**Outcome:** Diagnose a policy-enforced Block, a non-blocking Warn, and an authentication failure; give a defensible, safe customer response.

## The story — Courtney's release decision (0–3 minutes)

Courtney (they/them) is the **lead software engineer** for ActivityPulse. They build features alongside their team and coach less-experienced engineers through reviews, releases, and production issues. Their team has recently added Socket to the software supply-chain review process.

ActivityPulse imports activity records using Python's PyYAML library and presents results through a Node.js CLI. Courtney's team is preparing a release when two apparently contradictory reports arrive. One Socket CLI scan says **unhealthy** and blocks the dependency under policy. A GitHub Actions job also turns red, but its log shows **401 Unauthorized**, not a package alert. Meanwhile, another scan of the same PyYAML dependency reports only a warning.

Courtney must decide whether a dependency needs security review, the CI configuration needs repair, or both. They cannot responsibly tell the team to bypass controls just because a build is red. The learner is stepping into Courtney's investigation: work from the evidence, tell the team what it actually means, and choose the next action.

### Before you begin

**What you will do:** Inspect saved Socket scan evidence and GitHub Actions logs; classify each result; communicate a safe next step. No changes to code, tokens, or policy are required.

**Why:** These historical results are real and reproducible as **read-only investigations**. The original policy was restored to Balanced / Inherit after the experiment, so re-running a new scan today is **not** expected to reproduce the same Block.

**Have ready:** A browser with access to the [exercise repository](https://github.com/mlddragon/socket-technical-enablement-exercise), a notes area, and—**only if you already have authorized read-only Socket org access**—Socket CLI v1.15.x. To fetch historical reports, the token needs `full-scans:list` and `security-policy:read`. Do not request or paste token values.

**If you lack Socket org access:** Use the **Provided evidence** under each activity. Complete the classification and handoff anyway. Do not create an account, modify permissions, or change organization policy just to run this lab.

**Safety:** Do not disclose credentials, install unknown packages, run malicious code, or change organization-wide policy. The lab analyzes past results rather than forcing a fresh Block.

---

## Activity 1 — Find the policy block (3–10 minutes)

### What you are going to do
You will inspect the historical **Block** scan for PyYAML and identify the exact evidence that makes it a security-policy decision rather than an infrastructure error.

### Why you are doing it
A red CI indicator alone does not say *why* something failed. You need the package, finding, effective policy, scan health, and observed command outcome before advising a customer or release team.

### Steps to complete

1. Open the [Part I evidence brief](part-i-briefing.md) in another tab, and scroll to **Section 3 — Security-policy experiment**.
2. Locate scan ID **`1a1190d3-8b85-4692-9f01-310c3cc406bf`** under the **Block** row. Keep that scan ID available.
3. **If you have authorized Socket CLI access**, open a terminal and run the read-only command:

   ~~~bash
   socket scan report 1a1190d3-8b85-4692-9f01-310c3cc406bf --json --fold=version --no-banner
   ~~~

   If it fails because you lack organizational access, stop that path and use the provided historical evidence below. Do not regenerate the token or change policy.
4. In the returned report—or in **Provided evidence**—find these four details: the package/version, alert type, policy action, and `healthy` result.
5. Record your findings in **Case A** of the worksheet at the end. In the **Next action** cell, describe what you would ask the dependency owner or security reviewer to assess before the release proceeds.

### Expected result — what it should look like

**Provided evidence (from the verified historical experiment; shortened for teaching):**

~~~text
Package:  pypi/pyyaml/6.0.2
Finding:  potentialVulnerability
Policy:   error  (Block)
Healthy:  false
Original combined create/report process exit code: 1
~~~

The explicit **`policy: error`**, the named package finding, and **`healthy:false`** demonstrate that analysis reached a policy-enforcement decision. Exit **1** was observed when the **original scan-create/report command** ran under Block; running the read-only `scan report` command above is not a repeat of that process exit test.

**Checkpoint:** You should be able to say, “This result was blocked by policy because Socket evaluated a specific PyYAML finding.” You should **not** conclude that PyYAML is malware, or advise disabling the policy to ship.

---

## Activity 2 — Find a warning that did not block (10–15 minutes)

### What you are going to do
You will examine a historical **Warn** scan of the same package and compare its action, health status, and report visibility with Activity 1.

### Why you are doing it
Security detection, visibility thresholds, and enforcement are separate concepts. A warning can be present even when the process succeeds and an Error-only report appears empty.

### Steps to complete

1. Return to **Section 3** of the [Part I evidence brief](part-i-briefing.md).
2. Locate the historical **Warn** scan ID **`46093b05-bcd0-438a-9592-4e2a8f045ef3`**.
3. If you have authorized CLI access, run:

   ~~~bash
   socket scan report 46093b05-bcd0-438a-9592-4e2a8f045ef3 --json --fold=version --report-level=warn --no-banner
   ~~~

   If you are working from case evidence, read the expected result below instead.
4. Find the package and `potentialVulnerability` alert. Look for `policy: warn` and `healthy:true`.
5. Compare this result with Case A. In **Case B** of the worksheet, record the difference and answer: **Which CLI option makes the warning visible?**

### Expected result — what it should look like

~~~text
Package:  pypi/pyyaml/6.0.2
Finding:  potentialVulnerability
Policy:   warn
Healthy:  true
Original combined scan process exit code: 0
Report visibility: --report-level=warn
~~~

The warning is **not a policy Block**. Its original combined create/report command exited **0**. In this exercise, using an Error-only threshold could hide warnings from the displayed alert summary; `--report-level=warn` includes them.

**Checkpoint:** You should be able to say, “Socket detected a finding, but the selected action warned rather than failing the scan.” Do not change the organization's current policy to try to reproduce this older result.

---

## Activity 3 — Investigate the failed GitHub Actions job (15–21 minutes)

### What you are going to do
You will inspect a real failed CI attempt, locate the **first meaningful error**, and compare it with the later successful scan.

### Why you are doing it
Courtney's team needs to know whether to assign this issue to a dependency/security owner or to the CI/credential owner. Different causes require different fixes.

### Steps to complete

1. Open [Socket Security CI — workflow run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).
2. **Find the run-attempt selector** near the run heading. Select **Attempt 1** (the first failed attempt). GitHub's interface may present attempts in a dropdown or link instead of a tab; if the selector is not obvious, use the run summary's attempts/history view.
3. Open the **socket-security** job. Expand **Run Socket Security Scan** in the step list. The earlier **checkout**, **Python setup**, and **Socket CLI installation** steps should show success.
4. In the scan step, find the earliest `401 Client Error: Unauthorized` entry. Note the requested endpoint `/v0/python-cli-runs`; the subsequent trace also references `/v0/organizations`. Find **Process completed with exit code 3**.
5. In **Case C** of the worksheet, record the failing stage and the HTTP status. Explain why this evidence does **not** establish a malicious dependency or a policy Block.
6. Return to the same workflow run's attempts/history, select **Attempt 4**, and expand **Run Socket Security Scan** again. Locate:
   - Successful **CLI run registration** and **Organization initialization**.
   - **No issues found** and a successful job.
   - The warning: **Diff scan comparison failed with APIAccessDenied(Insufficient permissions), falling back to the streaming scan comparison**.
7. In your notes, answer: Did the attempt-4 fallback cause the job to fail? What part of the process was working despite that warning?

### Expected result — what it should look like

**Attempt 1 — failed authentication:**

~~~text
Starting Socket Security CLI version 2.12.2
API request failed: 401 Client Error: Unauthorized
  .../v0/python-cli-runs
Unexpected error when running the CLI: Unauthorized
  .../v0/organizations
Process completed with exit code 3
~~~

**Attempt 4 — successful scan with limited comparison mode:**

~~~text
CLI run registration completed
Organization initialization completed
Diff scan comparison failed: insufficient permissions
Diff comparison mode: effective=streaming
No issues found
Job conclusion: success
~~~

The historical troubleshooting established that the original CI secret contained a different `SHA512-...==` value, while the working credential was the actual Socket API token beginning with `sktsec_`. Changing the secret value resolved the **401**. Additional scope changes were also tried, so you must not claim the expanded scopes alone were the cause or solution. **Never request or expose the complete token.**

**Checkpoint:** You should distinguish **failed authentication before analysis** from **completed analysis with a non-fatal fallback**. A non-blocking warning in a successful job is not the same thing as a 401.

---

## Activity 4 — Advise Courtney's team (21–25 minutes)

### What you are going to do
You will complete a short diagnosis worksheet and prepare customer-ready explanations for all three cases.

### Why you are doing it
Courtney must turn raw scan details into a safe engineering decision. The team needs the issue owner, supporting evidence, and the next action—not just “the build is red.”

### Steps to complete

1. Fill each row using evidence gathered in Activities 1–3. The **original observed exit code** may be included, but must not be your only justification.
2. Under your worksheet, write **two sentences per case**: the first states the verified facts; the second identifies the next safe action.
3. Read the three updates aloud as though you were briefing Courtney and their team.
4. Check that none of the updates claims malware without evidence, promises a root cause not established by logs, exposes tokens, or recommends bypassing the organization's policy.

### Expected result — what it should look like

| Case | Scan analysis completed? | Evidence to cite | Classification | Safe next action |
|---|---|---|---|---|
| A — Block | Your answer | Your answer | Your answer | Your answer |
| B — Warn | Your answer | Your answer | Your answer | Your answer |
| C — 401 | Your answer | Your answer | Your answer | Your answer |

**Self-check:** A should be an evaluated policy Block; B should be a non-blocking Warn; C should be authentication/tooling failure. For A, start with a dependency and policy review. For C, start with the correct credential and CI configuration **without exposing secret contents**. Bonus: identify attempt 4's streaming fallback as a remaining narrower permissions issue, not a failed scan.

## The story concludes — Courtney makes the call

Courtney now has three different engineering outcomes instead of one vague category called “Socket failed.” Their original PyYAML Block reached policy evaluation and requires an accountable security decision. The Warn result surfaces the same type of finding without stopping the scan. The GitHub Actions failure happened earlier, during authentication, and was repaired by correcting the credential stored in the CI secret; the later scan passed even though it fell back to a different comparison mode.

With the evidence separated, Courtney can send the dependency finding to the appropriate security reviewer and the credential issue to the CI owner. Their team does not need to bypass policy to fix authentication, and it does not need to troubleshoot credentials when a finding has actually been blocked. The important lesson is now part of Courtney's release process: **first identify where the operation failed, then decide who should act and why.**

---

## Facilitator notes (not learner steps)

- **Facilitator answer key:** A = package PyYAML 6.0.2, `potentialVulnerability`, policy `error`, unhealthy, original exit 1. B = same finding, `warn`, healthy, original exit 0, visible at `--report-level=warn`. C = Python CLI HTTP 401 before scan completion, original exit 3; actual token value correction resolved it. Attempt 4 succeeded with streaming comparison after a diff permission fallback.
- **If learner lacks org access:** Use supplied evidence blocks without asking for credentials. GitHub job logs remain the main clickable exercise; if the attempt selector is unavailable, provide sanitized excerpts rather than fabricating live access. Do not score an access constraint as learner incompetence.
- **Timing:** Narrative/orientation 3 min; Block 7; Warn 5; auth failure/success comparison 6; customer handoff 4 = **25 min**.
- **Do not conflate:** A CLI `scan report` inspection with the original `scan create --report` exit code; GitHub App PR comments with Python CI job status; a diff-scan fallback with total scan failure; detected indicators with confirmed maliciousness.
- **Assessment:** Use the separately authored [practical readiness check](part-iii-readiness-check.md). Learner meets readiness only after they can diagnose from evidence, communicate safely, and choose appropriate next actions. A 5–7-minute post-lab readiness assessment is separate from the 25-minute lab; if the full teaching session must stay within 30 minutes, use its condensed 5-minute scenario check.
- **References:** [Part I briefing](part-i-briefing.md), [detailed execution log](part-i-walkthrough.md), [GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).

