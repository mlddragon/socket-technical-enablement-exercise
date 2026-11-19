# Part III — Teach It Back: Selected Topic & Package Index

**Selected November 19, 2026:** **Diagnosing a Socket security-policy block versus an authentication/tooling failure.** Selected because both behaviors were observed directly in Part I; this package does **not depend on completing Part II Firewall**.

## Three deliverables

1. **[Hands-on lab — 25 minutes](part-iii-lab.md):** Learner compares a policy Block, a Warn, and a GitHub Actions 401, using authentic saved scan IDs and CI logs (with screenshots and sanitized log excerpts for learners without org access). No org-wide policy changes or malicious package execution.
2. **[Customer talk track draft](part-iii-talk-track.md):** Practical response framework, objection handling, and safe evidence to request.
3. **[Practical readiness check draft](part-iii-readiness-check.md):** Observable scenario-based competence criteria, explicit not-ready conditions, and targeted remediation.

**Evidence basis:** [Part I briefing](part-i-briefing.md), [Part I walkthrough](part-i-walkthrough.md), and [Actions run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).

## Status and final checks

- **Lab:** Complete for this milestone after Mason's walkthrough. The screenshots and excerpts let learners work without access to the original Socket organization.
- **Remaining drafts:** Finalize the talk track and verify its one-page layout. Finalize the readiness check and verify the assessment timing.
- **Submission:** The formal package is still pending. See [current project status](PROJECT-STATUS.md) for the confirmed panel date and working submission target.
- **Firewall:** Part II remains unattempted. The lab runs independently of that work.

**Teaching intent:** Make the diagnostic decision concrete: did the scan evaluate a package and enforce an alert policy, or did the scanner fail to authenticate/initialize? Never infer malware from a red CI result alone. Pair any conclusion with observable evidence and a safe next action.

Original candidate notes and research IDs were incorporated into the above deliverables; this page supersedes the earlier planning-only outline.
