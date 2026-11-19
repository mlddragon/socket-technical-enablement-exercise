# Socket exercise repository guide

This repository contains Mason Dillon’s Socket Technical Enablement Lead interview exercise. It includes an application used for the hands-on work, evidence from that work, and materials for teaching it to a new SE, TAM, or Support Engineer.

## Where to start

1. Open the [reviewer index](README.md#reviewer-index). It maps the assignment requirements to files, evidence, and the appendix.
2. Read [current project status](project/PROJECT-STATUS.md) before assessing completion. It distinguishes completed work, drafts, and work that has not been attempted.
3. Follow the relevant evidence below. Use the [project index](project/README.md) for supporting records and the [research index](research/README.md) for background.

## Repository layout

| Location | What belongs there | How to read it |
|---|---|---|
| [`project/`](project/README.md) | Reviewer-facing deliverables, reports, screenshots, and supplemental enablement materials. | Start with the current evidence links. Draft labels apply to individual files. Dated plans, the PRD, and the artifact inventory are historical records. |
| [`research/`](research/README.md) | Training preparation, community observations, source notes, hypotheses, and rough ideas that informed the exercise. | Use it to trace the thinking or find sources. An attributed report or hypothesis needs separate evidence before it can support a claim about Socket behavior. |
| [`prod/`](prod/) | The ActivityPulse application and its runtime manifests. | [`cli.js`](prod/cli.js) invokes [`report.py`](prod/report.py) and formats the summary. The app reads the [anonymized CSV fixture](project/data/activitypulse-activities.csv) from `project/data/`, alongside its [provenance notes](project/data/README.md). Use the [README run instructions](README.md#run-activitypulse). |

Keep new deliverables and their evidence in `project/`, exploratory material in `research/`, and application code and runtime requirements in `prod/`. Use the indexes to distinguish the current deliverables from retained planning records.

## Evidence map

- **Friction log and AI use.** [Friction log](project/friction-log.md) records firsthand gaps and documentation recommendations. [AI use and verification](project/ai-use-and-verification.md) records how AI was used, what was corrected, and how outputs were checked.
- **Part I · Getting familiar with Socket.** [Briefing](project/part-i-briefing.md) summarizes the scans, integration comparison, and Block versus Warn demonstration. [Walkthrough](project/part-i-walkthrough.md) is the chronological record. The [README mapping](README.md#part-i--getting-familiar-with-socket) points to evidence for each numbered requirement.
- **Part II · Socket Firewall.** Use the [Firewall status](project/PROJECT-STATUS.md#part-ii--if-time-permits) for this part. Firewall planning and research do not establish that registry mode was run or a block was demonstrated.
- **Part III · Teach it back.** The [teaching package index](project/teaching-package.md) links the hands-on lab, one-page talk track, and practical readiness check with their current statuses. The [lab](project/part-iii-lab.md) contains original terminal and Actions screenshots, log excerpts, and a learner answer key.
- **Additional work.** The [README appendix](README.md#additional-work-and-supporting-research) links the live Permissions Explorer, Package Scores rewrite, and supporting research. The Explorer is a documentation-based reference with untested scope paths. The rewrite is a separately labeled draft.

## Read the evidence in context

- The baseline app and documentation are on `main`. [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) contains the color enhancement and the feature-branch manual Actions workflow. The [integration comparison](project/integration-comparison.md) explains which earlier configuration produced the historical Actions run. Check the relevant branch or commit when citing code and workflow behavior.
- Treat dated plans as evidence of intent. Use the committed artifacts, original captures, and linked run or PR evidence for observed results. Some Socket reports require organization access. The lab and briefing link to evidence that can be reviewed without that access.
- For a review, use read-only checks. Use the saved evidence for policy and credential behavior, and keep secret values and private source data out of findings and repository changes.
