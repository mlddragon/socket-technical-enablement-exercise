# Part I §4 — Technical reference notes (living draft)

**Status:** Research-only. No Socket CLI scan, policy rule, resolution, or API token behavior has been independently tested in the interview organization. These notes answer the assignment's two *think through, no build needed* prompts; expand the open observation sections after hands-on work.

**Assignment:** *Technical Enablement Lead Peer Interview*, p. 3–4, Part I §4.

## 4.1 Why are API tokens org-scoped and capability-scoped?

### Verified from Socket's published documentation

- Socket's REST API authenticates with **organization tokens** created in Socket organization settings, scoped to that organization. The token authenticates to Socket; it is **not automatically a GitHub repository access credential**. Source: [API Authentication](https://docs.socket.dev/reference/authentication).
- A token's **capability scopes** limit which Socket API operations it can perform. The [API Tokens guide](https://docs.socket.dev/docs/api-keys) lists examples including `full-scans:create`, `api-tokens:revoke`, and `api-tokens:rotate`; it says the list can change.
- [`socket scan create`](https://docs.socket.dev/docs/socket-scan) documents `full-scans:create` as its required scope. Confirm actual end-to-end token needs against CLI version, command options, and the exercise organization before finalizing least-privilege setup.
- Token **visibility** (admins only or organization members) and **capability scopes** are separate settings. The API Tokens documentation states visibility does not grant editing capability.
- [Creating and Managing API Tokens](https://docs.socket.dev/reference/creating-and-managing-api-tokens) describes rotation and revocation controls and recommends least privilege and periodic review. The API also documents [rotation](https://docs.socket.dev/reference/postapitokensrotate) and [revocation](https://docs.socket.dev/reference/postapitokensrevoke) endpoints; this is **not proof of built-in scheduled automatic rotation**.

### Planning rationale (not a claim about observed Socket behavior)

Org scoping limits the organization context; capability scoping limits allowed operations. Different narrowly scoped tokens for independent jobs can support separation, revocation, and smaller compromise blast radius. Do **not** claim per-token action attribution in customer audit logs without verifying that exact capability. Treat GitHub App permissions and Socket API token permissions as separate authorization surfaces.

### Open verification / observations

- [ ] Confirm which organization the token belongs to; record no token values.
- [ ] Confirm the actual minimum scopes for the local scan versus GitHub Actions scan.
- [ ] Verify visibility, rotation, revocation and any relevant audit records in the accessible Enterprise environment.
- [ ] Record token lifecycle and failure messages without exposing credentials.
- [ ] Note differences between published documentation and UI/CLI behavior.

## 4.2 When resolve a finding versus create a broader policy rule?

### Verified from Socket's published documentation

- [Resolve Alerts](https://docs.socket.dev/docs/alert-resolutions) describes **persistent, scoped resolutions**, not merely a one-time dismissal. Documented reasons: *Remediated*, *False positive*, *Tolerable risk*, and *Other*. Future matching alerts are resolved automatically.
- Resolution scope can include **location** (repository / repository label), **artifact** (ecosystem, package, version), and **finding** (alert type and identifiers). Omitting dimensions broadens matching. A resolution bounded to a package version usually does **not** carry forward when that version changes.
- [Policies](https://docs.socket.dev/docs/policies) govern classes of alerts with *Block*, *Warn*, *Monitor*, or *Ignore* actions. They evaluate ordered rules and use the first matching rule. Broad rules placed above narrow ones can shadow them.
- [Rule Conditions](https://docs.socket.dev/docs/rule-conditions) documents combinations of location, artifact and finding facts; a rule can match alert type such as `installScripts`. A matching rule is **not automatically a script-content hash approval**.
- [Resolve Alerts](https://docs.socket.dev/docs/alert-resolutions) and [Policies](https://docs.socket.dev/docs/policies) say resolutions take precedence over policy rules. A broad resolution can therefore hide an alert that a policy would otherwise block.
- [Policies](https://docs.socket.dev/docs/policies) states the newer Policies capability must be enabled for the organization; verify whether this interview organization uses Policies + Alert Resolutions or a legacy policy/triage experience before giving exact UI instructions.

### Working decision framework (planning guidance, not product findings)

1. Investigate the actual alert and its applicability; distinguish an inaccurate detection from a real behavior with accepted risk.
2. Use a **narrowly scoped resolution** for an individually reviewed finding that needs no further action; document reason and review owner.
3. Use a **policy rule** to express an intentional, repeatable organizational treatment of a *category* of findings; evaluate potential unintended matches and ordering.
4. If a customer reports excessive repeated reviews, first distinguish repeated **same-version** alerts from reviews triggered by new versions or additional repositories. Determine whether existing resolutions actually match.
5. Consider controlled dependency-update processes and narrowly tailored scope, but keep a path for urgent security releases. Avoid unreviewed blanket package/version trust.
6. Don't promise hash-based automatic carry-forward of an unchanged install script; not confirmed by the cited docs.

### Open verification / observations

- [ ] Identify which policy/resolution UI and API are enabled in the Enterprise organization.
- [ ] Observe an actual finding and its package, version, alert type, repository and identifier.
- [ ] Inspect a narrowly scoped resolution (if appropriate) and what future scans do.
- [ ] Demonstrate Block → Warn independently per Part I §3, documenting health, exit code, and policy effects.
- [ ] Test whether identical findings reappear or remain resolved; no assumed outcome.
- [ ] Confirm whether a script-content-aware exception mechanism exists; no such capability is established by the reviewed references.
- [ ] Record observations and any public-doc improvement in [friction log](../../socket-deliverables/friction-log.md).

## Evidence discipline and expansion

**Documented:** statements above with direct official sources. **Planning guidance:** recommended reasoning, not claims of observed product behavior. **Observed:** none yet for these two scenarios.

For each later observation, append: date, environment/CLI version, action, expectation, actual result, sanitized evidence link, official-doc reference, and any correction to these notes. Keep credentials and private organization details out of the public repository.
