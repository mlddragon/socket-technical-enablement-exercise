# Socket exercise repository guide

This repository contains Mason Dillon’s Socket Technical Enablement Lead interview exercise. It includes an application used for the hands-on work, evidence from that work, and materials for teaching it to a new SE, TAM, or Support Engineer.

## Where to start

1. Open the [reviewer index](README.md#reviewer-index). It maps the assignment requirements to files, evidence, and the appendix.
2. Read [current project status](socket-deliverables/PROJECT-STATUS.md) before assessing completion. It distinguishes completed work, drafts, and work that has not been attempted.
3. Follow the relevant evidence below. Use the [Socket Deliverables index](socket-deliverables/README.md) for supporting records and the [research index](research/README.md) for background.

## Repository layout

| Location | What belongs there | How to read it |
|---|---|---|
| [`socket-deliverables/`](socket-deliverables/README.md) | Reviewer-facing deliverables, reports, screenshots, and supplemental enablement materials. | Start with the current evidence links. Draft labels apply to individual files. Use this folder for current deliverables and evidence. |
| [`research/`](research/README.md) | Training preparation, community observations, source notes, and hypotheses. [Historical planning](research/README.md#historical-planning) covers the dated plans, PRD, and artifact inventory. | Use it to trace the thinking or find sources. An attributed report or hypothesis needs separate evidence before it can support a claim about Socket behavior. |
| [`activitypulse/`](activitypulse/) | The ActivityPulse application, runtime manifests, and bundled sample data. | [`cli.js`](activitypulse/cli.js) invokes [`report.py`](activitypulse/report.py) and formats the summary. The app reads the [anonymized CSV fixture](activitypulse/data/activitypulse-activities.csv) from `activitypulse/data/`, alongside its [provenance notes](activitypulse/data/README.md). Use the [README run instructions](README.md#run-activitypulse). |

Keep new deliverables and their evidence in `socket-deliverables/`, exploratory material in `research/`, and application code and runtime requirements in `activitypulse/`. Use the indexes to distinguish the current deliverables from retained planning records.

## Evidence map

- **Friction log and AI use.** [Friction log](socket-deliverables/friction-log.md) records firsthand gaps and documentation recommendations. [AI use and verification](socket-deliverables/ai-use-and-verification.md) records how AI was used, what was corrected, and how outputs were checked.
- **Part I · Getting familiar with Socket.** [Briefing](socket-deliverables/part-i-briefing.md) summarizes the scans, integration comparison, and Block versus Warn demonstration. [Walkthrough](socket-deliverables/part-i-walkthrough.md) is the chronological record. The [README mapping](README.md#part-i--getting-familiar-with-socket) points to evidence for each numbered requirement.
- **Part II · Socket Firewall.** The [verified registry-mode results](socket-deliverables/part-ii-firewall-results.md) record the allowed install, policy block, matching request ID, and evidence inventory. The [workplan](socket-deliverables/part-ii-firewall-workplan.md) contains the procedure.
- **Part III · Teach it back.** The [teaching package index](socket-deliverables/teaching-package.md) links the three submission deliverables. The [Widgets Mfg lab](socket-deliverables/part-iii-lab.md) uses a template and starter files to compare the same dependency change in GitHub Actions and the GitHub App. Saved captures support rehearsal. The [five-minute readiness check](socket-deliverables/part-iii-readiness-check.md) is part of the lab.
- **Additional work.** The [appendix index](socket-deliverables/appendix/README.md) links the proposed field assessment, live Permissions Explorer, documentation drafts, optional video scripts, and research. The proposed field assessment is distinct from the five-minute Part III readiness check.

## Read the evidence in context

- The baseline app and documentation are on `main`. [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) contains the color enhancement and the feature-branch manual Actions workflow. The [integration comparison](socket-deliverables/integration-comparison.md) explains which earlier configuration produced the historical Actions run. [PR #2](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) verifies the Widgets starter on one authorized repo. Check the relevant branch or commit when citing code and workflow behavior.
- Treat dated plans as evidence of intent. Use the committed artifacts, original captures, and linked run or PR evidence for observed results. Some Socket reports require organization access. The lab and briefing link to evidence that can be reviewed without that access.
- For a review, use read-only checks. Use the saved evidence for policy and credential behavior, and keep secret values and private source data out of findings and repository changes.
