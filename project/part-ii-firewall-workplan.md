# Part II — Socket Firewall live-demo workplan and capture runbook

**Status: PLAN ONLY (November 22, 2026).** This file is a handoff, not evidence that Docker, a registry, a security verdict, or a video has run. Interview: Tuesday November 24, 2026, 1:00 PM Eastern. The original seven-page exercise, sent November 10 by Lindsey Shanks, requires running **registry mode** in a container before the panel, connecting npm or pip, proving an **organization-policy installation block**, preserving terminal output and friction, and bringing Firewall running. Recruiter assistance was requested at least 48 hours before the interview; that cutoff has passed, so report any material blocker promptly rather than waiting. Do not email without Mason approving the message.

**Execution follow-up:** See the [November 22 verified results](part-ii-firewall-results.md) for actual outcomes, capture status and the panel readiness checklist.

## Objective and stopping rule

**Minimum viable outcome (first priority):** a running and reachable Firewall; npm explicitly pointed to it; one clean allowed artifact; an attempted `lodahs@0.0.1-security` download denied by Socket *security policy* with HTTP 403 / npm E403 and a Socket decision/request ID; screenshots and a 60–90-second unedited evidence capture; reproducible commands and friction log. No need to deploy upstream/middle registries, SIEM, multi-host networking or a production architecture.

**Second priority:** confirm the setup can be reopened for the panel and rehearse showing a policy-driven block. **Third:** narration/Descript editing. **Stretch only:** record natural troubleshooting traps and improve existing CLI/GitHub App footage. Respect the assignment's stated five-hour budget and note deviations rather than forcing endless troubleshooting.

## Non-negotiable safety and scope

- Work on Mason's Mac or the environment he will screen-share on interview day. If the Work agent cannot control **that** environment, provide one or two exact commands at a time for Mason to run; obtain pasted/sanitized output before claiming success.
- Use a **separate local demo workspace** (e.g., `~/socket-fw-demo`), not ActivityPulse's working tree. No production deployment, no persistent global npm registry change, no destructive Docker cleanup affecting other services.
- Use a Socket org token scoped to `packages:list` and `entitlements:list`. The *Firewall* environment variable is `SOCKET_SECURITY_API_TOKEN`, not necessarily the name or permissions used for the CLI or GitHub Actions. Never print/paste token values; avoid Docker inspection commands that reveal them. Store local `.env` and private TLS keys **outside** the public GitHub repo.
- The interview PDF explicitly names `lodahs@0.0.1-security`: Socket identifies it as malicious, yet it contains no code. A request is acceptable for observation, but use a throwaway project and `--ignore-scripts`; never run package scripts or install other unknown flagged packages.
- Prefer scoped/temporary npm configuration, a dedicated clean cache and a local CA file, rather than changing `~/.npmrc`, disabling SSL verification globally, or adding a self-signed certificate to the system trust store. Verify sensitive terminal windows/screens before recording.
- **A health response or npm failure alone does not prove enforcement.** A genuine demonstration ties the attempted artifact request to Socket's policy decision with request headers/logs and an org matching the token.
- Keep artifacts **observed vs expected** explicitly distinguished. No scripted screen simulation presented as real output. Only the scenario context may be fictional.

## Story / assumptions (for optional videos)

**Illustrative company: Harborline Software (fictional).** Assume ~200 developers, a GitHub-based engineering workflow, routine CI scans, a security team, and an interest in enforcing approved dependencies at download time. These are *scenario assumptions*, not facts about a Socket customer. They motivate why teams might use CLI for investigation, App for PR review, and Firewall for install-time control. Product behavior, actual versions, port choices, API responses, policy decisions, latency and screenshot contents must be **demonstrated or cited**, not invented.

## Step-by-step procedure and capture checkpoints

Use this as the live Work session checklist. At each checkpoint, update the friction log with **expected → actual → evidence → explanation** and capture only **clean, sanitized** screenshots/short clips. Clip IDs are stable planning labels, not existing media.

### 0. Preflight and protection (5–10 minutes)
1. Confirm the target computer, OS, container runtime (Docker Desktop, Colima/Docker CLI), `docker compose version`, `npm --version`, shell, local screen recording availability, host port 443 availability, and whether the Socket Enterprise org is selected. Do not assume Docker/Colima exists because it was discussed previously.
2. Check for a token with `packages:list` + `entitlements:list`. If absent, create a separate minimal token inside Socket securely (no token in chat). Verify the **same org** whose Default/legacy policy will be tested. Inspect whether UI says **Policies** or **Settings → Security Policy**; migration affects how policy is edited.
3. Make isolated working directories and private `.env`, `socket.yml`, `docker-compose.yml`, `ssl/`. Capture nothing while entering or viewing credentials.
4. Use the official first-time setup guide as the starting recipe, rather than guessing flags from a historical blog.
**Evidence P00:** sanitized host/tool readiness summary; no screenshot necessary unless a material failure. **Stretch T00:** dependency diagram or port-routing trap if it occurs.

### 1. Bring up a *minimal npm-only* Firewall (10–20 minutes)
1. First-time guide config: `socket.api_url: https://api.socket.dev`, `ports.https: 8443`, `path_routing.enabled: true`, single `path_routing.domain` hostname (e.g., `sfw.example.com`), `rewrite_scheme: https`, one route `/npm` → `https://registry.npmjs.org` with `registry: npm`; set `socket.fail_open: true` only as a *documented evaluation choice*, not an assurance that API failures will block. Include `SOCKET_IGNORE_LOG_LEVEL=warn` in the local private env for allowed decision evidence.
2. Follow the official SSL + Docker Compose recipe: local TLS cert with SAN for that hostname, mount cert and config, expose host `443` → container `8443` if free. Use host-only mapping in `/etc/hosts` **after owner reviews any sudo change**, or another resolvable valid hostname. Keep changes reversible. Do not bind to an existing service's host port or alter existing DNS globally without approval.
3. Fallback **only if 443 unavailable:** use explicit non-standard port and set `path_routing.use_incoming_domain: true` (supported on current Firewall versions) so rewritten package URLs keep the incoming hostname/port. Confirm the effective URL before an npm install.
4. `docker compose up -d`, `docker compose ps` and a `curl` health probe. Startup can take tens of seconds. Capture runtime/container version; do not claim security is enabled from a health result alone.
**Evidence P01:** terminal/container showing service up and health, token redacted. **Clip C01:** 6–10 s service/health.

### 2. Prove real upstream/security connectivity (5 minutes)
1. Inspect *sanitized* startup logs for `Resolved org slug from API` and any `Firewall access validation failed at startup` message. Verify hostname routes; a request to IP/`localhost` can receive 404 because its Host header differs.
2. Explain a critical distinction: `/health` can be healthy even when the Socket API cannot be reached or no registry route is configured. With `fail_open:true`, infrastructure failure can allow requests — that would **not** establish policy enforcement.
3. If token/scopes/egress invalid, fix before proceeding; do not blindly flip fail-open to force a 403 and call it a policy block.
**Evidence P02:** masked startup line proving org lookup; route/health comparison if useful. **Stretch T01:** “healthy ≠ protecting” failure diagnostic, **only** capture an actual failure if encountered naturally.

### 3. Configure an isolated npm client and establish the route (5–10 minutes)
1. Work in a new throwaway folder, not the main repo. Use a per-command or project-local npm registry pointing to `https://sfw.example.com/npm/` (with actual hostname/port). Use a dedicated cache so requests cannot silently bypass the proxy. Point npm `cafile` at the generated local test CA rather than disabling TLS verification globally.
2. Check the effective npm registry with `npm config get registry` under that scoped setup, and also validate the metadata URL and rewritten tarball URL. Do not log or screen-record token values.
3. Run a clean allowed-package test (e.g., pinned `lodash@4.17.21`) with `--ignore-scripts --no-audit --no-fund` in the throwaway folder. Inspect `SOCKET_DECISION` logs or other evidence that the artifact was actually fetched **via Firewall**, not from npm cache or a direct registry.
**Evidence P03:** effective registry settings (no secrets) and successful allowed request **with correlation** to Firewall. **Clip C02:** 8–12 s successful allowed package.

### 4. Demonstrate the *policy* block (10 minutes)
1. In a **separate throwaway folder/cache**, attempt the assignment's `lodahs@0.0.1-security` using the scoped registry and `--ignore-scripts --no-audit --no-fund`. The command should **fail**; preserve the exit status and exact npm error without conflating it with networking or TLS.
2. Verify the response to the specific tarball (without executing any code): metadata request may be HTTP 200, while the `/npm/lodahs/-/lodahs-0.0.1-security.tgz` request should be HTTP 403. Inspect `X-Socket-Decision: blocked`, `X-Socket-Block-Reason`, `X-Socket-Request-ID` and/or `npm-notice`. The response is what matters; a `403` without a correlated policy decision is insufficient.
3. Correlate the request ID with sanitized container `SOCKET_DECISION` event. Distinguish `decision` (what client received) from `action` (the policy evaluation); check `block_reason`. If result is not a genuine policy block, report the actual failure and diagnose instead of fabricating success.
4. Do not change org policy unless necessary; the current default is expected to block known malware, but **observe** before making that claim about this org. If a policy change is required, snapshot original setting, get owner approval, make the minimum change in the correct policy UI, retest with cache awareness, and restore afterwards. Beware the new **Policies → Default** system vs legacy Security Policy paths.
**Evidence P04 (hero):** terminal npm `E403` with package, URL and safe redacted request ID. **P05:** sanitized headers showing metadata `200` vs tarball `403`, decision/reason/request ID. **P06:** matching `SOCKET_DECISION` log line. **Clips C03, C04:** short 10–20 s capture of blocked attempt, then 10 s policy/header correlation.

### 5. Check readiness and preserve the demo (5–10 minutes)
1. Keep the successful working container running for Tuesday's panel; capture the exact startup/retest commands and a plan for re-opening the terminal/recordings. **Do not** leave the system's default npm registry changed.
2. Document safe rollback for isolated files, cert trust (if temporarily changed), `/etc/hosts` entry (if one was added), container, and token revocation **after** the panel. Don't revoke or stop a still-needed demo.
3. Update `project/friction-log.md`, `project/ai-use-and-verification.md` as relevant, a factual Part II result summary, and `project/PROJECT-STATUS.md` **only after actual verification**. Save sanitized screen captures in `project/images/part-ii/`; raw video files should remain outside the public repo (local/private media workspace). Record exact raw paths and clip timestamps in a small capture manifest without claiming GitHub can access local assets.
4. Review actual needs for the live panel: explain cold-cache overhead, TLS/private CA, outage fail-open vs fail-closed, private mirror topology, caching, client package manager configuration, and coaching SE/TAM/Support. These are discussion topics; do not attempt production benchmarks or architecture changes just to answer them.
**Evidence P07:** one-page final checklist with proof links, commands, source versions, and remaining issues.

## Optional documentary traps (after minimum outcome is secured)

These are *stretch teaching segments*, **not** reasons to intentionally break the working demo before it is captured. Distinguish documented behavior from firsthand occurrence.

| ID | Documented trap | How to demonstrate safely | Teaching point |
| --- | --- | --- | --- |
| T01 | `/health` green while Socket API/unloaded routes prevent checks | Show healthy + real `SOCKET_DECISION` proof; if an actual API failure occurs, capture relevant sanitized logs | Operational health ≠ security-policy enforcement |
| T02 | Metadata succeeds (200), tarball denied (403) | Capture both requests/headers during required block | Security gate is on artifact download; metadata alone does not prove allow |
| T03 | Alternate-port URL rewrite loses `:8443` (unless `use_incoming_domain` or 443 mapping) | If it naturally occurs, capture metadata URL and corrected URL; otherwise illustrative annotated graphic labeled “documented, not reproduced” | Follow the **rewritten** artifact URL when a fetch fails |
| T04 | npm certificate verification fails on self-signed TLS | Capture failure only if it occurs; show `cafile` correction without globally disabling TLS verification | Trust store varies across clients |
| T05 | Cached npm artifact bypasses Firewall | Contrast warm cached install (if observed) with isolated cache and logged Firewall fetch | No event is not the same as an allow decision |
| T06 | Policies vs legacy Security Policy, or fail-open API outages | Explain with official documentation and observed config; **do not** induce outage or risky global policy changes for footage | Troubleshoot policy ownership and outage posture |

If a worthwhile trap occurs, capture **before and after** as 2 short clips and a note (`symptom / diagnosis / resolution / observed or documented`). No need to generate a finished edit now.

## Screen/video capture and Descript budget

- Before a credential step, **pause recording**. Before a screenshot/clip, hide browser profile/account identifiers, API tokens, org secrets, real emails, internal URLs, screenshots of sensitive settings, local usernames where avoidable. Inspect/crop before public commit or Descript upload.
- Use macOS built-in screen recorder or existing capture tool. Capture **small independent 6–20-second clips** at checkpoints, not hours of terminal footage. Preserve original assets; no need to upload raw video to Descript while troubleshooting.
- Suggested names: `P01-startup-health.png`, `P02-org-validation.png`, `P03-clean-allow.png`, `P04-policy-block.png`, `P05-http-verdict-headers.png`, `P06-matching-decision-log.png`; clips `C01-health.mov` through `C04-block-verdict.mov`. Use only names for clips actually created.
- Build a **90–150 second** Firewall video *only if primary deliverables and live demo are ready*. Import selected sanitized clips once into Descript, stay inside the confirmed free allowance, avoid repeated AI narration/generation/export until a rough cut is approved.
- The second **CLI + GitHub App** video is a stretch goal, supported by existing Part I evidence/PR #1; use existing screenshots first. If new video capture is needed, do it after Firewall.
- Draft scripts: [Firewall walkthrough](appendix/video-scripts/firewall-demo-v1.md) and [CLI + GitHub App comparison](appendix/video-scripts/cli-github-demo-v1.md). These scripts are *unproduced drafts*, and any bracketed media placeholders must be replaced with observed results.
- No public publishing, video creation, or Descript credit usage without a later instruction. Descript is confirmed connected. Camtasia optional, not in the critical path.

## Source of truth and references (re-read before setup)

- Original interview attachment: “Technical Enablement - Peer Interview.pdf”, emailed November 10, 2026 by Socket recruiter Lindsey Shanks, Part II page 5 and panel format page 6. User's prior Gmail thread: `1a1c63b9fb366497`.
- [First-time Socket Firewall setup](https://docs.socket.dev/docs/sfw-block-installs) — TLS, env, Docker Compose, port 443, org-log verification and “healthy ≠ protecting.”
- [Flat block test](https://docs.socket.dev/docs/sfw-flat-block) — `lodahs`, npm `E403`, metadata 200 vs tarball 403 and transitive block option.
- [Developer registry configuration](https://docs.socket.dev/docs/sfw-registry-dev) — npm CA file, cache, registry and errors.
- [Firewall policy config](https://docs.socket.dev/docs/sfw-policy-config) — Default vs legacy, cache, actual verdict.
- [Decision/log data](https://docs.socket.dev/docs/sfw-data) — `SOCKET_IGNORE_LOG_LEVEL`, `decision` vs `action`, cache and logging.
- [Enterprise registry config reference](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference) — `fail_open`, `fail_open_unscanned`, HTTPS ports, `use_incoming_domain` and headers.

**Next session opening:** verify Work can reach Mason's local machine, current Docker/Colima state, permissions/token scopes, and port 443. Proceed checkpoint by checkpoint, pause for owner actions, and capture evidence as it happens.