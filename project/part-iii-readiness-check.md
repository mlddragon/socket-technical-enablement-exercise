# Practical readiness assessment · From demo to independent field execution

**Audience:** New Socket Solutions Engineers

**Customer:** Widgets Mfg and Courtney are fictional

**Teaching input:** [30-minute demo lab](part-iii-lab.md) and [customer talk track](part-iii-talk-track.md)

**Two distinct decisions:** A five-minute in-lab check establishes **demo readiness**. A separate **50–60-minute field assessment** is proposed to establish readiness to advance a supervised customer POC. The panel can see how the assessment works in five minutes; a learner cannot complete the field assessment in five minutes.

The original [Part I comparison](part-i-briefing.md) supplies real PyYAML Block/Warn scans, a CI 401, a later successful scan with a diff-scan permission fallback, and duplicate PR comments. The [Part II results](part-ii-firewall-results.md) supply a local Docker/Colima Firewall example with scoped TLS trust, an allowed install, and a policy-driven tarball 403. The enterprise variation below is **simulated**; none of this evidence demonstrates a Kubernetes, proxy, Artifactory, or Nexus deployment.

## 1. Five-minute in-lab check: ready to demo

During the lab's opening three minutes, ask for a 30-second first take: Which integration would the learner show Courtney first, why, and what does a developer do next? Record the answer without coaching. The final five minutes of the 30-minute lab are the observed check:

| Time | Evaluator prompt | Evidence to record |
|---|---|---|
| 0–3 min | “Show the same dependency change in GitHub Actions and the GitHub App from an engineer's point of view.” | Opens both views; identifies the producer, package/version, result, and next action. |
| 3–4 min | Ask one unannounced question: “Where do you start when this job is red?” or “Does this check stop a merge?” | Uses the failed stage or verified merge setting; says what remains unknown. |
| 4–5 min | “Which path would you pilot for Widgets Mfg, and what requirement would change your choice?” | Makes a customer-specific recommendation and acknowledges duplicate-feedback cost. |

**Ready to demo:** all three actions are independent, evidence-based, and free of critical errors. Allow one neutral “Where would you check?” prompt, but record it; directional help means **coaching needed**. A saved-result rehearsal can establish presentation readiness. Mark **live setup verified** only when the learner's own training paths ran and produced the expected results. Record the first take and final recommendation separately; this is coaching evidence, not a controlled pre/post performance measure.

Critical errors: exposing a credential; calling a 401 a dependency verdict or a red job proof of malware; promising that a check prevents merging without verifying the required-check setting; or recommending an unauthorized broad policy bypass. Practice the missed action and repeat with a different customer constraint or failed run. Record prompts and time to find each view.

## 2. Proposed field assessment: ready to advance a POC

### Candidate brief

> You are the SE for Widgets Mfg. Courtney wants dangerous dependencies surfaced early without making normal pull requests harder to ship. The team uses GitHub Actions and npm, and a security owner approves policy changes. Discover the team's workflow, recommend and demonstrate an initial Socket path using the provided training environment, interpret a finding and a failed run, propose an appropriately scoped policy decision, and hand Courtney a POC plan. Show what you verified and what still needs testing. You may use the shared lab, talk track, product documentation, and sanitized evidence. Keep credential values off screen and do not change organization-wide policy to make a demo pass.

**Evaluator setup, before the clock:** Prepare an authorized demo repository with a known dependency-change PR, either a working App integration or a staged Actions workflow and secret, access to the historical Block/Warn and failed/successful CI evidence, and a short customer-constraint card. Grant only the access needed. If the live route cannot run, provide saved results, record the access or product limitation, and do not award live-execution credit. The [lab](part-iii-lab.md) describes the two-repo setup and saved fallbacks. The separate [verification PR #2](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) showed both integrations on one pre-authorized repo; it did not validate two isolated learner repos end to end.

### Observed tasks and artifacts (50–60 minutes)

| Time | Learner action | Required artifact or observation |
|---|---|---|
| 0–8 min | Ask Courtney about dependency sources, PR/release workflow, required checks, security ownership, acceptable friction, and POC success. Explain the value in the customer's terms. | Discovery notes, one measurable POC success criterion, and a reason for the integration choice. |
| 8–23 min | Confirm organization/repository access and the chosen App or CI route. Set up or verify its scoped configuration, trigger the provided dependency change, **run/observe the resulting scan**, and demonstrate the developer view. | Repo/PR and run or scan link/ID, who produced the result, package/version, outcome, and any assistance or fallback. |
| 23–38 min | Interpret the package finding separately from its effective policy. Compare the saved PyYAML Block/Warn reports; diagnose the historical 401 and the successful streaming fallback. Choose a suitable Warn/Block treatment and review scope with the security owner; explain how enforcement would be verified. | Finding and policy decision record: observed evidence, customer-specific recommendation, approver, safe verification step, and untested assumptions. |
| 38–50 min | Work the enterprise variation below. Use shared documentation before asking an expert; isolate the failed hop, collect safe evidence, state the owner and escalation boundary. | Topology annotations, prioritized checks, evidence bundle, and escalation decision. |
| 50–60 min | Give Courtney a concise update and agree on the next POC milestone and success measure. Respond to one changed condition or objection. | Customer update, POC plan, and evaluator observation of independent response. |

**Policy verification boundary:** The saved Block/Warn scans demonstrate how the exercised alert type affected *those historical scans*. The current policy was returned to Inherit. A candidate can verify the historical result and present a specific proposed policy plus an authorized test plan. Mark the proposed customer's policy **not yet verified** unless an approved, isolated policy test is actually run and its outcome captured. Do not require an organization-wide policy change or suggest that changing a report visibility threshold changes enforcement.

### One enterprise variation (simulated)

Give the learner a compact topology: a Kubernetes-hosted CI runner uses an outbound proxy and internal CA; npm requests flow through Artifactory **or** Nexus and a proposed Socket Firewall route before an upstream registry. Choose **one** symptom card: TLS trust error, proxy/egress failure, registry route returning an unexpected status, or a Socket API authentication failure. Ask the learner to trace the request from developer/CI client through DNS and network path, proxy, certificate trust, registry/Firewall and upstream, then to Socket's policy decision. They should distinguish transport/authentication failures from a completed policy block, propose one safe isolation test, and name when platform, registry, security, or Socket specialists own the next step. Docker and the local Firewall result are supporting experience, not proof that this Kubernetes design works. Do not require a full implementation of every technology in one sitting.

### Behavioral scoring

Score each domain **0–4** from observed action and its artifact. Apply the same anchors across domains: **0** absent or unsafe; **1** unable to complete after a neutral prompt; **2** partially completes or needs directional help, with weak verification; **3** independently completes, cites evidence, states limits and next owner; **4** meets 3 and adapts accurately to a changed condition or objection. One neutral prompt (“What evidence would you check?”) is permitted and recorded. A substantive hint caps that domain at 2.

| Domain | What a score of 3 must show |
|---|---|
| Customer discovery and sales value | Discovers developer and security needs; explains risk reduction and developer friction; recommends a path tied to the workflow, with a falsifiable POC success criterion. |
| Setup, demo and scan | Uses authorized access, triggers and identifies an actual run/scan, verifies the package/result in the developer view, and distinguishes live action from saved evidence. |
| Findings and policy judgment | Separates detection, relevance, visibility and enforcement; supports a scoped policy choice with a risk owner; verifies only what the historical or authorized sandbox evidence actually shows. |
| Enterprise troubleshooting | Traces the chosen failure across CI/CD, Docker/Kubernetes environment, DNS/network/proxy/certificate trust, registry route and supply-chain policy; checks the likely hop safely and escalates with a useful evidence bundle. |
| Independent handoff | Uses shared resources, communicates verified facts and unknowns, assigns the right owner, and advances the POC with a measurable next milestone without avoidable expert dependence. |

**Pass:** at least **16/20**, **3 or more in every domain**, and no critical fail. This is readiness for a **supervised customer POC**, not proof of deep expertise in every enterprise platform. Critical fails: disclosure of secrets; unauthorized broad policy weakening or indiscriminate bypass; asserting a failed authentication step proves malware; presenting the simulated enterprise design or an unrun policy as verified; or concealing an unresolved security/connectivity dependency in the POC handoff. If live access is unavailable, record **simulation/rehearsal completed; live execution unverified** and defer a field-readiness pass until a live run is observed.

**Remediation:** Record the missed action and evidence, coach with the relevant lab section or shared runbook, then reassess that domain with a different but equivalent dependency, failure symptom, or customer constraint. A coached replay is practice; it does not replace independent reassessment. Two evaluators should independently score at least a sample and reconcile disagreements against specific actions and artifacts.

**Evaluator record:** Candidate/date; case and environment; first-take answer; live or saved mode; repo/PR/run/scan link; discovery criterion; policy finding and approver; simulated symptom and checks; customer/POC update; per-domain scores and supporting observations; prompts; critical fail if any; pass or reassessment; next coach and date. Never record token values.

### Validate field impact after the exercise

Pilot the assessment with several SEs. Use equivalent **baseline and post-training** customer cases with different fixtures, the same five domains, time limits, and help rules. Check scoring agreement between evaluators. Have a manager observe the first real POC and follow up at 30 days: note whether the SE performed discovery, demo, policy judgment, and handoff without rescue; whether POC milestones and customer decision criteria were met; time from training to independent execution; and escalations per comparable POC split into **appropriate specialist escalations** and **avoidable requests answered by shared guidance**. Report sample size, case mix, access constraints, and support received. Do not attribute a change in these measures to training without a design that supports that causal claim.

## Five-minute panel walkthrough of the field assessment

1. **0:00–0:45:** Show Courtney's brief and the five scored actions; distinguish the five-minute in-lab demo gate from the 50–60-minute field assessment.
2. **0:45–1:45:** Play two discovery questions and a workflow-based App/CI pilot recommendation that accounts for developer friction.
3. **1:45–2:45:** Point to the real saved Block/Warn and 401/successful fallback evidence. Ask what the learner may conclude and what remains unverified.
4. **2:45–3:45:** Show the labeled simulated proxy/CA/registry symptom and the evidence and escalation expected, without presenting it as a completed deployment.
5. **3:45–5:00:** Score one example at independent 3 versus coached 2. Show the pass rule, artifact record, and how comparable cases and manager observation would test field impact.
