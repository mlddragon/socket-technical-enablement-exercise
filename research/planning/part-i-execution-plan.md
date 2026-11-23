# Socket Part I — Complete Execution Plan

**Project:** ActivityPulse\
**Status:** Planning — execution not started\
**Interview:** Friday, November 20, 2026, at 1:30 PM Eastern\
**Part III submission deadline:** Thursday, November 19, at 1:30 PM Eastern

## Purpose

Build a minimal, functioning Node.js and Python application; scan its dependencies with Socket; compare the CLI, GitHub App, and optional GitHub Actions integration; demonstrate security policy enforcement; and document findings for the technical interview.

**Execution rule:** Complete one command or interface action at a time. Explain its purpose, inspect the result, and document meaningful evidence before proceeding.

Commands marked *provisional* depend on the final project structure or installed Socket CLI version.

---

## Phase 1 — Establish the ActivityPulse Baseline

### 1. Clone the repository

**Intended Command**

```
git clone https://github.com/mlddragon/socket-technical-enablement-exercise.git
```

**Expected Result:** A local copy of the existing GitHub repository.

**Reason:** Establish a working directory for application development and scanning. First check whether a clone already exists.

### 2. Enter the repository

**Intended Command**

```
cd socket-technical-enablement-exercise
```

**Expected Result:** Terminal operates inside the project repository.

**Reason:** Ensure subsequent commands affect the intended project.

### 3. Inspect repository status

**Intended Command**

```
git status
```

**Expected Result:** Current branch and working-tree changes are displayed.

**Reason:** Establish the baseline before editing files.

### 4. Create the Node.js manifest

**Intended Command — provisional**

```
npm init -y
```

**Expected Result:** A `package.json` file in the selected application directory.

**Reason:** Define the Node.js component and establish its package manifest.

### 5. Create the minimal application

**Intended Command:** File-creation commands to be selected after confirming the directory structure.

**Expected Result:** A Node.js CLI and Python reporter that display Hello World, read the 117-record anonymized CSV, and produce an activity summary.

**Reason:** Build a legitimate, functional polyglot application rather than an artificial security test.

### 6. Execute ActivityPulse

**Intended Command — provisional filename**

```
node cli.js
```

**Expected Result:** A greeting and activity-summary statistics based on the sample data.

**Reason:** Verify application behavior before introducing Socket scanning.

### 7. Establish dependency manifests

**Intended Command — provisional**

```
npm install --package-lock-only
```

**Expected Result:** An npm lockfile corresponding to the Node.js manifest. A suitable Python dependency manifest will also be created.

**Reason:** Provide dependency information for Socket to analyze. A standard-library-only baseline may produce few third-party findings; that limitation must be documented.

### 8. Commit the baseline

**Intended Commands**

```
git add .
git commit -m "Add ActivityPulse baseline"
git push
```

**Expected Result:** A stable application baseline available on GitHub.

**Reason:** Establish a known commit for comparing scans and subsequent dependency changes.

**Checkpoint:** Review staged files before committing. Exclude secrets, sensitive information, and unnecessary generated files.

---

## Phase 2 — Create the First Socket CLI Scan

*Assignment Part I, Section 1*

### 9. Install Socket CLI

**Intended Command**

```
npm install -g socket
```

**Expected Result:** Socket CLI becomes available in Terminal.

**Reason:** Establish the first hands-on Socket integration.

### 10. Verify the installation

**Intended Command**

```
socket --version
```

**Expected Result:** Installed Socket CLI version is displayed.

**Reason:** Record the tool version associated with our results.

### 11. Create a scoped API token

**Intended Command:** Socket dashboard action.

**Expected Result:** An organization-scoped token with only the permissions needed for a full scan, including `full-scans:create` where required.

**Reason:** Demonstrate least-privilege authentication and understand organization/capability scoping.

**Security:** Never publish the token, paste it into project documentation, or capture its value in screenshots.

### 12. Authenticate the CLI

**Intended Command — confirm against installed version**

```
socket login
```

**Expected Result:** Socket initiates its supported authentication flow.

**Reason:** Authorize scanning against the assigned Enterprise organization.

### 13. Execute the first full scan

**Intended Command:** Verified `socket scan create` invocation with the correct organization, repository, and manifest arguments.

**Expected Result:** Socket accepts the manifest scan and creates an identifiable scan result.

**Reason:** Fulfill the primary CLI-scanning requirement.

**Evidence:** Command, CLI version, manifest coverage, scan identifier or URL, analysis status, and relevant output.

### 14. Interpret the scan

**Intended Command:** Use the installed CLI's supported inspection command and Socket dashboard.

**Expected Result:** Findings and analysis state can be examined.

**Reason:** Explain what Socket actually analyzed, what its reported state means, and what remains uncertain.

---

## Phase 3 — Optional GitHub Actions Scan

*Assignment Part I, Section 1.3*

### 15. Configure GitHub Actions

**Intended Command:** Add a documented workflow file after confirming the supported action and tooling.

**Expected Result:** A workflow capable of scanning the baseline repository.

**Reason:** Establish a CI/CD integration for comparison with the local CLI.

**Note:** The documented GitHub Actions implementation may use Python `socketcli`, while the local CLI uses Node.js. Record tool differences.

### 16. Configure the GitHub Actions credential

**Intended Command:** GitHub repository settings or an approved GitHub CLI command.

**Expected Result:** A scoped Socket credential securely available to the workflow.

**Reason:** Enable automated authentication without exposing secrets in source control.

### 17. Execute and inspect CI

**Intended Command:** Trigger the configured workflow and inspect its run in GitHub Actions.

**Expected Result:** A traceable workflow result, including logs and any scan output or errors.

**Reason:** Compare CI setup, permissions, debugging, automation, and feedback with local execution.

**Time control:** This is optional. Stop and document an incomplete attempt if it threatens required deliverables.

---

## Phase 4 — GitHub App and Dependency-Change PR

*Assignment Part I, Section 2*

### 18. Connect the Socket GitHub App

**Intended Command:** Socket/GitHub browser configuration.

**Expected Result:** Socket GitHub App authorized for the exercise repository.

**Reason:** Evaluate the repository-integrated path and its permissions, onboarding, and feedback.

### 19. Create a feature branch

**Intended Command**

```
git switch -c feature/yaml-import
```

**Expected Result:** A dedicated branch for the YAML-import enhancement.

**Reason:** Isolate a legitimate dependency change for PR analysis.

### 20. Implement YAML import support

**Intended Command:** Install PyYAML through the selected Python 3.12 environment and update the application's Python dependency manifest.

**Expected Result:** ActivityPulse supports YAML input while retaining CSV functionality.

**Reason:** Create a realistic new dependency and meaningful application feature.

**Note:** PyYAML is not guaranteed to produce a Socket security alert.

### 21. Test the enhancement

**Intended Command:** Project-specific Node.js/Python tests or CLI invocations, finalized after implementation.

**Expected Result:** CSV processing still works; equivalent YAML input produces expected reporting results.

**Reason:** Verify the feature works independently of Socket's security analysis.

### 22. Commit and push the feature

**Intended Commands**

```
git add .
git commit -m "Add YAML import support"
git push -u origin feature/yaml-import
```

**Expected Result:** Feature branch and dependency changes appear on GitHub.

**Reason:** Provide a specific commit for automated integration comparison.

### 23. Open the pull request

**Intended Command:** GitHub interface or a verified `gh pr create` command.

**Expected Result:** A PR comparing the feature branch with `main`.

**Reason:** Trigger Socket's GitHub App analysis and the configured Actions workflow.

### 24. Compare integrations

**Intended Command:** Inspect GitHub PR checks and comments, Socket dashboard results, and GitHub Actions logs.

**Expected Result:** Evidence attributable to both the GitHub App and Actions workflow on the same PR and commit.

**Reason:** Evaluate differences in setup, authentication, triggers, findings, feedback, diagnostics, timing, and user experience.

**Controlled experiment:** The GitHub App and CI scanning will run concurrently for one bounded PR comparison. Duplicate comments are possible, not guaranteed. After evidence collection, end the overlap and document the resulting configuration.

---

## Phase 5 — Enforce a Security Policy

*Assignment Part I, Section 3*

### 25. Select a reproducible finding

**Intended Command:** Examine scan findings and relevant alert types.

**Expected Result:** A safe, reproducible finding suitable for demonstrating Block and Warn.

**Reason:** A policy change cannot demonstrate enforcement if no matching finding exists.

**Fallback:** If no suitable natural finding exists, use a deliberately selected safe manifest/package test without executing malicious code.

### 26. Configure Block policy

**Intended Command:** Socket dashboard policy configuration.

**Expected Result:** The selected alert type is configured as Block.

**Reason:** Demonstrate organization-level enforcement rather than detection alone.

### 27. Rerun the scan

**Intended Command:** Repeat the verified full-scan command using the appropriate manifests.

**Expected Result:** A scan result reflecting the configured Block policy, including its health indicator.

**Reason:** Verify real enforcement behavior.

### 28. Inspect the CLI exit code

**Intended Command — immediately after scan**

```
echo $?
```

**Expected Result:** The process exit code from the preceding scan.

**Reason:** Capture the CLI's machine-readable status for a blocked scan.

**Important:** Do not assume the exact exit code before observation.

### 29. Configure Warn policy

**Intended Command:** Socket dashboard action changing the same alert type from Block to Warn.

**Expected Result:** Policy action becomes Warn.

**Reason:** Demonstrate a less restrictive customer policy choice.

### 30. Rerun and compare

**Intended Command:** Repeat the verified scan, then immediately run:

```
echo $?
```

**Expected Result:** Evidence showing how scan findings, health status, and exit code differ between Block and Warn.

**Reason:** Explain the operational implications of both policy choices.

---

## Phase 6 — Interview Preparation

*Assignment Part I, Sections 2, 4, and 5*

### 31. Recommend an integration path

**Intended Command:** No terminal command; compare documented firsthand results.

**Expected Result:** A defensible recommendation for which integration a new SE, TAM, or Support Engineer should learn first.

**Reason:** The recommendation must be informed by actual CLI, GitHub App, and, if completed, CI experience.

### 32. Prepare conceptual explanations

**Intended Command:** Review Socket documentation and our observed examples.

**Expected Result:** Clear explanations of:

-   Organization-scoped and capability-scoped API tokens.
- When to suppress an individual finding.
- When to apply a broader package or policy rule.
- The problems created by overly broad or overly narrow security exceptions.

**Reason:** These are explicitly requested interview discussion topics.

### 33. Finalize documentation and friction log

**Intended Command:** Update the repository's walkthrough, friction log, AI-verification log, and comparison evidence.

**Expected Result:** Reproducible command history, meaningful findings, observed failures, documentation improvement proposals, and accurate AI-use disclosures.

**Reason:** The interview panel begins with the friction log and specifically asks what a new technical team member would struggle with.

---

## Scope and Priority Controls

**Required Part I outcomes**

-   Initial Socket CLI scan and interpretation.
- GitHub App integration and dependency-changing PR.
- Comparison of integration choices.
- Block-to-Warn policy demonstration.
- Conceptual security explanations.
- Friction log, including at least one public-documentation improvement.

**Optional or deferred**

-   GitHub Actions CI scan and controlled concurrent comparison.
- Go validator.
- Graphical dashboard.
- Additional application features.

**Time constraint**

The assignment estimates approximately five hours across all three parts and instructs candidates to stop after six hours and bring their notes. Our chosen ActivityPulse build and optional CI experiment extend beyond the minimum.

Part III materials are due **Thursday, November 19, at 1:30 PM Eastern**. Protect time for the short hands-on lab, one-page talk track, and practical readiness check.

## Official and Project References

-   [Socket CLI](https://docs.socket.dev/docs/socket-cli)
- [Socket scans](https://docs.socket.dev/docs/socket-scan)
- [Socket API tokens](https://docs.socket.dev/docs/api-keys)
- [Socket GitHub App](https://docs.socket.dev/docs/sca-connect)
- [Socket CI integration](https://docs.socket.dev/docs/sca-ci)
- [Socket policies](https://docs.socket.dev/docs/policies)
- [ActivityPulse PRD](PRD.md)
- [Continuous walkthrough](../../socket-deliverables/part-i-walkthrough.md)
- [Integration comparison protocol](../../socket-deliverables/integration-comparison.md)
- [Preflight checklist](prerequisites-checklist.md)

**Review status:** No Part I installation, application implementation, scan, or integration configuration has been performed as a result of preparing this document.
