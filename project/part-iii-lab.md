# Prepare a Socket demo for Widgets Mfg

**Audience:** New Socket Solutions Engineers

**Duration:** 30 minutes, including the customer rehearsal

## Your next customer call

You’re the Solutions Engineer supporting Widgets Mfg, which is in the later stages of evaluating Socket. Courtney, a senior manager of engineering, wants to understand what adopting Socket would change for their engineers day to day.

> Take me through an engineer’s pull request. If we put Socket in CI, what will they see? If we use the GitHub App, what will they see? In each case, when would they need to do something, and what would they do next?

Prepare two demos that use the same dependency change. Show where engineers see feedback, what happens on a routine change, and what they do if a result needs attention. Close with a recommendation tied to Widgets Mfg’s workflow.

Widgets Mfg and Courtney are fictional. The ActivityPulse dependency change comes from the original exercise. The template uses fictional activity data. [Original dependency PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)

## Before the clock starts

- From the [ActivityPulse GitHub template](https://github.com/mlddragon/activitypulse-demo-template), choose **Use this template → Create a new repository** twice, or use the two repositories your facilitator prepared. Use only the template’s default branch. Name the repos so you can distinguish CI from App, then clone both. Use private repos for training.
- Download [picocolors.patch](lab-assets/picocolors.patch) and [socket-ci.yml](lab-assets/socket-ci.yml). In GitHub’s file view, use **Download raw file**. Keep both files outside the clones until the steps call for them.
- The facilitator grants the learner access to the training organization and repos. They pre-stage the training Socket API token under the Actions secret name `SOCKET_SECURITY_API_KEY` in the **CI repo only** and confirm the learner or facilitator can select the App repo in the Socket GitHub App installation. Use the learner’s training repos and keep credential values off screen.
- Open the [saved CI workflow result](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163), [saved CI success screenshot](images/part-iii/actions-compare-success.png), and [original comparison PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) as fallbacks. If approvals, Actions, or App processing would exceed the activity window, switch to saved evidence and record where the live path stopped.

## 0–3 minutes · Plan the demo

Give a 30-second first take before opening the saved results. Ask Courtney where engineers should get the feedback and whether an existing pipeline needs to carry a required check. Write down the engineer’s first screen, the normal outcome, and one issue you’d be ready to explain for each path.

## 3–10 minutes · Prepare and trigger both versions

In each training clone, start from its default branch. Open a terminal at the repo root. Replace the patch path below with the location of your download.

~~~sh
git switch -c demo/add-picocolors
git apply --check /path/to/picocolors.patch
git apply /path/to/picocolors.patch
git diff --stat
~~~

- **A — GitHub Actions.** Add the workflow starter to this branch as `.github/workflows/socket.yml`. Check the pull-request trigger, checkout, and secret reference. Keep the App out of the CI demo repo. Stage the three changed ActivityPulse files and the workflow, commit, push, and open a PR into the default branch of **this repo**. Find the Actions run for that PR.
- **B — GitHub App.** In the Socket GitHub App installation, select or confirm access for the App demo repo. Keep the Actions starter out of this repo. Stage the same three changed ActivityPulse files, commit, push, and open a PR into the default branch of **this repo**. Find the App’s check and dependency feedback.
- Confirm that both PRs add `picocolors@1.1.1` to the application. Record the PR URLs and the evidence you intend to show. [Socket for GitHub Actions](https://docs.socket.dev/docs/socket-for-github-actions) · [GitHub App repository access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps)

## 10–18 minutes · Verify the engineer’s view

| Demo | Where to start | What to verify |
|---|---|---|
| **A — CI** | Start on the PR checks, then open the Socket job in Actions. Show the CI dependency comment if it posted. | The run evaluated this PR’s change. Identify the completed scan and job result. Explain where an engineer would investigate a failed run. |
| **B — App** | Start on the PR conversation and checks. Open the App’s dependency overview. | The App identifies the added package and version. Explain where an engineer would go to review a finding or get more detail. |

If you use saved evidence, identify who posted each original PR comment. The original experiment intentionally ran both integrations on one PR, which produced duplicate feedback. Its successful Actions job completed via streaming comparison after the preferred diff scan was denied. That run shows a passing job. A claim that a failed check prevents merging requires verified merge settings. [Actions comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7014418426) · [App comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620) · [Socket CI/CD guidance](https://docs.socket.dev/docs/sca-ci)

## 18–25 minutes · Rehearse the recommendation

Arrange the PRs, check, run, and backup evidence in demo order. Show the same change in both paths. Explain where the engineer sees the outcome, what they do next, and who owns setup and troubleshooting.

Prepare for Courtney to ask whether engineers need both. Recommend the App when the priority is feedback inside existing GitHub review. Explain the CI option when the team needs an explicit workflow step or pipeline control. Use the original duplicate comments to show the cost of making both paths post routine feedback. [Observed integration tradeoffs](integration-comparison.md)

## 25–30 minutes · Demo to Courtney

Give the two-view demo in three minutes. Take one unannounced customer question, then recommend which option to pilot and state what would change your recommendation. The facilitator scores the performance using the [readiness check](part-iii-readiness-check.md).

### Backup for customer questions

If Courtney asks about a red job, start with the first meaningful error. The saved Actions 401 shows a job that failed before dependency analysis completed. The saved local CLI reports show a different event, where Socket evaluated a finding and applied Block or Warn. The CLI examples illustrate policy behavior in that experiment. They are separate from the outcome of either demo PR. [CI failure capture](images/part-iii/actions-compare-failed.png) · [CLI Block evidence](images/part-iii/cli-policy-block.png) · [CLI Warn evidence](images/part-iii/cli-policy-warn.png)
