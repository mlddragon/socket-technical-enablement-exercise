# Show Courtney both Socket integration paths

**Widgets Mfg · Late-stage evaluation · Engineering leadership**

## Open with the workflow decision

“Courtney, I’ll use the same dependency change in both views. As we go, tell me where your engineers should get feedback and whether your existing pipeline needs to enforce the decision.”

## Show the same change twice

**A — GitHub Actions.** Open the pull request’s checks and follow the Socket job into Actions. Show where the engineer sees whether the scan completed and where they would investigate a failure. If the CI workflow posts a dependency comment, point to it in the PR.

**B — GitHub App.** Stay in the pull request. Show the App’s dependency overview and check. Point out the package and version, then show where the engineer would go for more context.

## Answer the likely objections

**“Do we need both?”** Choose one primary feedback path for this repo. The App is a practical starting point for teams that want feedback in their existing GitHub review. Use CI when a specific pipeline control or workflow step matters. Running both in our comparison produced two dependency comments on one PR.

**“Would a failed check stop the merge?”** Verify which check is required in the repository’s merge settings. Agree with the security and engineering owners on which findings should warn and which should block.

**“What does my developer do when the job goes red?”** Open the job and find the first meaningful error. A completed scan with an explicit policy action goes to the dependency and security owners. A 401 before analysis goes to the CI owner to check the integration credential. Keep its value out of shared logs.

## Close with a pilot decision

“Given your workflow, I’d pilot one path on one repo. We’ll look for one actionable feedback stream, confirm who owns exceptions, and check whether your normal dependency updates require any extra developer steps.”

[GitHub App feedback](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620) · [GitHub Actions result](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628/job/135696762163)
