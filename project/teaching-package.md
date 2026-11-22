# Part III — Teach It Back: Selected Topic & Package Index

**Topic** · Diagnosing a Socket security-policy block versus an authentication or tooling failure. Both behaviors were observed directly in Part I.

## Three deliverables

1. **[Hands-on lab — 25 minutes](part-iii-lab.md):** Learner compares a policy Block, a Warn, and a GitHub Actions 401, using authentic saved scan IDs and CI logs (with screenshots and sanitized log excerpts for learners without org access). No org-wide policy changes or malicious package execution.
2. **[One-page customer talk track](part-iii-talk-track.pdf)** ([text version](part-iii-talk-track.md)). Explain the result, handle customer objections, and collect the evidence needed to route the issue.
3. **[Practical readiness check](part-iii-readiness-check.md).** Five-minute scenario exercise with observable criteria, explicit not-ready conditions, and targeted remediation.

**Evidence basis:** [Part I briefing](part-i-briefing.md), [Part I walkthrough](part-i-walkthrough.md), and [Actions run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).

## Status and final checks

- **Lab:** Complete for this milestone after Mason's walkthrough. The screenshots and excerpts let learners work without access to the original Socket organization.
- **Talk track:** The PDF was checked for one-page layout and readable text. **Readiness check:** The facilitator sequence and rubric are ready to run. The five-minute target still needs a timed learner trial.
- **Submission:** The formal package is still pending. See [current project status](PROJECT-STATUS.md) for the confirmed panel date and working submission target.
- **Firewall:** [Part II results](part-ii-firewall-results.md) provide an optional panel example of install-time enforcement. The three teaching materials use the Part I cases.

**Teaching intent:** Make the diagnostic decision concrete: did the scan evaluate a package and enforce an alert policy, or did the scanner fail to authenticate/initialize? Never infer malware from a red CI result alone. Pair any conclusion with observable evidence and a safe next action.

Original candidate notes and research IDs were incorporated into the above deliverables; this page supersedes the earlier planning-only outline.
