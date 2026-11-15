# Public user friction signals (unverified reports)

Collected 2026-11-15 from the public Socket CLI issues index: https://github.com/SocketDev/socket-cli/issues . These are attributed issue titles and triage leads, **not confirmed customer impacts, current defects, or verified reproductions**. Some reporters may be developers rather than paying customers.

| Signal | Public report / source | Potential enablement implication | Verify next |
|---|---|---|---|
| CS-01 | Issue #1160: "Possibly outdated FAQ or unclear README" https://github.com/SocketDev/socket-cli/issues/1160 | Compare onboarding docs to installed version; identify novice decision points | Read issue body, reproduce relevant doc path |
| CS-02 | Issue #1489: pnpm v9 lockfile parsing allegedly creates alerts for packages not in tree https://github.com/SocketDev/socket-cli/issues/1489 | Teach validating findings before asserting a security incident; triage false positives | Review issue, package/version, current status |
| CS-03 | Issue #999: reported 429 rate limit during clean npm install on free plan https://github.com/SocketDev/socket-cli/issues/999 | Explain service plan and rate-limit errors vs policy blocks | Review limits and current issue |
| CS-04 | Issue #947: npm installed via mise reportedly not recognized by Socket wrapper https://github.com/SocketDev/socket-cli/issues/947 | Troubleshooting package-manager PATH and runtime setup | Check exact environment and reproduction |
| CS-05 | Issue #946: request to remember accepted risks https://github.com/SocketDev/socket-cli/issues/946 | Teach managing findings, exceptions, and accepted-risk workflow | Compare current policy/exception docs |
| CS-06 | Issue #1497: Homebrew distribution requested https://github.com/SocketDev/socket-cli/issues/1497 | Setup and packaging expectations may differ across developer OSes | Check available installation paths |
| CS-07 | Issue #1479: reported Node 18 regex parse problem https://github.com/SocketDev/socket-cli/issues/1479 | Teach supported runtime matrix / error triage | Validate version and status |
| CS-08 | Issue #68: reported Node 24 / Next.js missing --permission option https://github.com/SocketDev/socket-cli/issues/68 | Teach distinguishing wrapper/runtime failures from security blocks | Validate source title and issue number before use |

## Distinguish evidence from design

- An issue reports an author's experience; it does not establish prevalence, causation, customer identity, or ongoing impact.
- Triage by **importance to new SE/TAM/Support**, not by drama or sensational claims.
- Candidate talk-track question: "Is this a policy block, network/proxy failure, incompatible toolchain, rate limit, or analysis finding?"
- An issue may be addressed by a later release: consult https://github.com/SocketDev/socket-registry-firewall/releases and the actual tested versions.
- Keep a friction log of our own separate from these externally reported cases.
