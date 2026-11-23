# Firsthand friction log

Firsthand observations during the Socket Technical Enablement interview exercise. Public complaints and untested hypotheses belong in [research/community-signals.md](../research/community-signals.md). Entries below distinguish observed behavior from unverified explanations.

## Entry 001 — Enterprise invitation / first-login ambiguity

- **Status** — Access was pending on November 16, 2026. Mason later confirmed it was working.
- **Expected** — The exercise instructions say Socket provisions an Enterprise organization and sends an invitation. The candidate accepts it with the email associated with their GitHub account, without creating a separate organization or entering payment details.
- **Observed** — After the candidate provided their GitHub identity and demo repository, the recruiter said an invitation should be present and the account upgraded. The candidate found no invitation in Inbox, archived mail, Spam, or Trash. GitHub sign-in succeeded, then opened a setup screen asking for profile and organization details. The candidate asked the recruiter whether to complete setup or join an existing organization and stopped before creating one.
- **Impact** — The prompt made it hard to start the exercise confidently and created a risk of setting up or configuring the wrong organization. The exercise instructions and public Users and Permissions documentation describe invitations. Neither explained how to interpret this first-login screen.
- **Evidence** — Firsthand login observation and recruiting correspondence. No screenshot was captured. Exact field labels, browser and OS versions, organization name, and provisioning or entitlement state were unverified at that point. The cause of the prompt and whether profile setup was required were unknown.
- **Documentation improvement** — Add a first-login walkthrough with screenshots for invited users and new organization creators. Show which fields to complete, how to confirm organization membership and Enterprise entitlements, and what to do if the invitation email is missing.
- **Teaching use** — Before a first CLI or Firewall exercise, have the learner verify their GitHub identity, organization membership, Enterprise plan, and repository integration.

### Follow-up recorded 2026-11-18

Mason confirmed on November 18 that organization access had worked the night of November 16. The private work-item record captures the report to Grok. This closed the access question. Scan execution, token scopes, and Enterprise capabilities were outside that confirmation.

## Entry 002 — Concurrent integration reporting

- **Status** — Verified November 19. The GitHub App and Actions each left a dependency-review comment on PR #1. [Comparison outcome](integration-comparison.md#verified-execution-outcome-and-closure--2026-11-19)
- **Source** — Socket’s guidance, checked November 18, advises choosing either the GitHub App or a pipeline on a GitHub repository to avoid two sets of comments. [Socket Scan from CI/CD](https://docs.socket.dev/docs/sca-ci)
- **Decision** — Mason accepted this risk for a controlled concurrent GitHub App and Actions comparison. This superseded the earlier suggestion to disable CI before installing the App.
- **Expected evidence** — Separate App and Actions outputs for the same PR and head commit, examples of duplicate comments if observed, notification and review burden, timing, check behavior, and how the overlap ended. [Comparison protocol](integration-comparison.md)
- **Observed** — Both integrations reported during the controlled overlap. The GitHub App remained the routine PR path, and the feature branch switched Actions to manual dispatch.
- **Documentation improvement** — Add a comparison note explaining how to attribute App and CI feedback and return to one routine PR-reporting path after an evaluation.

## Entry 003 — API token rotation documentation typo (verified 2026-11-18)

- **Status** — Verified in the public documentation during interview preparation. The proposed correction has yet to be submitted to Socket.
- **Observed** — The Rotation section says, “API Tokens can be shown to disabled and forcibly rotated in the case of incidents requiring action.” The malformed wording may be a leftover from the preceding Visibility section. [Socket API Tokens](https://docs.socket.dev/docs/api-keys)
- **Impact** — During incident response, users need to know which actions they can take on a credential. The documented `api-tokens:revoke` and `api-tokens:rotate` scopes support the proposed wording. The actual UI action labels still need checking.
- **Documentation improvement** — Change the sentence to “API Tokens can be revoked and forcibly rotated in the case of incidents requiring action.”
- **Teaching use** — Pair this concrete wording fix with a larger onboarding or troubleshooting recommendation when discussing Part I §5.

## Entry 004 — CLI token scopes dispersed across command references (firsthand, 2026-11-18)

- **Status** — Firsthand documentation friction recorded. Token creation and scan results were verified later. The proposed docs change has yet to be submitted to Socket. [Part I briefing](part-i-briefing.md)
- **Context** — Part I §1.1 called for a least-privilege token to create, inspect, and policy-evaluate scans. Mason used Socket CLI v1.15.0, `socket scan --help`, `socket scan create --help`, and the public references. [Socket scan docs](https://docs.socket.dev/docs/socket-scan) · [Socket API token docs](https://docs.socket.dev/docs/api-keys)
- **Observed** — The needed scopes are documented across command references and a prose Report subsection. Mason had to assemble the combined scope set under time pressure. The friction was finding the workflow across those sections. The setup produced no authorization failure.
- **Verified scopes** — The scan docs and CLI help established these requirements. Mason’s pasted `socket scan create --help` confirmed `full-scans:create`. [Socket scan docs](https://docs.socket.dev/docs/socket-scan)
  - `socket scan create` requires `full-scans:create`.
  - `socket scan list`, `view`, `metadata`, and `diff` require `full-scans:list`.
  - `socket scan report` requires `full-scans:list` and `security-policy:read`.
  - `socket scan create --report` uses all three scopes.
- **Documentation improvement** — Add a workflow-based scope worksheet for first scans, policy evaluation, read-only triage, CI automation, and scan administration. List the goal, commands, required and optional scopes, verification steps, and common failures for each workflow. Link to the command references.
- **Teaching use** — Have new SEs, TAMs, and Support Engineers use the checklist to choose the minimum scopes before creating a token. [Socket CLI Permissions Explorer](https://docs.google.com/spreadsheets/d/1iQLzZkCqyz8XxqFjk2UQPY5TDkvVa1a49uHQ3eLOBPY/edit?usp=sharing) · [Original design brief](../research/planning/cli-permissions-worksheet-handoff.md)

## Entry 005 — Package-score explainability and human-centered documentation (firsthand, 2026-11-19)

- **Status** — Firsthand navigation and Mason’s assessment recorded. The cause of the individual scores and the documentation’s authoring process remain unknown. Feedback has yet to be submitted to Socket.
- **Observed** — For `npm/picocolors@1.1.1`, the GitHub App reported Supply Chain Security **100**, Vulnerability **100**, Quality **72**, Maintenance **80**, and License **100**. The full dependency-diff report showed the scores alongside maintainer, license, size, and direct/production classification. The package overview and docs gave no package-specific explanation for the Quality and Maintenance scores in the views Mason inspected. [PR #1 comment](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620) · [Package overview](https://socket.dev/npm/package/picocolors/overview/1.1.1) · [Package Scores documentation](https://docs.socket.dev/docs/package-scores)
- **Impact** — Developers and security reviewers could see the scores but had little evidence to decide whether a lower score called for investigation or remediation. Mason found that the documentation presented technical values before the context needed to make that decision.
- **Documentation improvement** — For each category score, show the contributing factors, link to the package-specific evidence, and explain what a developer or analyst can do next. A short annotated PR example could show how to make the decision.

## Entry 006 — Firewall registry-mode preflight and troubleshooting (2026-11-22)

- **Status** — Core demo verified. [Part II results](part-ii-firewall-results.md)
- **Context** — Apple Silicon Mac, Colima, Docker Engine 29.5.2 server, Compose 5.8.0, Firewall 2.23.0, and npm 11.19.0.
- **Observed** — Initial restricted agent checks suggested several prerequisites were unavailable. Direct host checks confirmed Colima and network access. A user-level bind to port 443 was denied, so the demo used loopback port 8443. Scoped TLS verification succeeded, and npm’s rewritten tarball URL preserved that port.
- **Observed policy result** — The fixture’s metadata returned HTTP 200. Its tarball returned HTTP 403 with a Socket request ID and `Known malware`. npm’s original error matched its Firewall event by request ID.
- **Troubleshooting** — An AI-suggested zsh loop used `path` as a variable. That replaced the shell’s command search path, so `curl` and `grep` were unavailable in that session. A fresh login shell and the variable name `request_path` restored the check.
- **Documentation improvement** — Put a verification sequence beside the registry setup instructions. Check health, confirm the organization in startup logs, inspect the rewritten tarball URL, and match the npm block to the Firewall decision. Show the metadata 200 and artifact 403 side by side. Use separate request IDs for independent requests.

When adding a technical entry, capture product and CLI versions, OS, relevant errors, first steps tried, and resolution where applicable. Keep tokens, private correspondence, and confidential data out of the log.
