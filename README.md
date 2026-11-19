# Socket Technical Enablement Exercise

## Reviewer index

Use this index alongside Socket’s **Technical Enablement Lead Peer Interview** instructions. Start with the friction log, which opens the panel discussion.

| Requested item | Status | Open |
|---|---|---|
| **Friction log** | Part I recorded | [Friction log](project/friction-log.md) · [Proposed public docs changes](project/part-i-briefing.md#6-friction-documentation-improvements-and-first-week-teaching) |
| **Part I · Getting familiar with Socket** | Complete | [Part I evidence by assignment section](#part-i--getting-familiar-with-socket) |
| **Part II · Socket Firewall** | Not attempted | [Status and outstanding evidence](project/PROJECT-STATUS.md#part-ii--if-time-permits) |
| **Part III · Short hands-on lab** (30 minutes or less) | Complete · 25 minutes | [Hands-on lab](project/part-iii-lab.md) |
| **Part III · One-page talk track** | Draft | [One-page talk track](project/part-iii-talk-track.md) |
| **Part III · Practical readiness check** | Draft | [Practical readiness check](project/part-iii-readiness-check.md) · [What “not ready” looks like](project/part-iii-readiness-check.md#decision) |
| **AI use log** | Recorded | [AI use, corrections, and verification](project/ai-use-and-verification.md) |

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

**ActivityPulse** is the demo repository’s CLI. [Node.js](prod/cli.js) invokes a [Python reporter](prod/report.py), reads its JSON summary, and prints activity counts. The reporter reads the bundled [117-record sample CSV](project/data/activitypulse-activities.csv) or a YAML file. PyYAML provides the dependency used in the policy demonstration.

The Part III lab uses original CLI and GitHub Actions evidence to teach when to review a blocked dependency, when to follow up on a warning, and when to hand an authentication failure to the CI owner. It includes screenshots and log excerpts for readers without Socket organization access.

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

- [Friction log and documentation recommendations](project/friction-log.md) record onboarding, permissions, and interpretation issues from the exercise.
- [Package Scores rewrite](project/package-scores-rewrite.md) is an additional documentation draft outside the required teaching package.
- [Current project status](project/PROJECT-STATUS.md) tracks completed work and remaining milestones. [Project notes](project/README.md) index the supporting records.
