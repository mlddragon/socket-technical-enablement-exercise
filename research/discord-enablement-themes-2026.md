# Discord enablement themes (May–November 2026)

Research review date: 2026-11-15. This public summary is anonymized. It reflects a bounded review of Socket community discussions and does not establish current product defects, prevalence, or private support outcomes. Detailed message-level evidence is held outside this public repository pending approval to publish it.

## Priorities

1. **Installation and integration troubleshooting.** Community discussions raised friction around package-manager wrappers, version managers, TLS trust during wrapped commands, container builds, and package version resolution. Prepare a current-doc-checked setup matrix and a lab that compares wrapped and native commands, records environment details, and shows when to escalate. The reported causes remain unverified.
2. **Firewall operating model and plan/policy guide.** Questions suggested confusion about when Firewall sees a package fetch, how registry/proxy deployment works, and which policy controls are available by plan. Validate a one-page capability matrix with the current product owner and demonstrate a real fetch alongside a command that does not fetch packages.
3. **Finding triage talk track.** Community discussions included a publicly closed anomaly review and a separate disputed risk assessment with no visible public conclusion. Teach how to distinguish a user report, an anomaly, and a confirmed malicious package; capture evidence and route contested findings without promising a classification.
4. **Support closure and documentation feedback.** Several questions were routed to support or had no visible public answer. Propose a field-ready acknowledgement, tracking cue, next-update expectation, and a test for whether the answer belongs in documentation. Public Discord status does not reveal private ticket resolution.
5. **Ecosystem coverage.** Requests and setup questions touched integrations outside the core workflow. A current support matrix should distinguish supported platforms from workarounds and requested integrations.

## Evidence standard

- A community report is attributed evidence of one user's experience, not a verified product fact.
- A visible moderator response establishes only what was said publicly, not a private ticket outcome.
- Each training decision above is a hypothesis until checked against current Socket documentation and a sanitized lab.
- Keep implementation notes and lesson drafts in `socket-deliverables/`; keep source research in `research/`.

The [detailed Discord research report](https://drive.google.com/file/d/1Ok_zfzgDN3AzKA08m5kYsfdfkqW7z-Wd/view?usp=drivesdk) contains dated message links, attributed reports, staff replies, and public resolution notes. It is private in Google Drive; sign in with Mason's personal Google account to view it.