# Prepare a Socket demo for Widgets Mfg

**Audience:** New Socket Solutions Engineers

**Duration:** 30 minutes, including the customer rehearsal

## Your next customer call

You’re the Solutions Engineer supporting Widgets Mfg, which is in the later stages of evaluating Socket. Courtney, a senior manager of engineering, wants to understand what adopting Socket would change for their engineers day to day.

> Take me through an engineer’s pull request. If we put Socket in CI, what will they see? If we use the GitHub App, what will they see? In each case, when would they need to do something, and what would they do next?

Prepare two demos that use the same dependency change. Show where engineers see feedback, what happens on a routine change, and what they do if a result needs attention. Close with a recommendation tied to Widgets Mfg’s workflow.

Widgets Mfg and Courtney are fictional. The ActivityPulse dependency change comes from the original exercise. The template uses fictional activity data. [Original dependency PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1)

## Before the clock starts

- From the [ActivityPulse GitHub template](https://github.com/mlddragon/activitypulse-demo-template), choose **Use this template → Create a new repository** twice, or use the two private repos your facilitator prepared. Use only the template’s default branch. Name the **GitHub Actions** repo `widgets-ci` and the **Socket GitHub App** repo `widgets-app`. Clone them as `$HOME/github/widgets-ci` and `$HOME/github/widgets-app` so you can paste the lab commands as written. If you use other clone paths, change the first two path variables in the setup block.
- Download [picocolors.patch](lab-assets/picocolors.patch) and [socket-ci.yml](lab-assets/socket-ci.yml). In GitHub’s file view, use **Download raw file**. Save both files in `$HOME/Downloads` with their original names. Keep them outside the clones until the steps call for them.
- The facilitator grants the learner access to the training organization and repos and pre-stages the training Socket API token as `SOCKET_SECURITY_API_KEY` in the **CI repo only**. Keep credential values off screen.
- Before starting the timer, complete the [GitHub App access setup](#b--socket-github-app) for the **App repo**. The steps cover a first-time installation and an existing installation. If the learner lacks permission to install or configure the App, the facilitator or GitHub account owner completes this step.
- Open the [saved CI workflow result](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163), [saved CI success screenshot](images/part-iii/actions-compare-success.png), and [original comparison PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1) as fallbacks. If approvals, Actions, or App processing would exceed the activity window, switch to saved evidence and record where the live path stopped.

## 0–3 minutes · Plan the demo

Give a 30-second first take before opening the saved results. Ask Courtney where engineers should get the feedback and whether an existing pipeline needs to carry a required check. Write down the engineer’s first screen, the normal outcome, and one issue you’d be ready to explain for each path.

## 3–10 minutes · Prepare and trigger both versions

Run these steps in order. This section is complete when you have two PR URLs.

1. [Set the paths and apply the patch](#set-the-paths-and-apply-the-patch) to both clones.
2. [Prepare and push the GitHub Actions branch](#a--github-actions). If the facilitator already added the secret, start with the workflow copy, commit, and push block.
3. [Confirm App access, then commit and push the App branch](#b--socket-github-app).
4. [Open one PR in each training repo](#open-one-pr-in-each-training-repo).

### Set the paths and apply the patch

Use Bash, zsh, or Git Bash on Windows. Use the same terminal for all the blocks below so the path variables stay set. Make sure Git can commit with your configured name and email and push to both private training repos.

To check the Actions secret and open the PRs from the terminal, use [GitHub CLI](https://cli.github.com/) and run `gh auth status` to confirm you’re signed in to the account that has access to both repos. Run `gh auth login` if you need to sign in. You can also use the GitHub browser steps below.

Set these four paths first. Change the example folder names to match your local clones. If you saved a download somewhere else or your browser renamed it, update that file’s path too. If you open a new terminal or tab, run this path block again before resuming. If both demo branches are already pushed, continue with the CI secret and App access checks, then open the PRs.

~~~sh
lab_ci_repo="$HOME/github/widgets-ci"
lab_app_repo="$HOME/github/widgets-app"
lab_patch="$HOME/Downloads/picocolors.patch"
lab_actions_starter="$HOME/Downloads/socket-ci.yml"
~~~

Start with a clean checkout of each repo’s default branch. Run this block once to apply the same dependency change to both clones. If you’re resuming on `demo/add-picocolors` and the patch is already present in either clone, the block picks up where you left off. Expect changes to `prod/cli.js`, `prod/package.json`, and `prod/package-lock.json` in each clone.

~~~sh
(
  set -e
  : "${lab_ci_repo:?Set lab_ci_repo using the path block above.}"
  : "${lab_app_repo:?Set lab_app_repo using the path block above.}"
  : "${lab_patch:?Set lab_patch using the path block above.}"
  for lab_repo in "$lab_ci_repo" "$lab_app_repo"; do
    printf '\n%s\n' "$lab_repo"
    lab_branch=$(git -C "$lab_repo" branch --show-current)
    if [ "$lab_branch" = demo/add-picocolors ] &&
      git -C "$lab_repo" apply --reverse --check "$lab_patch" 2>/dev/null; then
      printf 'Patch already applied.\n'
    else
      git -C "$lab_repo" apply --check "$lab_patch"
      if [ "$lab_branch" != demo/add-picocolors ]; then
        git -C "$lab_repo" switch -c demo/add-picocolors
      fi
      git -C "$lab_repo" apply "$lab_patch"
    fi
    git -C "$lab_repo" diff --stat
  done
  printf '\nBoth clones are patched. Next: A · GitHub Actions.\n'
)
~~~

### A · GitHub Actions

Keep the **CI repo** outside the Socket GitHub App’s repository selection. Before opening the CI PR, confirm that the CI repo has the `SOCKET_SECURITY_API_KEY` Actions secret. The block below checks for the secret. If it’s missing and you’re authorized to set it, paste the training token into GitHub CLI’s hidden prompt. If you don’t have the token or permission, ask the facilitator to complete this step. In the browser, check **Settings → Secrets and variables → Actions** in the CI repo. [GitHub CLI secret setup](https://cli.github.com/manual/gh_secret_set)

~~~sh
(
  set -e
  : "${lab_ci_repo:?Set lab_ci_repo using the path block above.}"
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
  : "${lab_ci_repo:?Set lab_ci_repo using the path block above.}"
  : "${lab_actions_starter:?Set lab_actions_starter using the path block above.}"
  if [ ! -f "$lab_actions_starter" ]; then
    printf 'Workflow starter not found at %s\n' "$lab_actions_starter" >&2
    exit 1
  fi
  cd "$lab_ci_repo"
  test "$(git branch --show-current)" = demo/add-picocolors
  mkdir -p .github/workflows
  cp "$lab_actions_starter" .github/workflows/socket.yml
  git add prod/cli.js prod/package.json prod/package-lock.json .github/workflows/socket.yml
  git diff --cached --name-only
  git commit -m "Demo dependency change with Socket Actions"
  git push -u origin demo/add-picocolors
  printf '\nCI branch pushed. Next: B · Socket GitHub App.\n'
)
~~~

### B · Socket GitHub App

The App needs access to the **App repo** before you open its PR. Complete the installation or access change before the timer, then verify the selection here.

- **First-time installation.** If the facilitator provided a Socket training organization, start from that organization’s **Settings → Integrations → Connected Apps → GitHub** in the [Socket dashboard](https://socket.dev/dashboard). Otherwise, open the [Socket Security GitHub App](https://github.com/apps/socket-security) and click **Install**. In GitHub, choose the account or organization that owns the App repo. Under **Only select repositories**, select the **App repo**, then approve the installation. [Socket App installation guide](https://docs.socket.dev/docs/socket-for-github-installation)
- **Existing installation.** For a personal repo, open the owner account’s [Installed GitHub Apps](https://github.com/settings/installations). For an organization repo, open the organization’s **Settings → Third-party Access → GitHub Apps**. Find **Socket Security**, choose **Configure**, and add the **App repo** under **Only select repositories**. Keep the other authorized repositories selected and save. [GitHub App access guide](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#modifying-repository-access)

Verify that Socket has access to the **App repo** and that the **CI repo** is excluded. If approval is pending or your existing installation covers **All repositories**, ask the facilitator for an isolated training setup or use the saved App evidence.

This clone gets just the three changed app files. Skip the block if you’ve already committed and pushed them.

~~~sh
(
  set -e
  : "${lab_app_repo:?Set lab_app_repo using the path block above.}"
  cd "$lab_app_repo"
  test "$(git branch --show-current)" = demo/add-picocolors
  git add prod/cli.js prod/package.json prod/package-lock.json
  git diff --cached --name-only
  git commit -m "Demo dependency change with the Socket GitHub App"
  git push -u origin demo/add-picocolors
  printf '\nApp branch pushed. Next: Open one PR in each training repo.\n'
)
~~~

### Open one PR in each training repo

After you’ve checked the CI secret and App access and pushed both branches, run this block. It finds each clone’s GitHub repo and default branch, then prints the URL of its open PR or creates one. [GitHub CLI pull request creation](https://cli.github.com/manual/gh_pr_create)

~~~sh
(
  set -e
  : "${lab_ci_repo:?Set lab_ci_repo using the path block above.}"
  : "${lab_app_repo:?Set lab_app_repo using the path block above.}"
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
  printf '\nBoth PRs are open. Next: 10–18 minutes · Verify the engineer’s view.\n'
)
~~~

In the browser, you can instead open a PR **in each repo** with that repo’s default branch as the **base** and `demo/add-picocolors` as the **compare** branch. Confirm that both PRs add `picocolors@1.1.1` and record their URLs. On the CI PR, follow the check into the **Socket Security CI** Actions run. On the App PR, look for the **Socket Security** check and dependency feedback in the PR. If either path stalls, switch to saved evidence and note what didn’t run.

## 10–18 minutes · Verify the engineer’s view

| Demo | Where to start | What to verify |
|---|---|---|
| **A — CI** | Start on the PR checks, then open the Socket job in Actions. Show the CI dependency comment if it posted. | The run evaluated this PR’s change. Identify the completed scan and job result. Explain where an engineer would investigate a failed run. |
| **B — App** | Start on the PR conversation and checks. Open the App’s dependency overview. | The App identifies the added package and version. Explain where an engineer would go to review a finding or get more detail. |

If you use saved evidence, identify who posted each original PR comment. The original experiment intentionally ran both integrations on one PR, which produced duplicate feedback. A claim that a failed check prevents merging requires verified merge settings. [Actions comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7014418426) · [App comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620) · [Socket CI/CD guidance](https://docs.socket.dev/docs/sca-ci)

## 18–25 minutes · Rehearse the recommendation

Arrange the PRs, check, run, and backup evidence in demo order. Show the same change in both paths. Explain where the engineer sees the outcome, what they do next, and who owns setup and troubleshooting.

Prepare for Courtney to ask whether engineers need both. Recommend the App when the priority is feedback inside existing GitHub review. Explain the CI option when the team needs an explicit workflow step or pipeline control. Use the original duplicate comments to show the cost of making both paths post routine feedback. [Observed integration tradeoffs](integration-comparison.md)

## 25–30 minutes · Demo to Courtney

Give the two-view demo in three minutes. Take one unannounced customer question, then recommend which option to pilot and state what would change your recommendation. The facilitator scores the performance using the [readiness check](part-iii-readiness-check.md).

### Backup for customer questions

If Courtney asks about a red job, start with the first meaningful error. The saved Actions 401 shows a job that failed before dependency analysis completed. The saved local CLI reports show a different event, where Socket evaluated a finding and applied Block or Warn. The CLI examples illustrate policy behavior in that experiment. They are separate from the outcome of either demo PR. [CI failure capture](images/part-iii/actions-compare-failed.png) · [CLI Block evidence](images/part-iii/cli-policy-block.png) · [CLI Warn evidence](images/part-iii/cli-policy-warn.png)

### Optional challenge · Explain an error in a passing job

Use this as Courtney’s customer question during the demo. In **Socket Security CI → socket-security → Run Socket Security Scan**, search the job log for `APIAccessDenied`. If your run doesn’t show it, use the [saved successful job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163) or check lines 32–33 in its [log capture](images/part-iii/actions-compare-success.png).

> Did you see the permission error? What operation was denied, how did Socket continue, and what evidence tells you whether the job passed?

<details>
<summary>Reveal the challenge answer key</summary>

- Socket attempted the native diff-scan comparison and received `APIAccessDenied(Insufficient permissions)`. That message identifies the denied operation. The log alone doesn’t identify a specific missing token scope.
- The next line shows `requested=diff-scan effective=streaming`. Socket completed the comparison using streaming, reported `No issues found`, and GitHub marked the job successful.
- In the saved HTTP 401 example, authentication failed before dependency analysis completed and the job failed. Check both the scan output and the final job result before deciding what action to take.

</details>
