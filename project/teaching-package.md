# Part III — Teach It Back: Selected Topic & Package Index

**Selected November 19, 2026:** **Diagnosing a Socket security-policy block versus an authentication/tooling failure.** Selected because both behaviors were observed directly in Part I; this package does **not depend on completing Part II Firewall**.

## Three deliverables

1. **[Hands-on lab — 25 minutes](part-iii-lab.md):** Learner compares a policy Block, a Warn, and a GitHub Actions 401, using authentic saved scan IDs and CI logs (or sanitized case cards when org access is unavailable). No org-wide policy changes or malicious package execution.
2. **[One-page customer talk track](part-iii-talk-track.md):** Practical response framework, objection handling, and safe evidence to request.
3. **[Practical readiness check](part-iii-readiness-check.md):** Observable scenario-based competence criteria, explicit not-ready conditions, and targeted remediation.

**Evidence basis:** [Part I briefing](part-i-briefing.md), [Part I walkthrough](part-i-walkthrough.md), and [Actions run #44557864628](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).

## Status and final checks

- **Drafted and saved:** All three complete initial drafts, based on actual scan and runner evidence.
- **Needs learner/instructor review:** Confirm target learner's read access to saved scan IDs; otherwise use provided sanitized case cards. Verify actual spoken time for talk track and that it fits on one page in chosen export layout.
- **Needs dry run:** Time the lab, test historical `socket scan report` commands under read-only scopes, and make sure the readiness assessment is deliverable without an active Socket organization.
- **Submission:** Part III is the package for advance submission. The original deadline was November 19 at 1:30 p.m. Eastern; user requested an extension to Monday, but acknowledgment should be checked before asserting it was granted. These repository drafts have **not been emailed or submitted**.
- **Scope note:** Part II may not be completed. Nothing in this topic requires a Firewall proxy.

**Teaching intent:** Make the diagnostic decision concrete: did the scan evaluate a package and enforce an alert policy, or did the scanner fail to authenticate/initialize? Never infer malware from a red CI result alone. Pair any conclusion with observable evidence and a safe next action.

Original candidate notes and research IDs were incorporated into the above deliverables; this page supersedes the earlier planning-only outline.
