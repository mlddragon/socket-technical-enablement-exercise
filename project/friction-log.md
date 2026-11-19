# Firsthand friction log

Firsthand observations during the Socket Technical Enablement interview exercise. Public complaints and untested hypotheses belong in [research/community-signals.md](../research/community-signals.md). Entries below distinguish observed behavior from unverified explanations.

| Date | Task / environment | Expected | Actual | Where docs helped or failed | Evidence (safe to publish) | Proposed documentation or onboarding improvement |
|---|---|---|---|---|---|---|
| 2026-11-16 | First-time Socket Enterprise access via GitHub SSO (web interface; browser/OS/version not captured) | Per the provided exercise instructions, Socket provisions an Enterprise organization and sends an invitation; candidate accepts it using the email associated with their GitHub account, without creating a separate Socket organization or entering payment details | Candidate found no invitation in Inbox, archived mail, Spam, or Trash. GitHub sign-in succeeded, but the resulting setup screen asked for profile and organization information. Candidate stopped before creating an organization. Recruiter reported access should already have been upgraded; candidate replied asking whether to complete setup or join an existing organization. **Resolution pending.** | Exercise instructions describe joining a provisioned Enterprise organization but do not address the first-login profile/organization prompt or how to distinguish an invitation-based flow from new-organization creation. Public Users and Permissions documentation describes organization invitations but did not settle this specific first-login screen. | Firsthand login observation and interview email correspondence, summarized without reproducing private messages. No screenshot captured; exact field labels and backend provisioning state unverified. | Add a first-login walkthrough with screenshots and an explicit decision point: invited user vs. new organization creator. Explain what fields are safe to complete, how to confirm organization membership/Enterprise entitlements, and what to do if the invitation email does not arrive. |

## Entry 001 — Enterprise invitation / first-login ambiguity

- **Status:** Open; awaiting confirmation from recruiter/Socket, as of November 16, 2026.
- **Impact:** Blocks confident start of the hands-on exercise; risk of creating the wrong organization or configuring the wrong environment.
- **Sequence:** GitHub identity and demo repository were provided; recruiter said an invitation should be present and the account upgraded; mailbox searches found no invitation; GitHub authentication worked but led to a setup flow requesting profile and organization details; candidate asked recruiter to clarify and did not proceed with organization creation.
- **Observed versus assumed:** The unexpected setup prompt and absent email are firsthand observations. Incorrect provisioning, a broken invitation, and whether profile setup is actually required are **hypotheses, not established defects**.
- **Reproduction gaps:** Exact on-screen wording, browser/OS, organization name, entitlement state, and eventual outcome were not captured. Check these after access is resolved.
- **Potential teaching use:** Build a new-user readiness checkpoint: confirm correct GitHub identity, organization membership, Enterprise plan, and repository integration before starting CLI/Firewall exercises. Link to training material only after the scenario is adopted.

### Follow-up recorded 2026-11-18

The private work-item record now records Mason's confirmation that organization access works, reported to Grok on November 18 about the night of November 16. This supersedes the entry's earlier access-pending status. It is an owner report, not a reproduced scan or verification of token scopes/Enterprise capabilities in this task. The original first-login observation above remains as dated evidence.

## Entry 002 — Concurrent integration reporting (planning)

- **Status:** Documented caveat; experiment not run.
- **Source:** [Socket Scan from CI/CD](https://docs.socket.dev/docs/sca-ci), checked November 18, advises choosing either the GitHub App or a pipeline on a GitHub repository to avoid two sets of comments.
- **Decision:** Mason explicitly accepts this risk for a controlled concurrent GitHub App/Actions comparison. The earlier suggestion to disable CI before App installation is superseded.
- **Expected evidence:** Separate App and Actions outputs on the same PR/head commit, duplicate-comment examples if observed, notifications/review burden, timing, check behavior and closure of the overlap. Use the [comparison protocol](integration-comparison.md).
- **Actual result:** No integration installed/configured and no scan or duplicate PR comment observed during this documentation work.
- **Potential documentation improvement:** Add a comparison note explaining how to attribute App versus CI feedback and return to one normal PR-reporting path after an evaluation.

For technical issues, also record product version, OS, CLI version, relevant errors, first steps tried, and resolution when applicable. Do not paste tokens, private correspondence, or confidential data.

## Entry 003 — API token rotation documentation typo (verified 2026-11-18)

- **Status:** Verified in the public documentation; proposed correction not submitted to Socket.
- **Official source:** [Socket API Tokens — Rotation](https://docs.socket.dev/docs/api-keys), section **Rotation**.
- **Observed text:** “API Tokens can be shown to disabled and forcibly rotated in the case of incidents requiring action.”
- **Issue:** “can be shown to disabled” is grammatically malformed and obscures the intended instruction. It may be a leftover from the preceding “Visibility” section. The documented `api-tokens:revoke` and `api-tokens:rotate` scopes support using “revoked” rather than assuming a separate “disabled” operation.
- **Suggested editorial rewrite:** “API Tokens can be revoked and forcibly rotated in the case of incidents requiring action.”
- **Why it matters:** In an incident-response procedure, users need clear, unambiguous directions about revoking and rotating credentials. The document lists `api-tokens:revoke` and `api-tokens:rotate` as API scopes, supporting this terminology; actual UI action labels should still be checked.
- **Provenance:** Firsthand documentation review during interview preparation; not a user-reported issue or a reproduced product defect.
- **Presentation value:** A concrete low-effort improvement to official public documentation, to pair with a substantive onboarding or troubleshooting recommendation when discussing Part I §5.

## Entry 004 — CLI token scopes dispersed across command references (firsthand, 2026-11-18)

- **Task:** Part I §1.1, determine least-privilege organization token for creating, inspecting and policy-evaluating Socket scans before creating the token.
- **Environment:** Socket CLI v1.15.0; user inspected CLI `socket scan --help` / `socket scan create --help` and [Socket scan docs](https://docs.socket.dev/docs/socket-scan), plus [API token docs](https://docs.socket.dev/docs/api-keys).
- **Expected:** Easy, task-oriented mapping from a common end-to-end workflow (first scan + review + policy evaluation) to the minimum combined token scopes.
- **Observed:** Required permissions are documented, but scattered by command and in a prose `Report` subsection. The user initially found the `full-scans:create` requirement, identified `full-scans:list` for other scan commands, and `security-policy:read` for `scan report`, but had to search across a long CLI-reference-style page to assemble the workflow. They emphasized this is a **discoverability/workflow guidance issue**, not absent information, and they had time pressure. No product defect or failed authorization was observed.
- **Verified permission combination:** `socket scan create` → `full-scans:create`; `socket scan list/view/metadata/diff` → `full-scans:list`; `socket scan report` → `full-scans:list` **plus** `security-policy:read`; `socket scan create --report` uses all three. Source: [Socket scan docs](https://docs.socket.dev/docs/socket-scan), API Token Requirements / Report / List-View sections. The user's pasted `socket scan create --help` independently confirms `full-scans:create`.
- **Suggested improvement:** Add a **task-based least-privilege workflow matrix / worksheet** with complete scope sets for common jobs (first scan, scan-and-evaluate policy, read-only triage, CI automation, scan administration). Link each row to command references and explain optional vs. required permissions. This is a starting recommendation; exact information architecture remains open pending more product experience. A template could include *goal / commands / required scopes / optional scopes / verification / common failure modes*.
- **Teaching value:** Build a quickstart permissions decision aid to prevent granting broad scopes just to get a scan working and speed first-week onboarding for SEs/TAMs/Support.
- **Status:** Firsthand friction recorded; proposed docs change not submitted to Socket. No API token created yet. Full spreadsheet handoff context, scoped sample matrix, and non-final design considerations are saved in [CLI permissions worksheet handoff](cli-permissions-worksheet-handoff.md); Work thread will receive separate user-specific build instructions.


## Entry 005 — Package-score explainability and human-centered documentation (firsthand, 2026-11-19)

- **Task:** Investigate the Socket GitHub App's automated PR dependency-review comment on [PR #1](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/1#issuecomment-7012611620), then drill into the package's assessment.
- **Observed:** For newly introduced `npm/picocolors@1.1.1`, the App reported Supply Chain Security **100**, Vulnerability **100**, Quality **72**, Maintenance **80**, and License **100**. The full dependency-diff report's package details displayed those scores plus maintainer, license, size and direct/production classification. The linked [public package overview](https://socket.dev/npm/package/picocolors/overview/1.1.1) did not provide the specific factors or calculations that led to the Quality 72 and Maintenance 80 scores in the views the user inspected. The [Package Scores documentation](https://docs.socket.dev/docs/package-scores) offers general scoring criteria, not a demonstrated package-specific score breakdown.
- **Problem / impact:** Scoring is visible and accessible, but the path from score → contributing evidence → decision is not clear in the inspected surfaces. This limits developer and security-reviewer ability to distinguish an innocuous lower score from one requiring investigation or remediation.
- **User's enablement assessment:** Make explanatory information more readily available, organize it for human comprehension rather than exposing raw technical values, and target guidance to the decision-maker. User compared the document style to early automated-documentation prototypes, but **the actual authoring process is unknown; do not claim AI generated Socket's docs**.
- **Proposed improvement:** Make individual category scores explainable with contributing factors, contextual evidence, actionable interpretation and direct links. Example flow: **What does this score mean? Why this score for this specific package? What should I do next?** Consider developer/analyst personas and an annotated PR-example walkthrough rather than numbers alone.
- **Status:** Firsthand navigation and user assessment recorded; no formal product defect or exact score-calculation failure established. Not submitted as feedback to Socket.
