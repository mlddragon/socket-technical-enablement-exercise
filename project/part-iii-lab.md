# Prepare a Socket demo for Widgets Mfg

**Audience:** New Socket Solutions Engineers

**Duration:** 30 minutes, including the customer rehearsal

## Your next customer call

You’re the Solutions Engineer supporting Widgets Mfg, which is in the later stages of evaluating Socket. Courtney, a senior manager of engineering, wants to understand what adopting Socket would change for their engineers day to day.

> Take me through an engineer’s pull request. If we put Socket in CI, what will they see? If we use the GitHub App, what will they see? In each case, when would they need to do something, and what would they do next?

Prepare two demos that use the same dependency change. Show where engineers see feedback, what happens on a routine change, and what they do if a result needs attention. Close with a recommendation tied to Widgets Mfg’s workflow.

Widgets Mfg and Courtney are fictional. The ActivityPulse dependency change comes from the original exercise. The template uses fictional activity data. [Original dependency PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)

## Before the clock starts

- From the [ActivityPulse GitHub template](https://github.com/mlddragon/activitypulse-demo-template), choose **Use this template → Create a new repository** twice, or use the two repositories your facilitator prepared. Use only the template’s default branch. Use private repos for training. The commands below use `widgets-ci` and `widgets-app` as example clone names. Clone both under `$HOME/github`, or use your existing clone locations.
- Download [picocolors.patch](lab-assets/picocolors.patch) and [socket-ci.yml](lab-assets/socket-ci.yml). In GitHub’s file view, use **Download raw file**. Save both files in `$HOME/Downloads` with their original names. Keep them outside the clones until the steps call for them.
- The facilitator grants the learner access to the training organization and repos. They pre-stage the training Socket API token under the Actions secret name `SOCKET_SECURITY_API_KEY` in the **CI repo only** and confirm the learner or facilitator can select the App repo in the Socket GitHub App installation. Use the learner’s training repos and keep credential values off screen.
- Open the [saved CI workflow result](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163), [saved CI success screenshot](images/part-iii/actions-compare-success.png), and [original comparison PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) as fallbacks. If approvals, Actions, or App processing would exceed the activity window, switch to saved evidence and record where the live path stopped.

## 0–3 minutes · Plan the demo

Give a 30-second first take before opening the saved results. Ask Courtney where engineers should get the feedback and whether an existing pipeline needs to carry a required check. Write down the engineer’s first screen, the normal outcome, and one issue you’d be ready to explain for each path.

## 3–10 minutes · Prepare and trigger both versions

### Set the paths and apply the patch

Use Bash, zsh, or Git Bash on Windows. Use the same terminal for all the blocks below so the path variables stay set. Make sure Git can commit with your configured name and email and push to both private training repos.

To check the Actions secret and open the PRs from the terminal, use [GitHub CLI](https://cli.github.com/) and run `gh auth status` to confirm you’re signed in to the account that has access to both repos. Run `gh auth login` if you need to sign in. You can also use the GitHub browser steps below.

Set these four paths first. Change the example folder names to match your local clones. If you saved a download somewhere else or your browser renamed it, update that file’s path too.

~~~sh
lab_ci_repo="$HOME/github/widgets-ci"
lab_app_repo="$HOME/github/widgets-app"
lab_patch="$HOME/Downloads/picocolors.patch"
lab_actions_starter="$HOME/Downloads/socket-ci.yml"
~~~

Start with a clean checkout of each repo’s default branch. Apply the same dependency change to both. Run the block once for the CI repo, then change the first line to `lab_repo="$lab_app_repo"` and run it for the App repo. Skip a repo if you’ve already applied the patch there on `demo/add-picocolors`. Expect changes to `prod/cli.js`, `prod/package.json`, and `prod/package-lock.json`.

~~~sh
lab_repo="$lab_ci_repo"
(
  set -e
  git -C "$lab_repo" apply --check "$lab_patch"
  git -C "$lab_repo" switch -c demo/add-picocolors
  git -C "$lab_repo" apply "$lab_patch"
  git -C "$lab_repo" diff --stat
)
~~~

### A · GitHub Actions

Keep the **CI repo** outside the Socket GitHub App’s repository selection. Before opening the CI PR, confirm that the CI repo has the `SOCKET_SECURITY_API_KEY` Actions secret. The block below checks for the secret. If it’s missing and you’re authorized to set it, paste the training token into GitHub CLI’s hidden prompt. If you don’t have the token or permission, ask the facilitator to complete this step. In the browser, check **Settings → Secrets and variables → Actions** in the CI repo. [GitHub CLI secret setup](https://cli.github.com/manual/gh_secret_set)

~~~sh
(
  set -e
  cd "$lab_ci_repo"
  lab_origin=$(git remote get-url origin)
  lab_ci_slug=$(gh repo view "$lab_origin" --json nameWithOwner --jq '.nameWithOwner')
  lab_secret_present=$(gh secret list --repo "$lab_ci_slug" --app actions --json name \
    --jq 'any(.[]; .name == "SOCKET_SECURITY_API_KEY")')
  if [ "$lab_secret_present" = true ]; then
    printf 'Actions secret already configured in %s\n' "$lab_ci_slug"
  else
    printf 'Set the training Actions secret for %s\n' "$lab_ci_slug"
    gh secret set SOCKET_SECURITY_API_KEY --repo "$lab_ci_slug" --app actions
  fi
)
~~~

The downloaded starter already defines the `pull_request` trigger, an `actions/checkout` step, and the secret reference. Copy the starter into the CI clone and stage it with the three changed app files. If you’ve already committed and pushed the starter and app changes, skip this block. [Socket for GitHub Actions](https://docs.socket.dev/docs/socket-for-github-actions)

~~~sh
(
  set -e
  cd "$lab_ci_repo"
  test "$(git branch --show-current)" = demo/add-picocolors
  mkdir -p .github/workflows
  cp "$lab_actions_starter" .github/workflows/socket.yml
  git add prod/cli.js prod/package.json prod/package-lock.json .github/workflows/socket.yml
  git diff --cached --name-only
  git commit -m "Demo dependency change with Socket Actions"
  git push -u origin demo/add-picocolors
)
~~~

### B · Socket GitHub App

Open the installed Apps list in GitHub. For a personal repo, use **Settings → Applications → Installed GitHub Apps**. For an organization repo, use the organization’s **Settings → Third-party Access → GitHub Apps**. Choose **Configure** next to Socket and confirm that **Only select repositories** includes the **App repo** and excludes the CI repo. If you’re authorized to add the App repo, keep the other authorized repositories selected and save. Ask the facilitator if the installation uses **All repositories** or you can’t manage its settings. [GitHub App repository access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#modifying-repository-access)

This clone gets just the three changed app files. Skip the block if you’ve already committed and pushed them.

~~~sh
(
  set -e
  cd "$lab_app_repo"
  test "$(git branch --show-current)" = demo/add-picocolors
  git add prod/cli.js prod/package.json prod/package-lock.json
  git diff --cached --name-only
  git commit -m "Demo dependency change with the Socket GitHub App"
  git push -u origin demo/add-picocolors
)
~~~

### Open one PR in each training repo

After you’ve checked the CI secret and App access and pushed both branches, run this block. It finds each clone’s GitHub repo and default branch, then prints the URL of its open PR or creates one. [GitHub CLI pull request creation](https://cli.github.com/manual/gh_pr_create)

~~~sh
(
  set -e
  lab_head=demo/add-picocolors
  for lab_repo in "$lab_ci_repo" "$lab_app_repo"; do
    cd "$lab_repo"
    lab_origin=$(git remote get-url origin)
    lab_slug=$(gh repo view "$lab_origin" --json nameWithOwner --jq '.nameWithOwner')
    lab_base=$(gh repo view "$lab_origin" --json defaultBranchRef --jq '.defaultBranchRef.name')
    lab_pr=$(gh pr list --repo "$lab_slug" --base "$lab_base" --head "$lab_head" \
      --state open --limit 1 --json url --jq '.[0].url // empty')
    printf '%s\n' "$lab_slug"
    if [ -n "$lab_pr" ]; then
      printf '%s\n' "$lab_pr"
    else
      gh pr create --repo "$lab_slug" --base "$lab_base" --head "$lab_head" \
        --title 'Demo dependency change with picocolors' \
        --body 'Add picocolors to ActivityPulse for the Widgets Mfg Socket demo.'
    fi
  done
)
~~~

In the browser, you can instead open a PR **in each repo** with that repo’s default branch as the **base** and `demo/add-picocolors` as the **compare** branch. Confirm that both PRs add `picocolors@1.1.1` and record their URLs. On the CI PR, follow the check into the **Socket Security CI** Actions run. On the App PR, look for the **Socket Security** check and dependency feedback in the PR. If either path stalls, switch to saved evidence and note what didn’t run.

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
