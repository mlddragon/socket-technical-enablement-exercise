# Socket Technical Enablement Exercise

This repository shows how to scan a real dependency change with Socket, explain what the results mean, and teach a technical audience how to tell a policy Block from a scanner failure.

**ActivityPulse** is a small CLI. [Node.js](prod/cli.js) invokes a [Python reporter](prod/report.py), reads its JSON summary, and prints activity counts. The reporter reads the bundled [117-record sample CSV](project/data/activitypulse-activities.csv) or a YAML file. PyYAML provides the dependency used in the policy demonstration.

| Assignment | Status | Where to start |
|---|---|---|
| **Part I · Scan, integrate, and interpret** | **Complete** | [Part I briefing](project/part-i-briefing.md) and [execution walkthrough](project/part-i-walkthrough.md). See [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1), the [integration comparison](project/integration-comparison.md), and the [successful Actions job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163). |
| **Part II · Socket Firewall** | **Not attempted** | The registry-mode setup and policy-block demonstration are outstanding. |
| **Part III · Teach It Back** | **Lab complete. Two drafts remain.** | Start with the [25-minute hands-on lab](project/part-iii-lab.md). The [customer talk track](project/part-iii-talk-track.md) and [practical readiness check](project/part-iii-readiness-check.md) are drafts. |

The lab uses original CLI and GitHub Actions evidence to teach three decisions: when to review a blocked dependency, when to follow up on a warning, and when to hand an authentication failure to the CI owner. It includes screenshots and log excerpts for readers without Socket organization access.

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
