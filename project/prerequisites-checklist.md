# ActivityPulse / Socket Part I — Prerequisite checklist

**Status:** Planning checklist only; not an installation or setup record. **Last reviewed:** 2026-11-18.

Use before implementation. Mark **verified** only after checking the actual machine, repo, and Socket organization. Never commit passwords, API tokens, GitHub secrets, private organization details, or credentials.

| Item | Verification / acceptance criterion | Current status | Official reference |
|---|---|---|---|
| GitHub exercise repository | Confirm correct repo and main branch are accessible, with write permissions | Repo exists; runtime access not rechecked | [Existing demo repository](https://github.com/mlddragon/socket-technical-enablement-exercise), [GitHub repositories](https://docs.github.com/en/repositories) |
| Socket Enterprise organization | Sign in with the intended GitHub identity; confirm the assigned org is available | Owner confirmed org access; permissions/plan details not separately tested | [Socket API tokens](https://docs.socket.dev/docs/api-keys) |
| macOS terminal and Git | Verify `git --version`; confirm working clone and clean/expected changes | Git CLI verified: `git version 2.54.0 (Apple Git-157)` (user-run check); clone and working tree still unchecked | [Git install](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |
| Node.js runtime | Verify `node --version`; **Socket CLI requires Node.js 22+** | Verified on user's Mac: `v24.21.0` (user-reported terminal output, 2026-11-18); meets documented minimum | [Socket CLI guide](https://docs.socket.dev/docs/socket-cli), [Node.js downloads](https://nodejs.org/en/download) |
| npm | Verify `npm --version`; npm available to install Socket CLI and run ActivityPulse | Verified on user's Mac: `11.19.0` (user-reported terminal output); npm executable available | [Socket CLI guide](https://docs.socket.dev/docs/socket-cli), [npm CLI docs](https://docs.npmjs.com/cli/) |
| Python runtime | Verify `python3 --version`; choose and document target version before implementing the Python reporter | Verified `python3` reports Python 3.9.6 and `which python3` reports `/usr/bin/python3` (user-run checks); Apple system path, leave unchanged; `which -a python3` returned only `/usr/bin/python3` (user-reported); Homebrew inventory shows `python@3.12 3.12.16` and `python@3.14 3.14.10` installed; Homebrew Python 3.12.16 executable independently verified using `$(brew --prefix python@3.12)/bin/python3.12 --version`; selected as ActivityPulse target; system Python left unchanged | [Python downloads](https://www.python.org/downloads/), [Python csv](https://docs.python.org/3/library/csv.html) |
| Homebrew package manager | Verify `brew --version` for separate Python installation management | Verified Homebrew `7.0.12` (user-reported terminal output); Homebrew inventory verified installed `python@3.12 3.12.16` and `python@3.14 3.14.10` | [Homebrew documentation](https://docs.brew.sh/) |
| Python packaging / manifest plan | Choose supported Python dependency manifest and lockfile, if applicable; verify Socket recognizes both ecosystems after first scan | Not chosen | [Socket CLI guide](https://docs.socket.dev/docs/socket-cli), [Socket scan](https://docs.socket.dev/docs/socket-scan) |
| Node.js manifest plan | Create appropriate `package.json` and lockfile during separately authorized implementation; ensure actual meaningful dependencies exist or record a limited/empty baseline | Not implemented | [npm package.json](https://docs.npmjs.com/cli/configuring-npm/package-json), [Socket scan](https://docs.socket.dev/docs/socket-scan) |
| Anonymized sample data | Verify row counts, generic identifiers, no sensitive values; decide which activity fields to report | 117-row CSV committed; application parsing not tested | [Project dataset](data/activitypulse-activities.csv), [Provenance](data/README.md) |
| Socket CLI installation | After authorization, install `npm install -g socket`; verify `socket --version` and help | Not performed | [Socket CLI guide](https://docs.socket.dev/docs/socket-cli) |
| Scoped Socket API token | Confirm org scope, create token with minimal permissions required; for `socket scan create`, docs list `full-scans:create` | Not created/verified | [Socket token guide](https://docs.socket.dev/docs/api-keys), [scan command and scopes](https://docs.socket.dev/docs/socket-scan) |
| Socket CLI authentication | Authenticate with `socket login` or supported environment variable; **do not capture token values** | Not performed | [Socket CLI guide](https://docs.socket.dev/docs/socket-cli) |
| Baseline local scan | Confirm org slug, repo name, branch, manifest coverage, resulting report URL, analysis state, health/exit behavior | Not performed | [Scan from CI/CD: one-off workstation scan](https://docs.socket.dev/docs/sca-ci), [scan reference](https://docs.socket.dev/docs/socket-scan) |
| GitHub Actions permissions and secret | Check Actions enabled, ability to add repo secret, secure Socket API key, supported workflow permissions | Not checked | [Socket for GitHub Actions](https://docs.socket.dev/docs/socket-for-github-actions), [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) |
| CI comparison | Record exact workflow/CLI variant and credentials needed. Socket's GitHub Actions example may use the Python `socketcli`, versus local Node `socket` CLI | Planned, not tested | [Socket CI guide](https://docs.socket.dev/docs/sca-ci), [Socket GitHub Actions](https://docs.socket.dev/docs/socket-for-github-actions) |
| GitHub App permission / installation | Identify required repository permissions and whether allowed by GitHub account; install/configure only during implementation | Not checked | [Socket Connect repositories](https://docs.socket.dev/docs/sca-connect), [Socket GitHub App permissions](https://docs.socket.dev/docs/permissions) |
| Concurrent App + CI evidence | Confirm controlled period, attribution method, same PR/commit comparison, and explicit end condition. Duplicate comments are anticipated, not yet observed | Approved experiment; unperformed | [Socket Scan from CI/CD](https://docs.socket.dev/docs/sca-ci), [comparison protocol](integration-comparison.md) |
| Part II Docker / Docker Compose | Before Firewall work, verify Docker Engine/Desktop and Compose availability; not required to start Part I | Deferred; not checked | [Socket Firewall quickstart](https://docs.socket.dev/docs/socket-firewall-quickstart) |
| Part II Firewall-specific token | Before Firewall work, confirm minimum token scopes (quickstart lists `packages:list` and `entitlements:list`); do not assume the Part I scan token is sufficient | Deferred; not created | [Socket Firewall quickstart](https://docs.socket.dev/docs/socket-firewall-quickstart) |
| Part II npm registry setup | Preserve normal npm registry settings during Part I; later run isolated Firewall client test and restore settings afterwards | Deferred; not configured | [Socket Firewall registry mode](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode) |
| Safe policy demonstration | Prefer an organic ActivityPulse finding; fallback to safe manifest/test dependency; never execute known-malicious code | Decision made; fixture undecided | [Socket policies](https://docs.socket.dev/docs/policies), [scan reference](https://docs.socket.dev/docs/socket-scan) |
| Logs and reference links | Capture meaningful commands, normal results concisely, exceptional outputs in detail; link back to official docs and assignment | Protocol agreed; walkthrough initialized | [Part I walkthrough](part-i-walkthrough.md), [friction log](friction-log.md) |

## Preflight commands (examples only — **not yet run**)

```bash
git --version
node --version
npm --version
python3 --version
socket --version
```

If `socket` is not installed, `socket --version` is expected to fail until CLI setup. Record the actual output when executed; do not mark success from the example.

## Scope and sequencing

1. Verify local runtime and GitHub permissions.
2. Implement the minimal Node.js/Python CSV baseline only after authorization.
3. Create the least-privileged Socket token and run the local scan.
4. Run the optional CI scan and capture evidence.
5. Install GitHub App and evaluate the planned YAML dependency PR with concurrent CI scanning for a bounded period.
6. Use a suitable observed finding for Block → Warn, or a safe controlled fallback.
7. Record lessons continuously in the [walkthrough](part-i-walkthrough.md); choose the first-week teaching path **after** comparing observed integrations.

The above is a plan, not evidence that steps have happened.
