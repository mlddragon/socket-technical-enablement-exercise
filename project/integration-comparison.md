# Controlled GitHub App and Actions comparison

**Decision:** Accepted by Mason on 2026-11-18. **Execution:** Planned; not started. This document authorizes no installation, workflow creation or application implementation.

## Rationale and accepted tradeoff

Socket's [Scan from CI/CD](https://docs.socket.dev/docs/sca-ci), checked November 18, recommends choosing either its GitHub App or a CI pipeline for a given GitHub repository because both can produce duplicate PR comments. Mason explicitly accepts that documented risk for a controlled period on this exercise repository. The goal is to compare workflows, outputs and negative impacts, and retain concrete examples for the interview discussion.

This supersedes the earlier suggestion to disable CI before connecting the App. The optional CI exercise remains Part I §1.3; the comparison informs §2.2–2.3. It does not turn CI into a required assignment deliverable or authorize a production pipeline.

## Prerequisites and lift

When implementation is separately authorized, first complete the Node/Python CSV baseline and required local manifest scan. Confirm organization access and minimum token scopes. CI will need a scoped Socket API key stored as a GitHub Actions secret, appropriate GitHub token permissions, the correct checkout/manifests and PR context, and a runner/tool version that can execute the documented scan. Never commit token values.

The [official Actions guide](https://docs.socket.dev/docs/socket-for-github-actions), checked November 18, shows Python 3.12, the `socketsecurity` distribution and `socketcli`; the planned local path uses the Node `socket` CLI. Compare equivalent manifest inputs and scan purpose, while recording that the executables and environments differ. Do not assume identical flags, outputs, authentication or policy behavior. Recheck documentation and versions before executing.

The earlier assistant estimate of 20–40 minutes and proposed 30-minute CI timebox were planning suggestions only. They are neither confirmed elapsed work nor an owner-approved duration commitment. The assignment budgets about five hours overall and says to stop after six and bring notes; track actual participation and preserve required work first.

## Bounded sequence

1. Establish a successful local baseline scan, then attempt the optional Actions scan on the same baseline. Record failures without expanding the scope to a general CI/CD pipeline.
2. Connect the GitHub App and intentionally retain CI PR scanning during the planned YAML/PyYAML dependency PR. Both integrations must evaluate the same PR/head commit during the overlap; a manual scan without PR context alone does not demonstrate concurrent PR reporting.
3. Before the overlap starts, record the selected PR, base/head SHAs, event/configuration and tools. The default bound is that one controlled dependency PR and the evidence needed to compare its results. Any extra comparison attempt needs an explicit reason in the evidence record.
4. Capture outputs separately, then compare them using the matrix below. Record duplicate comments if they occur; absence of duplicates or missing output is also a result, with configuration limitations stated.
5. End the overlap after evidence capture, or earlier if it impedes required work, produces excessive noise, or the assignment time limit is reached. Preserve evidence, then disable or narrow the optional CI PR reporting so the required App path can continue. Record actual closure and the final enabled configuration; do not imply it has happened now.

The control is event-bounded, not a fabricated calendar window. Actual start/end timestamps and elapsed effort remain to be observed during execution. No workflow, secret, App setting or branch protection is changed by this documentation update.

## Evidence matrix

| Dimension | Local CLI reference | GitHub App | GitHub Actions CI |
|---|---|---|---|
| Inputs and identity | Commit, manifests, org/repo context | Same PR, base/head SHAs, installation scope | Same PR/commit, checkout depth, scan target and PR context |
| Setup and authentication | Runtime/CLI version, token scopes | Installation and repository permissions | Runner/runtime/CLI version, secret names and token permissions; no values |
| Trigger and workflow | Manual invocation | Actual App event and feedback sequence | Actual workflow event, run URL and steps |
| Outputs | Sanitized command/output, scan URL and exit code | Comment/check URLs, wording and scan links | Logs, comment/check URLs, scan links and job outcome |
| Findings and policy | Findings, analysis state and configured policy | Findings, analysis state and policy/check result | Findings, analysis state and policy/job result |
| Timing and failure handling | Observed start/end and first diagnostic | Feedback timing, missing/pending checks | Queue/run/feedback timing, missing secrets/permissions/manifests vs policy failure |
| User experience | Manual effort and reproducibility | Review workflow and onboarding | Configuration effort and troubleshooting |

For each conclusion, record expected behavior, actual behavior, an attributable evidence link, limitations and the teaching implication. Match equivalent findings by package/version/alert; two messages about one finding are not two independent vulnerabilities. A failing check alone is not proof that branch protection prevents merging; record enforcement only if separately verified.

## Negative impacts to evaluate

- Duplicate or repeated PR comments and resulting notification/review burden.
- Similar or conflicting wording/check outcomes that make it unclear which result to trust.
- Pending or stale feedback on different commits; record commit context before calling this a disagreement.
- Extra runs, runner time and maintenance/troubleshooting work. Separate overlapping integrations from duplicate push/PR triggers within CI itself.
- Whether the combined experience hides actionable feedback or complicates the recommended onboarding path.

These are evaluation questions. Only duplicate reporting is documented by the cited caveat; none is a firsthand finding yet. Capture counts/timing only when observed. Retain a concise before/after example if available and a recommendation for normal use based on the actual evidence.

## Execution record

| Item | Current value |
|---|---|
| Comparison PR / base / head | Not selected |
| App configuration / CI run | Not configured by this task |
| Overlap start/end | Not started |
| App / CI / local evidence | Pending |
| Duplicate comments and other impacts | Not observed in this task |
| Final normal configuration / closure proof | Pending execution |

Link observations from the [friction log](friction-log.md). Update the [AI-use log](ai-use-and-verification.md) with verification against actual product behavior when the experiment is performed.
