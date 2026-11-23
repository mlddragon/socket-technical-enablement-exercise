# Package scores

*How to read a score and decide what to review*

**Draft v0.1 | Single-pass AI rewrite | Human review and approval pending**

November 19, 2026. Editorial direction by Mason Dillon. Drafted by ChatGPT.

[Google Doc review copy](https://docs.google.com/document/d/1bm8TfSpiRpJJDsCublt_rcPcJtmmN5wza23yOrIHb8Q/edit)

Socket scores package versions from 0 to 100 across five categories: supply chain risk, quality, maintenance, vulnerabilities, and license. Higher scores reflect more favorable signals in that category. In [Package Search](https://docs.socket.dev/docs/package-search), open a package and select Versions to compare releases. Open Alerts, Dependencies, or License to see the details that matter to your decision.

## Why scores exist

A dependency review can take you through a changelog, an advisory database, and a license file before you know where to start. Package scores give you a quick way to spot what deserves a closer look. If the license score catches your eye, open the license details. If the vulnerability score dropped in the version you’re considering, start with the advisory.

## Read a score in your daily work

### Start with the version you’ll actually use

Open Package Search, choose the ecosystem, and find the package. In Versions, locate the exact release you plan to add or the version recorded in your lockfile. When comparing an upgrade, review the current and proposed versions side by side.

### Follow the category to the evidence

- **Supply chain risk.** Check Alerts for the specific signal. An unexpected install script or an ownership change can call for a closer look at the release.
- **Quality.** Review the underlying signals, such as documentation or package size. A lower score can help you decide where to inspect the package more closely.
- **Maintenance.** Check the release history and maintainers. Look for signs that the project will get fixes when you need them.
- **Vulnerabilities.** Open the advisory and check whether it affects your version. If it comes from a dependency, find what brings that dependency in.
- **License.** Check the detected license and compare it with what your organization allows for your intended use.

**Example.** You plan to upgrade a package from 2.3.0 to 2.4.0. The vulnerability score drops while maintenance looks about the same. Check the advisory and dependency path for 2.4.0. If there’s an unaffected release, review that version before updating. If the finding is unclear, share the version and alert with your security team.

Treat a lower score as a reason to investigate. A high score can still appear alongside a finding your team needs to address. Use the [alert details](https://docs.socket.dev/docs/what-to-do-with-socket-alerts) and your team’s review process to decide what happens next.

## Review scores as an administrator

### Use the score for triage and policy for enforcement

A package score summarizes signals about a version. Your organization’s policy determines how Socket handles a finding in your workflow. In the dashboard, check the [policy that applies to the repository](https://docs.socket.dev/docs/sca-enforce) and the action assigned to that alert type. A Warn action calls for review. A Block action fails the Socket pull request check. On GitHub, requiring that check is what stops a merge.

For a one-off finding your team has reviewed and accepted, record the reason and use a [narrowly scoped resolution](https://docs.socket.dev/docs/alert-resolutions) where your policy setup supports it. If your team consistently treats a whole class of alerts differently, review the rule and its scope. For example, a license decision should follow the detected license and your organization’s [license policy](https://docs.socket.dev/docs/sca-license-policy).

### Set up a repeatable review

When you ask a developer to investigate, include the package version, the category that prompted review, the alert or license evidence, and the affected repository. If a score moved after an upgrade, compare the alerts and dependency paths before changing policy. Use those findings to decide whether the team needs an upgrade, a scoped exception, or a broader policy review.

## Explain score differences in the field

### Check what each result includes

A shallow score covers the package itself. A deep score includes the dependency tree. The [CLI’s](https://docs.socket.dev/docs/socket-package) `socket package score` report presents both views, while `socket package shallow` returns package-only results. If a package looks healthy by itself but the deep score is lower, start with the top alerts and the dependency named in the deep report.

For a support case, record the ecosystem, package, exact version, score category, shallow or deep view, and where and when you observed it. Include the alert identifier and dependency path when available. Compare like-for-like results before attributing a difference to a scoring change.

### What can move a score

Socket’s published methodology combines category-specific signals with alerts. More severe alerts can pull a category down more sharply. Release activity, dependency counts, and other package characteristics can also affect results. Two packages with the same alert count can score differently, and the score alone can’t tell you which finding drove the difference.

The [published scoring methodology](https://docs.socket.dev/docs/package-scores) describes the weighting and limits for readers who need them. Socket notes that the deployed model can change. For a customer investigation, use the observed score and underlying findings as your evidence.
