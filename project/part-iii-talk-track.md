# Part III — Customer Talk Track (one page)

## “Did Socket block the dependency, or did the scan fail?”

**Audience:** Developer lead / DevSecOps / customer engineer.  
**Core message:** An unsuccessful CI run is not always a security decision. First determine whether scanning completed, whether a dependency alert was evaluated under policy, and whether the infrastructure/API path worked.

### Opening (30 seconds)
“Socket can flag risky package behavior, then apply your organization's selected action. Separately, the scanner relies on valid credentials, connectivity, permissions and workflow configuration. If a job fails, we'll separate those two paths before deciding whether to change code, policy or the integration.”

### Three patterns to explain

| Customer sees | What it means in our verified ActivityPulse examples | First response |
|---|---|---|
| **Block:** `potentialVulnerability`, `policy: error`, `healthy:false`, CLI exit **1** | Scan evaluated PyYAML 6.0.2; active policy enforced the finding | Examine the exact dependency, behavior, policy scope and options; don't blindly bypass |
| **Warn:** `policy: warn`, `healthy:true`, exit **0** | Finding is visible at Warn report level, but this scan did not fail | Explain accepted policy posture, document risk/owner as appropriate |
| **Tooling error:** HTTP **401 Unauthorized**, Python CLI exit **3** | GitHub Actions failed to authenticate before completing its scan | Verify the intended secret and credential handling; don't classify the package as unsafe |

**Caution:** These exit codes were observed in this exercise, not guaranteed universal mappings. Interpret the surrounding logs.

### Likely questions and responses

**“The pipeline is red. Is our dependency malicious?”**  
“Not necessarily. Show me where the run failed. An explicit policy finding and an HTTP authentication error require different responses.”

**“Can we change Block to Warn to ship?”**  
“That changes organizational enforcement, not the underlying package behavior. Identify which finding triggered, assess exposure and ownership, and use the agreed change-control process. A scoped exception or risk decision should be deliberate and traceable.”

**“Why don't I see the warning in the report?”**  
“Check the reporting threshold. In our experiment, `--report-level=warn` showed a warning hidden by an Error-only report.”

**“But the token was present—how could authentication still fail?”**  
“A masked environment variable proves a value was supplied, not that it is the correct credential. We resolved our 401 only after supplying the actual Socket API token, not a different value associated with its creation.”

**“The Actions check is green but it still says insufficient permissions.”**  
“The preferred diff-scan operation fell back to a streaming comparison, and the full job succeeded. That's a narrower capability gap, not a failed baseline scan. We should disclose the fallback and investigate it if customers require that diff mode.”

**“Do we need the GitHub App and Actions?”**  
“Usually choose one primary PR feedback path. We ran both for a controlled comparison and got duplicate dependency-review comments. Our default for fast onboarding is the GitHub App; CI is appropriate where pipeline-specific enforcement or custom workflow controls matter.”

### Close: customer action plan
“Send the sanitized command/job stage, alert type and policy action *or* API error, affected package and version if present, scan ID, relevant GitHub run URL, and whether the process completed. Do **not** send secret values. We will decide whether the next owner is dependency/policy review or tooling/auth troubleshooting.”

**Evidence:** [Block/Warn results](part-i-briefing.md), [historical runner logs](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628).  
**Scope:** Example outcomes are observed results, not promises of behavior across every Socket edition or version.