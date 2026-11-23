# Socket Technical Enablement Exercise

## Reviewer index

**Part III · Teach it back**

The Widgets Mfg scenario teaches a new Socket SE to show the same dependency change in GitHub Actions and the Socket GitHub App, then recommend a pilot based on the customer’s workflow.

| Required deliverable | Open | What to review |
|---|---|---|
| **1. Short hands-on lab** | [Widgets Mfg lab](socket-deliverables/part-iii-lab.md) | 30-minute exercise with a public template, starter files, and saved evidence for rehearsal. |
| **2. One-page customer talk track** | [Widgets Mfg talk track (PDF)](socket-deliverables/part-iii-talk-track.pdf) | Two developer views, likely customer objections, and a pilot recommendation. |
| **3. Practical readiness check** | [Five-minute readiness check](socket-deliverables/part-iii-readiness-check.md) | An observed demo, a customer question, and clear criteria for coaching or reassessment. |

The [Part III teaching package](socket-deliverables/teaching-package.md) collects these three links and explains what was verified.

## Panel evidence

| Discussion | Start here |
|---|---|
| **Friction log** | [Where setup was difficult](socket-deliverables/friction-log.md) · [Proposed documentation changes](socket-deliverables/part-i-briefing.md#6-friction-documentation-improvements-and-first-week-teaching) |
| **Part I · Getting familiar with Socket** | [Briefing](socket-deliverables/part-i-briefing.md) · [Original comparison PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) · [Evidence by assignment section](#part-i--getting-familiar-with-socket) |
| **Part II · Socket Firewall** | [Verified registry-mode results](socket-deliverables/part-ii-firewall-results.md) · [Startup and health](socket-deliverables/images/part-ii/P01-startup-health.png) · [Matching policy decision](socket-deliverables/images/part-ii/P06-matching-decision-log.png) |
| **Widgets demo verification** | Actions and the GitHub App passed on separate private training repos and each posted feedback for the `picocolors` change. Public comparison evidence is available in [verification PR #2](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) and its [Actions job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/45215148824/job/137834176673). |
| **AI use** | [AI use, corrections, and verification](socket-deliverables/ai-use-and-verification.md) |

[Current project status](socket-deliverables/PROJECT-STATUS.md) · [Run ActivityPulse](#run-activitypulse)

## Part I · Getting familiar with Socket

The [Part I briefing](socket-deliverables/part-i-briefing.md) summarizes the demonstration. This table maps Socket’s numbered instructions to the evidence.

| Instruction section | Evidence |
|---|---|
| **1. Create your first scan** | [CLI setup, first scan, and results](socket-deliverables/part-i-walkthrough.md#entry-002--token-and-first-local-cli-scan) · [Optional GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163) |
| **2. Compare integration paths** | [Dependency-change PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) · [CLI, GitHub App, and Actions tradeoffs](socket-deliverables/part-i-briefing.md#4-integration-comparison-cli-vs-github-app-vs-github-actions) · [Comparison results](socket-deliverables/integration-comparison.md) · [First-week teaching recommendation](socket-deliverables/part-i-briefing.md#6-friction-documentation-improvements-and-first-week-teaching) |
| **3. Enforce a policy** | [Block and Warn results with scan health and exit codes](socket-deliverables/part-i-briefing.md#3-security-policy-experiment-ignore--block--warn--inherit) · [Block screenshot](socket-deliverables/images/part-iii/cli-policy-block.png) · [Warn screenshot](socket-deliverables/images/part-iii/cli-policy-warn.png) |
| **4. Think through, no build needed** | [Token scopes and finding-level resolution versus policy rules](socket-deliverables/part-i-briefing.md#5-technical-judgment-questions) |
| **5. Prep for your interview** | [Demo order and evidence](socket-deliverables/part-i-briefing.md#7-demo-order-evidence-and-handoff-decisions) · [Friction log](socket-deliverables/friction-log.md) |

## ActivityPulse demo

**ActivityPulse** is the demo repository’s CLI. [Node.js](activitypulse/cli.js) invokes a [Python reporter](activitypulse/report.py), reads its JSON summary, and prints activity counts. The reporter reads the bundled [117-record sample CSV](activitypulse/data/activitypulse-activities.csv) or a YAML file. PyYAML provides the dependency used in the policy demonstration.

The Part III lab asks a Solutions Engineer to prepare both Socket integration paths and demo the same dependency change for a fictional engineering leader. It includes a reusable GitHub template, starter files, and authentic evidence for rehearsal. See the [three-part teaching package](socket-deliverables/teaching-package.md).

## Run ActivityPulse

From the repository root on `main`, with Node.js and Python 3.12 available:

```sh
python3.12 -m venv ../activitypulse-venv
../activitypulse-venv/bin/python -m pip install -r activitypulse/requirements.txt
ACTIVITYPULSE_PYTHON=../activitypulse-venv/bin/python node activitypulse/cli.js
```

The CLI prints **117 total records** and a count by activity type. No npm packages or Socket credentials are needed for this baseline. To read your own YAML file, invoke the reporter directly with `../activitypulse-venv/bin/python activitypulse/report.py /path/to/activities.yaml`. Use a list of records with an `activity_type` field in each record.

## Where the GitHub integration evidence lives

- **`main`** contains the working baseline and exercise materials.
- **[PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)** is open on `feature/activitypulse-cli-output`. It adds `picocolors` and retains a manual Actions workflow after the controlled comparison. The historical run used the earlier PR-triggered configuration. The branch-only workflow cannot be manually dispatched while it is absent from the default branch. [GitHub workflow trigger documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow#defining-inputs-for-manually-triggered-workflows)

## Additional work and supporting research

See the [appendix index](socket-deliverables/appendix/README.md) for supplemental assessments, documentation examples, research, and optional video drafts.

## Further reading

- [Repository guide for agents](AGENTS.md) explains where to find evidence and how the folders are organized.
- [Socket Deliverables index](socket-deliverables/README.md) index the supporting records.
