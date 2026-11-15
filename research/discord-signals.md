# Socket Discord community research — initial pass

Collected 2026-11-15 from the **#questions forum** in the user's logged-in Socket Discord tab:
https://discord.com/channels/905691206783209574/1433237869509611592

**Scope limitation:** Only currently visible forum post previews and metadata were inspected. Individual threads and staff replies were not opened. Dates and titles below are as rendered; these are attributed *user reports*, not product-verified facts. Direct post permalinks and resolutions require opening each post.

| ID | Posted | User-reported issue or question | What it may indicate for SE/TAM/Support enablement | Status |
|---|---|---|---|---|
| DIS-01 | 2026-09-29 | User reported `deno install -g npm:socket` resolved to `socket@2.1.0`, labeled “bad build,” while adding `@latest` produced expected version; user asked whether this reflected Deno dist-tags or Socket package metadata and whether it posed a security issue. Environment macOS 27.2 beta, Deno 2.9.7. | Installation trust, version-resolution verification, triage of product vs ecosystem problems | Attributed report; unanswered/unverified |
| DIS-02 | 2026-08-24 | User cited Socket's “free for open-source repositories” FAQ and asked whether Gerrit open-source repositories receive same offering as GitHub; said GitHub integration worked but couldn't add Gerrit. | Clarify integration coverage and marketing/FAQ scope | Attributed report; platform support unverified |
| DIS-03 | 2026-07-04 | User reported a transaction stuck for 11 hours. | **Low priority** — unclear relevance to Socket; could be unrelated spam. Do not use as product evidence | Unconfirmed relevance |
| DIS-04 | 2026-06-09 | User asked which Firewall features Team and Business include versus Enterprise or add-ons, citing discrepancy between product docs and pricing table; specifically asked about registry/proxy modes, custom policy, private registries, RubyGems, telemetry, GCP marketplace. | Edition/entitlement guide and pre-sales qualification talk track | Attributed report; may reflect historic plans |
| DIS-05 | 2026-05-23 | User integrating SFW into a Dockerfile as a front for `uv` reported `CERTIFICATE_VERIFY_FAILED` when building a wheel involving downloads from sourceforge; asked for reliable solution; mentioned ARM64. | TLS/certificate chain troubleshooting and scope of proxied vs direct downloads | Attributed report; root cause not established |
| DIS-06 | 2026-05-19 | User asked whether wrapping package-manager commands in an `sfw` prefix via PowerShell profile was good practice to ensure Firewall coverage. | Deployment design, transparent/proxy vs wrapper tradeoffs, enforcement gaps | Question, not complaint |

## Follow-up priorities

1. **DIS-05**: open the thread; check staff responses and the actual network/certificate mechanism. High relevance to Part II.
2. **DIS-04**: compare current pricing and official docs; avoid teaching potentially stale entitlement claims.
3. **DIS-01**: verify the distinction between `socket` and the actual Socket CLI distribution and Deno package resolution; do not reproduce an installation against an unknown build without due diligence.
4. **DIS-06**: determine documented recommended modes and how package-manager routing is enforced.
5. **DIS-02**: check official integration list and whether Gerrit is supported.

## Traceable training assumptions

- **A-DIS-01:** A new SE may conflate an installer/package-manager metadata problem with a malicious package finding (DIS-01). Candidate learning check: identify which dependency, version, installer and source are actually involved.
- **A-DIS-02:** A new technical seller may need a concise edition/capability matrix (DIS-04), validated against the plan in effect at the time of the customer call.
- **A-DIS-03:** A new support engineer may struggle to separate client trust-store, proxy TLS, and external download certificates in a Docker build (DIS-05). Frame as a troubleshooting hypothesis, **not** a confirmed Socket-caused certificate problem.

**No verified issue resolutions or direct per-post message links yet.**