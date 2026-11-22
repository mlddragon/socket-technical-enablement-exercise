# Draft video script v1 — Socket CLI + GitHub App: Discover, Decide, Review

**Status:** Draft; not recorded, rendered or published (November 22, 2026). **Stretch goal only after Part II Firewall is operating and required Part III materials are ready.** Target 90–150 seconds. Use existing verified Part I evidence first; record additional screen footage only where a useful shot is missing. Keep Descript usage minimal.

## Consistent fictional scenario

**Harborline Software** is a fictional team of ~200 developers, with GitHub PRs and CI, evaluating when to use local CLI analysis versus automatic PR review. The company, team size and requirements are **scenario assumptions**. ActivityPulse and the actual scan/PR evidence are exercise artifacts. Don't represent fictional business impact, scan count, integration coverage, time savings, or unobserved product behavior as fact.

## Spoken script / visual plan v1

| Approx. time | Voiceover draft | Supporting image/clip | Verification and edit note |
| --- | --- | --- | --- |
| 0:00–0:15 | “Harborline Software wants two things: a way for engineers to investigate dependency risk in depth, and a way to bring that review into the pull requests where the team already works.” | Title, minimal workflow line: **CLI → investigation; GitHub App → review**. Mark Harborline “fictional scenario.” | Use a simple diagram, not an invented customer dashboard. |
| 0:15–0:34 | “Our demonstration project is ActivityPulse, a small Node.js CLI calling a Python reporter. We used the Socket CLI to scan the dependency manifests and then added the legitimate PyYAML dependency for YAML import.” | Repo `README.md`, `prod/cli.js` / `prod/report.py` with short terminal clip if captured. | 117 sample records; no private PATH data. |
| 0:34–0:54 | “The scan showed one PyYAML package represented by 53 release-artifact records. Those aren't 53 unique vulnerabilities. Findings, policy actions, and relevance must be interpreted separately.” | Actual Socket CLI reports, highlight exact package/interpretation; use Part I walkthrough. | Explicitly preserve artifact count vs distinct findings. |
| 0:54–1:17 | “We tested policy enforcement: under Block, a fresh scan was unhealthy and the command exited with code 1. Under Warn, the finding stayed visible, but the scan was healthy and the command exited with code 0. We returned the policy to Inherit afterward.” | Existing `project/images/part-iii/cli-policy-block.png` and `cli-policy-warn.png`, side by side with a small status table. | The Warn finding required `--report-level=warn` to display; only show actual report output. |
| 1:17–1:40 | “Now look at the GitHub App. We scoped the integration to our demo repository and opened PR number one adding `picocolors@1.1.1`. The App reviewed the dependency change and left check results and a comment where reviewers could act.” | Real [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1): sanitized screenshots of App check and dependency comment. Optional 8-second actual browser capture. | PR intentionally open; do not merge or change app settings just for footage. |
| 1:40–1:58 | “We also compared GitHub Actions, but its first run failed with a 401 authentication problem — not a blocked package. After correcting the token, an Actions scan passed. We observed duplicate App and Actions PR feedback, so chose the App as the normal PR path.” | Existing `project/images/part-iii/actions-search-401.png` and `actions-compare-success.png`; optional run link caption. | Do not label the 401 a policy block; Actions success used streaming fallback after permission denial. |
| 1:58–2:13 | “The recommendation isn't ‘use every integration everywhere.’ Teach the CLI for investigations and reproducible experiments, and the GitHub App when automatic, review-time feedback fits the customer's workflow. Use CI when pipeline context requires it, with clear ownership of duplicate feedback.” | Three-column closing: CLI / GitHub App / CI; small “customer workflow determines choice.” | Opinion based on our observed exercise; avoid universal product promises. |

## Missing footage / optional stretch capture

1. **G01:** 5–8-second terminal clip running ActivityPulse and showing the two-runtime nature; no user/private data.
2. **G02:** 8–10-second clip or still of a real Socket CLI scan and structured health/policy evidence. Existing screenshots can replace recording.
3. **G03:** Close crop of PR #1 GitHub App comment/check (with account identity redacted as necessary). Do not merge PR #1, alter policies or regenerate comments.
4. **G04:** 8-second compare of failed Actions 401 and later passing run. Existing screenshots already exist; additional footage not essential.
5. **G05 (stretch):** A natural documented integration troubleshooting issue, only if it arose and is supported by actual logs. No deliberate breakage of the ready-for-panel environment.

## Production rules

- First finish real Firewall proof. Then audit the existing screenshots for readable text at 1080p and record **only** missing shots. One short edited video is enough, not a full training series.
- Keep raw video privately, not in the public Git repo. Maintain a manifest of actual file locations. Sanitized stills may be committed with attribution.
- Import a selected short cut to Descript once; draft narration first, preserve free allowance, and evaluate any watermark before exporting a full demo.
- Any unrecorded scene remains a placeholder; don't show simulated product output as firsthand evidence.
- The video is an **optional portfolio enhancement**, not a fourth mandatory Part III deliverable. The exercise explicitly requests only the lab, one-page talk track, and readiness check.

## Source evidence

- [Part I walkthrough](../../part-i-walkthrough.md) · [Part I briefing](../../part-i-briefing.md) · [Integration comparison](../../integration-comparison.md) · [Friction log](../../friction-log.md)
- [Actual GitHub App PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)
- [Actual passing Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628)
- [Lab with screenshots](../../part-iii-lab.md)
- [Firewall plan (optional companion video)](../../part-ii-firewall-workplan.md).