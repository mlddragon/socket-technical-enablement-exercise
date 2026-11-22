# Part III — Practical Readiness Check

**Topic:** Distinguishing a Socket policy block from scanner/tooling failures  
**Learner:** New SE / TAM / Support engineer  
**Check duration:** 5 minutes in the panel walkthrough or up to 7 minutes in a separate coaching session  
**Method:** Scenario interpretation and short customer handoff, not a recall-only quiz

## Scenario prompts
Provide the learner two anonymized snippets with no token material:

**Scenario 1 — Policy result**  
`pypi/pyyaml/6.0.2` · `potentialVulnerability` · `policy: error` · `healthy:false` · example CLI exit **1**.

**Scenario 2 — Infrastructure result**  
Python Socket CLI initialized, API response **401 Unauthorized** for `/v0/organizations`; scan could not complete; example CLI exit **3**.

**Follow-up probe:** Another scan yields `policy: warn`, `healthy:true`, exit **0**, but the first report shows no warnings. What flag/threshold should be checked?

Ask the learner to:
1. Categorize each scenario and say **which observed evidence**, not just an exit code, supports it.
2. State one safe next troubleshooting or remediation step for each.
3. Explain to a customer why a red job is not automatically a malicious-dependency verdict.
4. Describe how to access the warning without making a policy change.
5. Provide a concise, non-alarmist customer update without disclosing credentials.

## Run the five-minute check

Show the prompts with the answer key closed. Ask the learner to speak through their evidence and the next owner for each case.

| Time | Facilitator action |
|---|---|
| 0:00–1:00 | Hand over the two excerpts and ask for a first classification. |
| 1:00–3:00 | Ask for one piece of evidence and one safe next action per case. |
| 3:00–4:00 | Give the Warn prompt and ask how to make the finding visible. |
| 4:00–5:00 | Ask for a two-sentence customer update. Record the decision and any specific coaching need. |

Use a neutral prompt if the learner stalls. Ask “Which line would you show me?” and allow one correction before scoring.

## Observable rubric

| Competency | Ready behavior | Not-ready signal |
|---|---|---|
| **Diagnosis** | Explicitly distinguishes a completed, policy-evaluated scan from an API/auth failure | Calls every red pipeline result a policy block or malware finding |
| **Evidence** | Names package/version, alert type/action, scan health or actual HTTP error; recognizes exit codes are contextual | Relies solely on exit-code numbers or guesses at cause |
| **Safe next action** | Investigates the dependency/policy for Block; checks correct token reference and authorization for 401 without displaying secrets | Disables controls, broadens all permissions, or pastes tokens into public logs |
| **Warnings & visibility** | Understands Warn may be non-failing; uses `--report-level=warn` and distinguishes visibility from enforcement | Equates a hidden warning with absent detection or says Warn necessarily fails a build |
| **Customer communication** | Accurately separates observation from hypothesis, identifies owner and next action | Promises a root cause or remediation without corroborating evidence |

### Decision
**Ready** if all five competencies are demonstrated without any critical safety error, including at least one correct evidence-based distinction for each primary scenario and a usable customer-facing explanation. **Not ready** if there is any critical safety error, either scenario is misclassified after one coaching prompt, or the learner cannot identify evidence to support their conclusion.

**Critical safety errors:** revealing or requesting secret values in logs/tickets; changing organization-wide security policy to make a test pass without authorization; claiming scan failure establishes malware; recommending indiscriminate bypass of Block without risk ownership.

### Remediation for “not ready”
Coach the specific missed decision. Ask whether the scan completed, what it found, which action policy applied, and whether an API error interrupted the run. Replay the relevant saved output with a mentor, then repeat the performance check with a different sanitized example. Record the exact competency gap.

<details>
<summary>Facilitator answer key</summary>

- **Scenario 1:** Policy-enforced finding; analysis reached evaluation; investigate the package and agreed security posture before remediation/exception.
- **Scenario 2:** Authentication/tooling failure before successful dependency evaluation; validate GitHub secret is actual `sktsec_...` token and the intended scopes/organization, without disclosure. Actual historic cause was wrong secret value, not proven to be missing scopes.
- **Follow-up:** `--report-level=warn` on a compatible report command; a successful Warn scan still may contain findings.
- **Bonus distinction:** The successful CI run's insufficient-permission diff-scan fallback is a *partial capability* limitation while its streaming scan completed successfully, not another 401.

</details>

**Source:** [Part I briefing](part-i-briefing.md) and [verified Actions attempts](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).