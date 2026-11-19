# Part I — Continuous hands-on walkthrough

**Status:** Living document; planning completed in part, hands-on execution not started as of November 18, 2026.

**Documentation decision:** Maintain this walkthrough continuously as work occurs. Organize it in actual execution order, not merely the assignment's order, and cross-reference the assignment sections. Capture routine success concisely; preserve additional sanitized evidence for meaningful findings, failures, policy changes, and integration comparisons. Update proactively rather than reconstructing from memory. **Command capture decision:** Record every meaningful command required to reproduce the workflow, with purpose, execution context, and relevant official reference. Preserve full or extended terminal output only where it demonstrates behavior, failure, enforcement, or an important discrepancy; otherwise summarize outcomes. Redact tokens, secrets, and identifying metadata.

**Assignment source:** *Technical Enablement Lead Peer Interview*, Part I, sections 1–5, pages 3–4.

## Before hands-on work — confirmed context and decisions

- Demo repository exists. Current authorization is **documentation only**; no application or scan implementation has been performed through this document.
- Socket Enterprise organization access: owner confirmed login succeeded; scopes/scan capability not yet tested.
- ActivityPulse plan: initial Node.js CLI + Python reporting engine, anonymized CSV records; later YAML/PyYAML dependency PR. Go validation is optional. [PRD](PRD.md).
- CI scan is optional in the assignment, but selected for the comparison. Controlled GitHub App + GitHub Actions overlap is explicitly approved despite possible duplicate PR comments. [Comparison protocol](integration-comparison.md).
- Policy Block → Warn test: prefer an organic finding from ActivityPulse; use a safe deliberate manifest/test dependency only if necessary.
- Final recommendation for which integration to teach first is **deferred until local CLI, App and Actions have been tested and compared**.
- Relevant conceptual research: [Part I §4 notes](part-i-conceptual-notes.md). Known documentation issues and hands-on friction: [friction log](friction-log.md). AI use: [AI verification log](ai-use-and-verification.md).

## Local repository discovery — firsthand observation

- User located a local `socket-project` directory, but `git remote -v` there reported `fatal: not a git repository (or any of the parent directories): .git`. Do not delete or infer its contents.
- User then entered adjacent `socket-technical-enablement-exercise` directory within their local `github` folder. `git remote -v` confirmed `origin` fetch and push target `https://github.com/mlddragon/socket-technical-enablement-exercise.git`.
- This is the correct existing working clone; skip an additional `git clone`. `git status` verified `main` tracking `origin/main`, up to date, with a clean working tree (user-run check). Top-level `ls -la` (user-run) shows only `.git/`, `project/`, `research/`, and `README.md`, with no application directory yet. Proposed `prod/` application directory; inspect `project/` first.

## Walkthrough entries (add in actual execution order)

### Entry 001 — Baseline application and manifests
- **Assignment mapping:** Part I §1.1 prerequisites
- **Status:** Planned; not performed
- **Action / commands:** Pending
- **Expected:** Node.js and Python components run, with analyzable manifests.
- **Actual result / sanitized evidence:** Pending
- **References:** [PRD](PRD.md), [Socket CLI docs](https://docs.socket.dev/docs/socket-cli)
- **Friction / follow-up:** Pending

### Baseline implementation observations (user-run, 2026-11-18)
- Existing correct local clone found at `/Users/masondillon/github/socket-technical-enablement-exercise`, and `main` was clean and tracking `origin/main`.
- `mkdir prod` created a new application directory, followed by `git pull --ff-only`: fast-forwarded `main` from `4b38bc1` to `c8afa2b` with only `project/part-i-walkthrough.md` updated.
- Entered `prod/` and ran `npm init -y`. npm created `prod/package.json` with default name `prod`, version `1.0.0`, main `index.js`, `type: commonjs`, ISC license, and default placeholder test. This is a user-observed successful initialization, not yet committed; no dependencies installed.
- `npm pkg set name=activitypulse` succeeded (no output); `cat package.json` verified `"name": "activitypulse"`, with remaining npm defaults and no dependencies. User confirmed `npm pkg set main=cli.js` completed without error; verification of resulting manifest not independently shown. Next planned: create minimal `prod/cli.js` printing `ActivityPulse v0.1` and `Hello World!` (not yet user-confirmed).

- User created `prod/cli.js` with `'use strict';`, `console.log('Hello World!');`, and `console.log('I am ActivityPulse v0.1');` (verified through user-run `cat cli.js`). This is a deliberate harmless variation on the proposed wording. User ran `node cli.js` from `prod/` and observed exactly two lines: `Hello World!` and `I am ActivityPulse v0.1`; first Node CLI execution succeeded. Next: inspect first five CSV lines with `head -n 5 ../project/data/activitypulse-activities.csv` before implementing Python reporter.

- User ran `head -n 5 ../project/data/activitypulse-activities.csv` from `prod/`; header verified as `record_id,day,participant,activity_type,source,activity_category,duration_hours,status,online`. Example rows show `application`, `follow_up`, `other`, blank or zero durations, and statuses `recorded`/`logged`; these are **sample observations only**, not yet entire-file statistics.
- Next user action: create `prod/report.py` with Python standard library `csv.DictReader`, `Counter(activity_type)`, and JSON summary (`total_records`, `by_activity_type`), reading `project/data/activitypulse-activities.csv` via a path relative to `__file__`. Execution/output not yet observed.

- User created `prod/report.py` and ran `$(brew --prefix python@3.12)/bin/python3.12 report.py` from `prod/`. Python returned valid JSON `total_records: 117`; `by_activity_type`: `application: 27`, `follow_up: 16`, `interview: 4`, `job_readiness: 4`, `other: 66`. Category counts sum to 117; this verifies data read and type-frequency summary (not uniqueness, duration, or schema validation). Next: integrate Node CLI with Python reporter; Python 3.12 path invocation works while default `python3` still points at system Python 3.9.6.

- User ran `command -v python3.12` from `prod/`; observed `/opt/homebrew/bin/python3.12`. The Node CLI can invoke `python3.12` through PATH. Next action proposed: update `prod/cli.js` to launch Python reporter via Node `spawnSync`, parse JSON and display counts; not yet executed.

- User reported updated `prod/cli.js` with Node `spawnSync('python3.12', [reporter])`, JSON parsing and formatted output, then ran `node cli.js` successfully. Observed output: `Hello World!`; `I am ActivityPulse v0.1`; `Activity Summary`; `Total records: 117`; application 27, follow_up 16, interview 4, job_readiness 4, other 66. Confirms end-to-end Node -> Python 3.12 -> CSV -> JSON -> Node reporting with no external application packages yet. User ran `npm install --package-lock-only` successfully; npm reported `up to date, audited 1 package in 191ms` and `found 0 vulnerabilities`. Expected lockfile created, but contents not independently inspected. npm audit is not a Socket scan. Next proposed: create empty `prod/requirements.txt` for standard-library-only Python baseline; verify coverage once Socket scan runs.

- User confirmed `touch requirements.txt` completed, creating an intentionally empty Python baseline dependency manifest (standard-library-only reporter). `git status --short` from inside `prod/` returned `?? ./`, consistent with untracked application directory. `ls -la` from `prod/` verified exactly five application files: `cli.js` (784 bytes), `report.py` (501), `package.json` (247), `package-lock.json` (213), and empty `requirements.txt` (0); no unexpected files/directories. User confirmed executing `git add cli.js report.py package.json package-lock.json requirements.txt` from `prod/` without reported errors. User ran `git diff --cached --stat`: `prod/cli.js` 32 additions, `prod/package-lock.json` 13, `prod/package.json` 13, `prod/report.py` 21, and empty `prod/requirements.txt` 0; total `5 files changed, 79 insertions(+)`, no deletions. User asked about Git's `+` diffstat bars and insertion count; explained these represent changed lines, not editing actions. Staged file count and line totals verified; actual staged content still to be reviewed prior to commit.

- User ran `git diff --cached --check` (no output; whitespace check passed), then `git diff --cached` and shared full staged diff. Reviewed five **new** files (`prod/cli.js`, `prod/report.py`, `prod/package.json`, `prod/package-lock.json`, `prod/requirements.txt`) totaling 79 insertions, consistent with successful Node -> Python report. The Python dependency file is empty; lockfile has zero third-party npm packages. No secrets or unexpected files evident in provided diff. `package.json` still contains default placeholder `test` script which fails if run; replace later if tests are added, but it does not block baseline. User's pager shows `(END)`; next instruct `q` to exit, then commit after user confirmation. Local `main` may lag documentation commits from this chat; reconcile before push.

- User ran `git commit -m "Add ActivityPulse Node.js and Python baseline"` successfully on local `main`. Observed commit `d2cd96e`, 5 files, 79 insertions; all five `prod/` files created. This is **local only** as of the observation; remote sync/push pending. Next step requested: `git fetch origin` to inspect remote documentation changes without affecting local commit.

- User ran `git push origin main` successfully after rebasing; output confirms remote `main` moved from `6ce89d3` to `e078a11`, publishing the five-file ActivityPulse baseline. The resulting baseline commit is [`e078a11`](https://github.com/mlddragon/socket-technical-enablement-exercise/commit/e078a11), replacing pre-rebase local SHA `d2cd96e`. Node and Python functional smoke tests passed previously. **Next:** Part I §1 install Socket CLI, then scope token and first scan. Note baseline has no third-party npm/Python dependencies, so security findings may be absent; verify manifest detection separately.

### Entry 002 — Token and first local CLI scan
- **Assignment mapping:** Part I §§1.1–1.2
- **Status:** Organization token created; CLI authentication and first full scan pending
- **Action / commands:** User created organization API token in Socket web UI. Friendly name: **`Socket Token 1`**. Selected scopes observed/confirmed: `full-scans:create`, `full-scans:list`, `security-policy:read`. Credential securely stored by user in Apple Passwords. No secret or token username/identifier saved to public documentation.
- **Expected:** Scoped token permits full scan and policy-result inspection; requires live verification.
- **Actual result / sanitized evidence:** Screenshot showed selected `full-scans:list` and `full-scans:create`; user explicitly confirmed `security-policy:read` also selected and named credential `Socket Token 1`. Token creation/completion evidenced by appearance in user's password vault. **No CLI authentication or scan has been performed yet.**
- **References:** [Socket scan documentation](https://docs.socket.dev/docs/socket-scan), [Token docs](https://docs.socket.dev/docs/api-keys)
- **Friction / follow-up:** Pending

- User ran `socket login --help` (CLI v1.15.0) while banner still displayed `token: (not set), org: (not set)`. Help states default browser login supplies read-only package/alert/threat-feed access; `socket login --api-token` provides masked API-token login for scans and write commands. Help mentions quota 1 unit and optional `--api-base-url`, `--api-proxy`. Next user action proposed: run `socket login --api-token` and supply `Socket Token 1` secret locally via masked prompt (never share secret). User then ran `socket login --api-token` (CLI v1.15.0). Observed API token verification succeeded, account/org context reported `mason-dillon-interview`, user explicitly declined optional system-wide security-policy enforcement, accepted bash tab completion (takes effect after terminal restart), and CLI reported `API credentials set`. **No credential string, token identifier, or storage file path was recorded.** First scan still pending. User ran `socket scan --help` after login: banner confirmed Socket CLI v1.15.0, token loaded from `(config)` and org `mason-dillon-interview` from `(config)`; masked token prefix deliberately not retained. `create --report` now ready to test; proposed `socket scan create --repo=socket-technical-enablement-exercise --branch=main --default-branch --report .` from repo root. The command creates a real default-branch full scan and performs policy evaluation; **not yet executed**, results TBD.

### Entry 002a — Socket CLI global installation
- User ran `npm install -g socket` from repository root. npm reported `added 24 packages in 1s` and `6 packages are looking for funding`; no installation error reported. This is a **global tool installation**, not an ActivityPulse application dependency. User ran `socket --version` and reported `1.15.0`; installed CLI version now verified. Next run `socket scan --help` before choosing token scopes and scan arguments.

- User ran `socket scan --help` with CLI v1.15.0. Banner reported `token: (not set), org: (not set)` and cwd repository root. Available subcommands: `create`, `del`, `diff`, `list`, `metadata`, `reach`, `report`, `setup`, `view`. Key distinction: `create` creates a scan; `report` checks results against organization security/license policy. Next: inspect `socket scan create --help` to verify invocation and flags before token creation. No token or scan configured yet.

- User ran `socket scan create --help` on CLI v1.15.0. Help explicitly lists API **quota 1 unit** and permission `full-scans:create`; target defaults to cwd and recursively discovers supported manifests in directories, including `package.json` and `requirements.txt`. Supports `--org`, `--repo`, `--branch`, `--default-branch`, `--report`, `--read-only`, and `--cwd`. `--report` waits and runs policy evaluation; `--read-only` stops before creating an actual report. `--reach` is optional full application reachability and not needed for baseline. Token and org remain unset; no scan initiated. Next: create least-scoped organization token in Socket UI, keeping secret value out of chat/logs.

### Entry 003 — GitHub Actions scan
- **Assignment mapping:** Part I §1.3 (optional)
- **Status:** Selected for planned comparison; not performed
- **Action / commands:** Pending
- **Expected:** Runner scan and attributable CI logs for comparison with local CLI.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket CI guide](https://docs.socket.dev/docs/sca-ci), [Comparison protocol](integration-comparison.md)
- **Friction / follow-up:** Pending

### Entry 004 — GitHub App and dependency-change PR
- **Assignment mapping:** Part I §§2.1–2.2
- **Status:** Planned; not performed
- **Action / commands:** Pending
- **Expected:** GitHub App evaluates real YAML/PyYAML dependency PR; concurrent Actions scan documents comparative outputs and any duplicate feedback.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket integration guide](https://docs.socket.dev/docs/sca-connect), [Comparison protocol](integration-comparison.md)
- **Friction / follow-up:** Pending

### Entry 005 — Policy Block → Warn
- **Assignment mapping:** Part I §§3.1–3.3
- **Status:** Planned; finding not yet selected
- **Action / commands:** Pending
- **Expected:** Observe actual block behavior, CLI health and exit code; change action to Warn and compare.
- **Actual result / sanitized evidence:** Pending
- **References:** [Socket policies](https://docs.socket.dev/docs/policies), [Socket scan documentation](https://docs.socket.dev/docs/socket-scan)
- **Friction / follow-up:** Pending

### Entry 006 — Wrap-up and decisions
- **Assignment mapping:** Part I §§2.2–2.3, 4, 5
- **Status:** Deferred until evidence is collected
- **Topics:** CLI/App/CI suitability and failure modes; first-week teaching path; org-scoped tokens; alert resolutions vs policy rules; friction log and public documentation improvement.
- **Actual evidence and conclusions:** Pending
- **References:** [Conceptual notes](part-i-conceptual-notes.md), [friction log](friction-log.md)

## Record format for additional entries

**Date · Step · Assignment mapping · Product/version/environment · Official reference · Expected · Actual · Sanitized evidence link · Friction/insight · Follow-up**.

If the actual order differs from this suggested sequence, preserve true order and renumber or reorganize entries. Do not convert planned expectations to observed facts without evidence. Never publish tokens or private organizational details.
