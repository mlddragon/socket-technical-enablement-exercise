# Practical readiness check · Present both Socket integration paths

**Audience:** New Solutions Engineers

**Duration:** Five minutes, included in the 30-minute lab

Ask the learner for a 30-second first take at the beginning of the lab. Record which path they would show, why, and one action they expect a developer to take. Give no coaching. Score the recommendation and developer’s next action again at the end. Record demo navigation and prompting separately.

## Run the check

1. **0–3 minutes:** Ask the learner to demo GitHub Actions and the GitHub App for Courtney. They should show the same dependency change, identify who produced each result, and point to where the developer would take their next action.
2. **3–4 minutes:** Ask one question they did not receive during the walkthrough. For example, “Where would my engineer start if the job is red?” or “What setting determines whether this can block a merge?”
3. **4–5 minutes:** Ask which path they would pilot at Widgets Mfg and what customer requirement would change that choice. Record the result and one concrete coaching need.

| Observe | Ready behavior | Coaching signal |
|---|---|---|
| **Two-view demo** | Opens both views independently and points to the same package and version. Identifies the CI job and App output. | Cannot find a view or misattributes a comment or check. |
| **Developer next step** | Shows where the engineer sees feedback and what they do with it in each path. | Lists features without showing the engineer’s workflow or next action. |
| **Customer follow-up** | Uses a failed stage or verified setting to support the answer. Identifies what to verify when evidence is missing. | Calls a 401 a dependency verdict or claims merge enforcement from a check alone. |
| **Pilot recommendation** | Chooses a primary path based on Courtney’s workflow and explains what would change the recommendation. | Suggests both feedback paths by default without accounting for duplicate notifications. |

**Ready to demo** means all four behaviors are demonstrated without coaching or a critical error. Treat exposing credentials, claiming a policy verdict with no analysis, or promising merge enforcement without evidence as critical errors. Record the mode as **live setup and demo** or **demo rehearsal from saved results**. Either can demonstrate presentation readiness. Live setup proficiency requires both paths to have run and produced their expected evidence.

If coaching is needed, practice the missed action, then repeat the check with a different customer constraint or failed run. Record time to find each view, prompts required, and the improvement from the first take. [Hands-on lab](part-iii-lab.md) · [Customer talk track](part-iii-talk-track.pdf)
