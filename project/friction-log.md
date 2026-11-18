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
- **Issue:** “can be shown to disabled” is grammatically malformed and obscures the intended instruction. It may be a leftover from the preceding “Visibility” section. The exact intended product behavior of “disable” versus “revoke” should be confirmed before publishing technical replacement language.
- **Suggested editorial rewrite (subject to behavior verification):** “API tokens can be disabled or forcibly rotated in response to a security incident.”
- **Why it matters:** In an incident-response procedure, users need clear, unambiguous directions about revoking, disabling, and rotating credentials. The document already lists `api-tokens:revoke` and `api-tokens:rotate` as API scopes, so ensure the product's actual action labels match any revised prose.
- **Provenance:** Firsthand documentation review during interview preparation; not a user-reported issue or a reproduced product defect.
- **Presentation value:** A concrete low-effort improvement to official public documentation, to pair with a substantive onboarding or troubleshooting recommendation when discussing Part I §5.
