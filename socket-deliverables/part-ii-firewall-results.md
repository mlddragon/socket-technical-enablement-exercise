# Part II · Socket Firewall registry-mode results

**Verified November 22, 2026.** Mason ran Socket Firewall 2.23.0 in registry mode on the interview Mac using Docker and Colima. An isolated npm project installed an allowed package through Firewall. A second project received a policy-driven HTTP 403 when npm requested the exercise fixture’s tarball.

## What the requests showed

| Request | Result | Evidence |
|---|---|---|
| `/health` over TLS | HTTP 200, container up | P01 shows the certificate-verified request and the container bound to `127.0.0.1:8443`. P02 records the matching organization lookup with the slug masked. Health verifies that the service responds. The lookup and package decisions establish that Firewall reached Socket. |
| `lodash@4.17.21` | npm added one package. Firewall returned HTTP 200, with upstream HTTP 200. | npm reported a rewritten tarball URL on the local Firewall route. P03 shows an uncached download with `decision: allowed`, `action: monitor`. Socket recorded Medium CVE and High CVE alerts under Monitor. |
| `lodahs@0.0.1-security` | npm reported `E403` and **Blocked by Security Policy** for the tarball. | The npm notice and Firewall’s P06 event shared request ID `13c0…2f15` (masked). The event records `decision: blocked`, `block_reason: Known malware`, and `response_code: 403` on an uncached download. Socket recorded Possible typosquat attack separately as a warning. |
| Separate HTTP requests for that fixture’s metadata and tarball | Metadata HTTP/2 200. Tarball HTTP/2 403. | P05 records the tarball’s `x-socket-decision: blocked`, `x-socket-block-reason: Known malware`, and its own request ID. Use the npm attempt’s ID to find the P06 event. |

This test verifies policy enforcement at artifact download. A successful metadata response can precede a blocked install. The allowed request also shows that an applicable Monitor rule can allow the download while recording alerts.

## Environment and scope

- Apple Silicon Mac with Colima, Docker Engine 29.5.2 server and Compose 5.8.0. npm 11.19.0 on Node.js 24.21.0.
- Firewall image pinned to `socketdev/socket-registry-firewall@sha256:dda95362da176e8ffc58fd87ff25402f4fabc0ac507f202d474eecf611b1a82b`. The decision log reported Firewall 2.23.0.
- A single `/npm` route forwards to the public npm registry. Incoming host and port were preserved in the rewritten tarball URL. TLS used a local certificate with `localhost` in its SAN, trusted by the demo clients through a scoped CA file.
- The demo used two throwaway npm projects with separate caches, TLS verification enabled and package scripts disabled. Afterward, npm outside those projects still resolved to `https://registry.npmjs.org/`. The demo used the existing organization policy.
- The evaluation config uses `fail_open: true`. Outage behavior, warm-cache behavior and rollout performance were outside this test. The optional video’s Harborline Software story is fictional.

## Evidence and Tuesday readiness

| Checkpoint | Reviewer evidence |
|---|---|
| P01 · Startup and health | [Container status and HTTP 200](images/part-ii/P01-startup-health.png) |
| P02 · Organization lookup | Saved startup line below, with the organization slug masked |
| P03 · Allowed installation | npm success line and selected Firewall decision fields below |
| P04 · Blocked install | npm’s original error lines below, with the full request ID and debug-log path omitted |
| P05 · Response headers | The direct HTTP check below, with its separate request ID masked |
| P06 · Request correlation | [Matching Firewall decision screenshot](images/part-ii/P06-matching-decision-log.png) |

<details>
<summary>Terminal excerpts for P02–P05</summary>

```text
P02 · Firewall startup
socket-firewall-1  | [2026-11-22 21:38:23] INFO: Resolved org slug from API: [INTERVIEW ORG]

P03 · npm result and Firewall event
added 1 package in 566ms
decision: allowed
action: monitor
monitor_reason: Medium CVE,High CVE
response_code: 200
upstream_status: 200
cached: false

P04 · npm result
npm error code E403
npm error 403 403 Forbidden - GET https://localhost:8443/npm/lodahs/-/lodahs-0.0.1-security.tgz - Blocked by Security Policy

P05 · Direct HTTP check
/npm/lodahs
HTTP/2 200

/npm/lodahs/-/lodahs-0.0.1-security.tgz
HTTP/2 403
x-socket-request-id: [REDACTED]
x-socket-decision: blocked
x-socket-block-reason: Known malware
```

</details>

The interview Mac holds the full local capture set and two raw clips. C02 shows the allowed install (44.5 seconds). C03 shows the policy block (26.6 seconds). The clips are available for the panel as a fallback. The optional edited walkthrough remains unproduced.

Before the Tuesday panel, keep Colima and Firewall running and recheck this endpoint from the demo directory. The certificate is scoped to this request.

```sh
curl --noproxy '*' --cacert ssl/fullchain.pem \
  -sS -o /dev/null -w 'Health: HTTP %{http_code}\n' \
  https://localhost:8443/health
```

Expected response is `Health: HTTP 200`. If the container has stopped, use `docker --context colima compose up -d` from the demo directory, then recheck health and the organization lookup. Keep the local captures available as a fallback. After the panel, use the [runbook](part-ii-firewall-workplan.md#5-check-readiness-and-preserve-the-demo-510-minutes) for scoped cleanup.

[Runbook](part-ii-firewall-workplan.md) · [Friction log](friction-log.md#entry-006--firewall-registry-mode-preflight-and-troubleshooting-2026-11-22) · [AI use and verification](ai-use-and-verification.md) · [Firewall setup guide](https://docs.socket.dev/docs/sfw-block-installs) · [Firewall decision data](https://docs.socket.dev/docs/sfw-data)
