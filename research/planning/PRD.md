# ActivityPulse — Product Requirements Document

**Version:** 0.4 — Controlled concurrent integration comparison (2026-11-18)  
**Status as of November 18, 2026:** Planning / requirements discovery

**Repository:** [mlddragon/socket-technical-enablement-exercise](https://github.com/mlddragon/socket-technical-enablement-exercise)  
**Primary interface:** Terminal CLI  
**Data:** Anonymized local records derived from existing trackers  
**Target languages:** Node.js, Python, eventually Go

**Historical scope for this revision:** Informational artifacts only. The application phases below were proposed work at the time. Implementation and integration setup were outside the scope of this revision. See [current project status](../../project/PROJECT-STATUS.md) for implemented work and [the activity log](activity-log.md) for the historical record.

**Change from v0.3:** Mason explicitly chose to run the Socket GitHub App and GitHub Actions CI scanning concurrently for a controlled period, accepting the documented duplicate-comment risk. This replaces the earlier advice to disable CI before connecting the App. The assignment still treats CI as optional; our project decision is to include the comparison when implementation is separately authorized.

## 1. Product Overview

ActivityPulse is a lightweight, extensible activity-reporting application. It consolidates activity records from multiple sources, calculates useful metrics, and presents summaries to users.

The initial use case is job-search activity reporting. However, the application's underlying data model will be generic enough to support other activities in the future.

ActivityPulse will also provide a realistic, controlled development environment for evaluating Socket's software supply-chain security capabilities.

### Design objectives

1. Build a useful application rather than code written solely for demonstration.
2. Start with a terminal interface and defer graphical interfaces.
3. Use multiple programming languages with distinct responsibilities.
4. Keep the application simple, lightweight, and locally executable.
5. Develop incrementally so Socket can evaluate dependencies and their changes.
6. Use anonymized tracker-derived data without requiring databases or external integrations.
7. Preserve a clear relationship between application functionality and Socket interview requirements.

## 2. Technology and Architecture

| Technology | Responsibility | Timing |
|---|---|---|
| Node.js | CLI commands, user interaction, presentation | Baseline |
| Python | Data ingestion, aggregation, reporting | Baseline |
| Go | Record validation and data quality checks | Later enhancement |
| CSV | Existing anonymized activity records | Baseline |
| YAML | Additional import format | First feature PR |
| JSON | Possible internal communication between components | As needed |

JSON remains available as an internal interchange format. CSV is the initial sample-data format.

The baseline application will not require a database, web server, cloud service, or real third-party data integration.

### Conceptual architecture

```text
ActivityPulse CLI (Node.js)
        |
        +-- Reporting Engine (Python)
        |       |
        |       +-- CSV data files
        |       +-- YAML data files (later)
        |
        +-- Validation Utility (Go, later)
        |
        +-- Future Web Interface (deferred)
```

The Node.js CLI will invoke the Python reporting component locally. A simple process invocation and structured output will be sufficient initially.

## 3. Functional Requirements

| ID | Requirement | Phase |
|---|---|---|
| FR-001 | Display "Hello World" in the terminal | Baseline |
| FR-002 | Load anonymized activity records from CSV | Baseline |
| FR-003 | Calculate and display an activity summary | Baseline |
| FR-004 | Run through documented CLI commands | Baseline |
| FR-005 | Support Node.js and Python components in one repository | Baseline |
| FR-006 | Filter activity reports by source or status | First enhancement |
| FR-007 | Import anonymized activity records from YAML | First enhancement |
| FR-008 | Validate missing fields, invalid statuses, and duplicate IDs | Later enhancement |
| FR-009 | Present reports through a browser interface | Future |

### Example initial terminal output

```text
ActivityPulse v0.1

Hello World!

ACTIVITY SUMMARY — SAMPLE DATA

Activities recorded       24
Applications submitted    12
Interviews scheduled       3
Follow-ups pending         5
Offers received            1

Status: Demo data loaded successfully.
```

All sample metrics are fictional.

## 4. Development and Implementation Plan

### Phase 1 — Establish the baseline

**Application work**

- Add a Node.js CLI.
- Add a Python reporting engine.
- Use the existing [117-record anonymized CSV](../../prod/data/activitypulse-activities.csv); preserve its provenance and distinguish reporting credits from elapsed time as described in its [README](../../prod/data/README.md).
- Display "Hello World" and a basic summary.
- Add appropriate package manifests and lockfiles.
- Document local setup and execution.

**Socket work**

- Confirm Enterprise organization access.
- Create a scoped API token.
- Install and authenticate the Socket CLI.
- Run a full scan of the repository's manifests.
- Review the scan results.
- Record findings and friction.

After the successful local scan, plan the optional GitHub Actions scan from Part I §1.3. Leave it available for the controlled overlap in Phase 2. See [comparison protocol](../../project/integration-comparison.md) for prerequisites, evidence, and stop conditions. No workflow is created by this PRD update.

**Expected outcome:** A functional two-language application with an initial Socket scan.

**Important limitation:** If the baseline relies entirely on standard libraries, there may be few or no third-party dependencies for Socket to analyze. That is acceptable for the initial functional baseline, but we must verify that both ecosystems are actually recognized by Socket.

### Phase 2 — Introduce a legitimate dependency change

**Application work**

- Add YAML import support.
- Introduce PyYAML as a Python dependency.
- Maintain CSV compatibility.
- Optionally add source or status filtering.
- Submit the changes through a GitHub pull request.

**Socket work**

- Connect the Socket GitHub App to the demo repository.
- Allow Socket to inspect the dependency change.
- Run GitHub Actions scanning alongside the GitHub App on the same controlled dependency PR and commit. Accept possible duplicate PR comments for this bounded evaluation.
- Compare both workflows, outputs, timing, checks and negative impacts, with the local CLI scan as a reference.
- Record observations about usability, feedback, and security alerts.
- Capture attributable evidence from each integration, then end the overlap and record the selected normal configuration. A duplicate comment is a possible observation, not a promised result.

**Expected outcome:** A meaningful application enhancement that demonstrates dependency-change analysis.

**Important limitation:** PyYAML is not guaranteed to generate a security alert. The GitHub App comparison should not depend on a particular package being flagged.

### Phase 3 — Demonstrate policy enforcement

**Application work**

- Preserve the working application.
- Make only changes necessary to support a controlled policy demonstration.

**Socket work**

- Select an alert type and configure its organization policy to block.
- Re-run the CLI scan.
- Inspect the health indicator and process exit code.
- Change the policy action to warn.
- Re-run the scan and compare behavior.

**Expected outcome:** A reproducible demonstration of how Socket policy affects scanning results.

**Test selection decision (2026-11-18):** First try to use a naturally occurring ActivityPulse dependency finding for Block → Warn. If the scan offers no suitable finding, fall back to a deliberately chosen safe test dependency or manifest entry that yields a reproducible alert without executing known-malicious code. Do not invent a successful test in advance.

**Open dependency:** We must identify and verify a safe, reliable finding matching the selected alert type. A harmless dependency change is not guaranteed to trigger a block.

### Phase 4 — Optional third-language expansion

**Application work**

- Introduce a small Go module.
- Implement record validation.
- Add CLI access to validation results.
- Document the new component and its build requirements.

**Socket work**

- Review the new ecosystem's supported manifests.
- Scan the expanded repository.
- Compare results with the original baseline.

**Expected outcome:** An expanded polyglot application with three meaningful language roles.

**Priority:** Optional. This phase must not interfere with completing the assigned Socket tasks.

### Phase 5 — Future graphical interface

After CLI functionality is stable:

- Add a lightweight web dashboard.
- Reuse the existing reporting engine.
- Keep CLI functionality available.
- Consider real data integrations only if useful.

This phase is outside the current interview scope.

## 5. Traceability to the Socket Interview

The following mapping follows the original *Technical Enablement Lead Peer Interview* assignment. Confirmed requirements are distinguished from our implementation choices.

| Assignment requirement | ActivityPulse implementation | Status |
|---|---|---|
| Environment: Demo GitHub repository | Existing dedicated public repository | Available |
| Environment: Enterprise organization | Recruiter-provisioned Socket organization | Owner-confirmed access recorded; token scopes and lab behavior not verified here |
| Part I, 1.1: Scoped API token | Token for initial CLI scanning | Not yet completed |
| Part I, 1.1: Full manifest scan | Node.js/Python baseline manifests | Planned |
| Part I, 1.2: Interpret results | Examine analysis state and findings | Planned |
| Part I, 1.3: Optional CI scan | GitHub Actions scan, compared to the local scan | Selected project plan; optional in assignment; not executed |
| Part I, 2.1: GitHub App and dependency PR | YAML support with PyYAML | Planned |
| Part I, 2.2–2.3: Integration comparison | Controlled concurrent GitHub App + Actions comparison, with CLI reference | Decision accepted; protocol documented; first-path teaching recommendation explicitly deferred until all three integrations are tested |
| Part I, 3.1–3.3: Block/warn policy | Prefer a naturally occurring ActivityPulse dependency finding; if none suitable, use a deliberately selected safe test dependency or manifest entry | Primary/fallback decision confirmed; finding and behavior unverified |
| Part I, 4: Conceptual questions | [Source-linked living reference notes](part-i-conceptual-notes.md) for API token scoping and resolutions vs. rules | Documented from official sources; firsthand verification and examples still open |
| Part I, 5: Interview preparation | Live demo and friction log | Ongoing |
| Part II: Socket Firewall | Local registry-mode proxy and blocked install | Not yet designed |
| Part III: Teach it back | Lab, one-page talk track, readiness check | Topic not selected |

### 5.1 Part I, Section 1 — First Scan

This is the first assigned hands-on milestone and the current priority.

ActivityPulse supports it by providing:

- A realistic repository.
- Multiple language ecosystems.
- Appropriate dependency manifests.
- A reproducible application baseline.
- A way to inspect results before introducing additional dependencies.

**Acceptance criteria**

- Application runs successfully.
- Node.js and Python execute meaningful work.
- Socket CLI scan completes.
- Scan results can be inspected.
- Observations are entered in the friction log.

**Reference:** Interview assignment, page 3, Part I §1.

### 5.2 Part I, Section 2 — Compare Integration Paths

The planned YAML feature provides an authentic reason to open a dependency-changing pull request.

We will observe how the GitHub App evaluates changes and compare that behavior with local CLI scans and GitHub Actions scanning on the same PR/commit. Mason accepts the duplicate PR comments documented by Socket for a controlled period so we can evaluate both integration experiences and show their negative impacts. This is an exercise-specific exception to Socket's normal recommendation to choose one GitHub reporting path.

The [comparison protocol](../../project/integration-comparison.md) defines the entry criteria, evidence matrix and end condition. Start after baseline/local scanning, overlap on the planned dependency PR, capture results, then disable or narrow CI scanning to end concurrent PR reporting. Record actual start/end events when performed; none has occurred in this documentation task.

**Comparison acceptance criteria**

- Identify each integration's configuration and event on the same repository, PR, base/head commit and manifests.
- Preserve App comments/checks and Actions logs/comments/checks with attributable links; note any missing output.
- Compare findings, wording, policy/check behavior, authentication, setup, troubleshooting and timing.
- Record actual duplicate comments and notifications, review noise, conflicting/stale feedback and extra runs when observed. Clearly label anticipated impacts that do not occur.
- Explain when each integration is appropriate and why concurrent PR reporting is bounded here.
- Capture overlap closure and the chosen normal configuration, or explain an incomplete attempt.

**Still to determine**

- Appropriate repository permissions and installation settings.
- What Socket reports on the PR.
- Whether policy changes influence PR checks.
- Actual differences between CI and the two required paths; tool versions and behavior must be recorded during execution.
- Which integration path should be taught first to a new team member. **Decision: defer the recommendation until the CLI, GitHub App and GitHub Actions experiences have been tested and compared.**

**Reference:** Interview assignment, page 3, Part I §2.

### 5.3 Part I, Section 3 — Enforce a Policy

This requirement is primarily a Socket configuration exercise rather than an ActivityPulse development feature.

The application provides the repository and dependency inventory against which the policy will operate.

We still need a repeatable, safe test that produces a finding subject to the configured block policy.

**Reference:** Interview assignment, page 3, Part I §3.

### 5.4 Part II — Socket Firewall

The existing Node.js and Python package managers provide potential clients for a registry-mode Socket Firewall.

The assignment requires:

- Running Firewall registry mode in a container.
- Configuring a package manager to use it.
- Demonstrating an organization-policy block.
- Capturing terminal evidence.

This should be an **isolated exercise**, not a feature of ActivityPulse's application code.

The Firewall test must not execute malicious package code.

**Open:** Docker setup, registry configuration, policy details, safe test procedure, and failure recovery.

**Reference:** Interview assignment, page 5, Part II.

### 5.5 Part III — Teach It Back

ActivityPulse may supply the environment for the teaching lab, but the topic should be selected based on what we learn during Parts I and II.

The assignment requires:

- One hands-on lab taking 30 minutes or less.
- One-page customer talk track.
- Practical readiness check and definition of “not ready.”

No final topic has been selected.

**Reference:** Interview assignment, page 6, Part III.

## 6. Operational Rules

### CLI-first

All development and testing should use the terminal wherever practical.

We will distinguish between operations supported by Socket's CLI and those that require its dashboard or GitHub interface. CLI-first does not mean avoiding a required UI step when no equivalent is available.

### Scope control

- Do not add frameworks without a clear functional need.
- Do not add unnecessary third-party dependencies.
- Do not build application features solely to create security alerts.
- Do not require a database or network integration.
- Keep demonstration changes reproducible.
- Preserve the original functional baseline.
- Stop adding optional functionality if it threatens interview readiness.
- Keep this task limited to documentation and existing informational artifacts. Implementation requires a later instruction.
- Keep CI scanning within the assignment's optional §1.3; do not expand this into a deployment pipeline.

### Documentation and evidence

For each substantive Socket operation, record:

1. The assignment requirement.
2. Official documentation reference.
3. Action attempted.
4. Expected result.
5. Actual result.
6. Unexpected behavior or friction.
7. Relevance to future technical enablement.

Maintain a separate AI-use and verification log as requested by the interview assignment.

## 7. Current Decisions

**Confirmed design decisions**

- Product: ActivityPulse.
- Generic activity-reporting model, using job-search sample data.
- Node.js CLI and Python reporting engine.
- CSV as the initial data format.
- Terminal output before graphical interfaces.
- Initial "Hello World" output.
- YAML import as a meaningful enhancement.
- Go validator as a planned optional expansion.
- Anonymized, locally stored tracker-derived data; original private records remain in their source trackers.
- No database or external integration in the baseline.
- Incremental changes through pull requests.
- Controlled concurrent GitHub App and Actions scanning for comparison, accepting duplicate PR comments and documenting negative impacts; see [decision and protocol](../../project/integration-comparison.md).
- Select which integration path to teach a new SE first **only after** the three hands-on paths have been compared.
- For policy Block → Warn, first use an organic dependency finding; if none is suitable, use a controlled safe manifest/test dependency as fallback.

**Open design decisions**

- Exact CLI command names.
- Node.js and Python package managers.
- Runtime versions.
- How the baseline handles dependencies.
- Interpretation of the existing CSV fields, especially reporting credits versus elapsed time.
- Exact YAML import behavior.
- Error handling between language components.
- Socket GitHub App configuration.
- Reliable policy-block demonstration.
- Firewall configuration.
- Final teaching topic.

## 8. Next Milestone After Separate Implementation Authorization

The current milestone is to save and verify the PRD, decision, research, dataset and activity records. It does not authorize the application work below.

**Milestone M1 — Functional baseline ready for Socket scanning**

The next implementation should produce a working ActivityPulse CLI that:

1. Loads a small CSV dataset.
2. Uses Python to calculate a summary.
3. Uses Node.js to display the output.
4. Prints "Hello World."
5. Contains appropriate Node.js and Python manifests.
6. Includes clear setup instructions.

Once complete, run the first Socket CLI scan and capture the results.

Do not begin the YAML PR until the baseline is established.

## 9. References

### Interview assignment

*Technical Enablement Lead Peer Interview*, seven-page document supplied by Lindsey Shanks.

- Page 1: Purpose, friction log, time budget.
- Page 2: Organization setup, safety, AI-use expectations.
- Page 3: Part I, sections 1–3.
- Page 4: Part I, sections 4–5.
- Page 5: Part II, Socket Firewall.
- Page 6: Part III, deliverables and interview structure.
- Page 7: Assessment criteria.

### Official documentation

- [Socket CLI](https://docs.socket.dev/docs/socket-cli)
- [Socket scan command](https://docs.socket.dev/docs/socket-scan)
- [Socket SCA quickstart](https://docs.socket.dev/docs/socket-sca-quickstart)
- [Scan from CI/CD: duplicate GitHub reporting caveat](https://docs.socket.dev/docs/sca-ci) — checked 2026-11-18.
- [Socket for GitHub Actions](https://docs.socket.dev/docs/socket-for-github-actions) — checked 2026-11-18; documented Python CLI path differs from the planned local Node CLI path.
- [Connect repositories](https://docs.socket.dev/docs/sca-connect)
- [Socket Firewall quickstart](https://docs.socket.dev/docs/socket-firewall-quickstart)
- [Socket Firewall registry mode](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode)
- [Python CSV module](https://docs.python.org/3/library/csv.html)
- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [Go Modules Reference](https://go.dev/ref/mod)

These references describe the relevant product capabilities and programming tools. The ActivityPulse architecture, phases, and feature choices are our own design decisions.
