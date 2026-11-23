# Socket Technical Enablement Exercise

## Reviewer index

Use this index alongside Socket’s **Technical Enablement Lead Peer Interview** instructions. Start with the friction log, which opens the panel discussion.

| Requested item | Status | Open |
|---|---|---|
| **Friction log** | Parts I and II recorded | [Friction log](project/friction-log.md) · [Proposed public docs changes](project/part-i-briefing.md#6-friction-documentation-improvements-and-first-week-teaching) |
| **Part I · Getting familiar with Socket** | Complete | [Part I evidence by assignment section](#part-i--getting-familiar-with-socket) |
| **Part II · Socket Firewall** | Registry-mode enforcement verified | [Demo results and evidence](project/part-ii-firewall-results.md) · [Runbook](project/part-ii-firewall-workplan.md) |
| **Part III · Short hands-on lab** (30 minutes or less) | Packaged · 30 minutes | [Hands-on lab](project/part-iii-lab.md) |
| **Part III · One-page talk track** | One-page layout verified | [One-page PDF](project/part-iii-talk-track.pdf) · [Text version](project/part-iii-talk-track.md) |
| **Part III · Practical readiness check** | Ready to run | [Practical readiness check](project/part-iii-readiness-check.md) |
| **AI use log** | Recorded | [AI use, corrections, and verification](project/ai-use-and-verification.md) |
| **Appendix** | Supplemental | [Additional work and supporting research](#additional-work-and-supporting-research) |

## Additional work and supporting research

These materials supplement the exercise and sit outside the three required Part III deliverables.

| Additional work | Open | What it shows |
|---|---|---|
| **Socket CLI Permissions Explorer** | [Socket CLI Permissions Explorer](https://docs.google.com/spreadsheets/d/1iQLzZkCqyz8XxqFjk2UQPY5TDkvVa1a49uHQ3eLOBPY/edit?usp=sharing) · [Design brief](research/planning/cli-permissions-worksheet-handoff.md) | Google Sheets reference covering 68 commands and variants. Filter by customer role, persona, or use case and see a deduplicated **Scopes to tick** list. The shared sheet is open for comments. Use an editable copy to try the dropdowns. Scope entries are based on documentation and CLI help, with live API verification still needed for untested paths. |
| **Package Scores documentation rewrite** | [Repository draft](project/package-scores-rewrite.md) · [Google Doc review copy](https://docs.google.com/document/d/1bm8TfSpiRpJJDsCublt_rcPcJtmmN5wza23yOrIHb8Q/edit) | Proposed rewrite for people interpreting scores in their daily work. AI-assisted draft awaiting human review. |
| **Progressive disclosure documentation skill** | [Full skill instructions](project/appendix/progressive-disclosure-docs/SKILL.md) · [Firewall Registry Mode rewrite draft](project/appendix/socket-firewall-registry-mode-rewrite.md) | Reusable approach from the Package Scores rewrite, tested on another dense Socket page. The Firewall draft demonstrates the writing method. See the [Part II results](project/part-ii-firewall-results.md) for the live test. |
| **Socket community research** | [Enablement themes](research/discord-enablement-themes-2026.md) · [Detailed findings](research/discord-may-nov-2026.md) | Attributed customer and community reports that informed the training and documentation ideas. |
| **Teaching delivery options** | [Training platform comparison](research/training-platform-options-2026-11-18.md) | Research into authoring and sharing options for the teaching package. |
| **ActivityPulse design** | [Product requirements and assignment mapping](research/planning/PRD.md) | Historical design record for the two-runtime demo and its role in the exercise. |

[Run ActivityPulse](#run-activitypulse) · [Current project status](project/PROJECT-STATUS.md)

## Part I · Getting familiar with Socket

The [Part I briefing](project/part-i-briefing.md) is the short overview. Each row below points to the evidence for that numbered section of Socket’s instructions.

| Instruction section | Evidence |
|---|---|
| **1. Create your first scan** | [CLI setup, first scan, and results](project/part-i-walkthrough.md#entry-002--token-and-first-local-cli-scan) · [Optional GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163) |
| **2. Compare integration paths** | [Dependency-change PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) · [CLI, GitHub App, and Actions tradeoffs](project/part-i-briefing.md#4-integration-comparison-cli-vs-github-app-vs-github-actions) · [Comparison results](project/integration-comparison.md) · [First-week teaching recommendation](project/part-i-briefing.md#6-friction-documentation-improvements-and-first-week-teaching) |
| **3. Enforce a policy** | [Block and Warn results with scan health and exit codes](project/part-i-briefing.md#3-security-policy-experiment-ignore--block--warn--inherit) · [Original report screenshots](project/part-iii-lab.md#side-by-side-comparison-for-step-4) |
| **4. Think through, no build needed** | [Token scopes and finding-level resolution versus policy rules](project/part-i-briefing.md#5-technical-judgment-questions) |
| **5. Prep for your interview** | [Demo order and evidence](project/part-i-briefing.md#7-demo-order-evidence-and-handoff-decisions) · [Friction log](project/friction-log.md) |

## ActivityPulse demo

**ActivityPulse** is the demo repository’s CLI. [Node.js](prod/cli.js) invokes a [Python reporter](prod/report.py), reads its JSON summary, and prints activity counts. The reporter reads the bundled [117-record sample CSV](prod/data/activitypulse-activities.csv) or a YAML file. PyYAML provides the dependency used in the policy demonstration.

The Part III lab asks a Solutions Engineer to prepare both Socket integration paths and demo the same dependency change for a fictional engineering leader. It includes a reusable GitHub template, starter files, and authentic evidence for rehearsal. See the [three-part teaching package](project/teaching-package.md).

## Run ActivityPulse

From the repository root on `main`, with Node.js and Python 3.12 available:

```sh
python3.12 -m venv ../activitypulse-venv
../activitypulse-venv/bin/python -m pip install -r prod/requirements.txt
ACTIVITYPULSE_PYTHON=../activitypulse-venv/bin/python node prod/cli.js
```

The CLI prints **117 total records** and a count by activity type. No npm packages or Socket credentials are needed for this baseline. To read your own YAML file, invoke the reporter directly with `../activitypulse-venv/bin/python prod/report.py /path/to/activities.yaml`. Use a list of records with an `activity_type` field in each record.

## Where the GitHub integration evidence lives

- **`main`** contains the working baseline and exercise materials.
- **[PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)** is open on `feature/activitypulse-cli-output`. It adds `picocolors` and retains a manual Actions workflow after the controlled comparison. The historical run used the earlier PR-triggered configuration. The branch-only workflow cannot be manually dispatched while it is absent from the default branch. [GitHub workflow trigger documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#defining-inputs-for-manually-triggered-workflows)

## Further reading

- [Repository guide for agents](AGENTS.md) explains where to find evidence and how the folders are organized.
- [Friction log and documentation recommendations](project/friction-log.md) record onboarding, permissions, and interpretation issues from the exercise.
- [Current project status](project/PROJECT-STATUS.md) tracks completed work and remaining milestones. [Project notes](project/README.md) index the supporting records.
