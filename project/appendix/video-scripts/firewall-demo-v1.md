# Draft video script v1 — Socket Firewall: Stop a Package at Download

**Status:** Unproduced script / illustrative scenario, dated November 22, 2026. Do not record narration claiming success until [Part II evidence](../../part-ii-firewall-workplan.md) has been captured and checked. Target **~2 minutes**, 90–150 s. Descript free allowance: import only selected clean footage after the demo works. Source PDF Part II is page 5 of Socket's “Technical Enablement Lead Peer Interview.”

## Story setup and assumptions

Fictional customer: **Harborline Software**; assume ~200 developers, shared CI, existing repository scans, and concern about a risky dependency entering a build before the next scan or PR. This is an *illustrative use case*, not a real customer. No invented benchmarks, policy effects, or successful results. Script below assumes the planned npm-only downstream setup **succeeds**; replace bracketed shot directions and observed details with actual evidence, or rewrite honestly if it does not.

## Spoken script and storyboard (draft, subject to evidence)

| Approx. time | Voiceover draft | Visual / capture | Proof / caution |
| --- | --- | --- | --- |
| 0:00–0:16 | “Harborline Software already reviews dependency risk in GitHub. But their team asks a different question: can we stop a disallowed package *before* a developer downloads it? That's what we're testing with Socket Firewall.” | Clean title + simple diagram: Developer npm → Firewall → public npm registry. Mark “fictional customer scenario.” | Scenario only; do not claim deployment scale or coverage measured. |
| 0:16–0:36 | “This is registry mode: a container receives package-manager requests, asks Socket for the applicable security decision, then proxies allowed downloads or denies blocked ones.” | `P01-startup-health.png` / `C01-health.mov`, then a sanitized path routing config snippet. | Show product/container version if visible. |
| 0:36–0:50 | “A green health check is useful, but not enough. We also confirm that Firewall can contact the right Socket organization and apply actual verdicts.” | `P02-org-validation.png`, startup log safely cropped. | Do not show an org secret or turn a health check into proof of enforcement. |
| 0:50–1:08 | “I point an isolated npm client at our proxy. A clean package downloads successfully, and Firewall's decision log confirms this request passed through the service.” | `P03-clean-allow.png` / `C02-clean-allow.mov` plus one sanitized decision log. | Don't imply an allow decision if cache bypassed Firewall; validate log correlation. |
| 1:08–1:34 | “Now the test: `lodahs@0.0.1-security`. Socket's exercise identifies it as a malicious test package with no code. Metadata may still load, but when npm requests the actual package artifact, Firewall denies the download.” | `C03-block.mov`, `P04-policy-block.png`, then `P05-http-verdict-headers.png` with highlighted 403, blocked, reason, ID. | Only use if observed in current environment; never execute test package code. |
| 1:34–1:49 | “That request ID ties npm's error to the Firewall decision record. This is different from a CLI scan returning a nonzero exit code: here, the registry path itself refused the artifact.” | `P06-matching-decision-log.png` and concise side-by-side: CLI check vs install-time policy block. | Match actual request ID/reason or omit. |
| 1:49–2:05 | “In a customer rollout, we'd also test certificate trust, warm and cold cache behavior, and the team's chosen posture when the security API is unreachable. The lesson is not just that Firewall starts — it's that we can prove what it actually enforces.” | Closing diagram/three checks: route, policy verdict, diagnostic evidence. | These are rollout considerations, not tested performance claims. |

## Optional 15–25-second teaching inserts, only after the main demo works

- **T01 “Healthy is not protecting”:** Official docs say the health endpoint can succeed without Socket API connectivity or loaded routes. Insert screenshot of a real issue if it occurs, and its resolution; otherwise label a graphic “documented pitfall — not reproduced.” Suggested line: “A healthy container proves it's running, not that requests are being checked. Verify the organization lookup and a real blocked artifact.”
- **T02 “Metadata passes; artifact blocked”:** The 200/403 contrast is part of the required proof and can be highlighted without extra testing. Line: “Don't stop investigating at the package metadata response. Follow the actual tarball download.”
- **T03 “Port rewrite lost my port”:** The official first-time guide notes that metadata can return a rewritten HTTPS URL without nonstandard `:8443`, sending artifact requests to port 443. Only record an actual problem if naturally observed; otherwise explain a diagram explicitly labeled “documented case.” Line: “Inspect the URL npm actually follows; mapping 443 or preserving the incoming host and port addresses this.”
- **T04 “Certificate not trusted”:** If npm raises a certificate error with a self-signed certificate, capture a short before/after using `cafile`, never teach globally disabling TLS verification as the preferred fix.
- If inserts would push the video past 2:30, prefer a separate appendix clip rather than lengthening the main teaching story.

## Capture/edit guide

Use actual clips `C01`–`C04`, screenshots `P01`–`P06` defined in [runbook](../../part-ii-firewall-workplan.md). All visuals involving responses must be real and sanitized. Avoid showing .env, tokens, system-user details and browser account identifiers. Prefer subtle highlights and captions over synthetic terminal screenshots. Record narration only after validating the command outputs. A single rough cut and export are enough to test free-tier watermark/quality; no repeated Descript generations until explicitly approved.

## Evidence and references

[Stand up Firewall](https://docs.socket.dev/docs/sfw-block-installs) · [Flat block](https://docs.socket.dev/docs/sfw-flat-block) · [Decision data](https://docs.socket.dev/docs/sfw-data) · [Developer registry setup](https://docs.socket.dev/docs/sfw-registry-dev).