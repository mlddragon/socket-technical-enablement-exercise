# Did Socket block the dependency, or did the scan fail?

**Customer talk track · Developer leads, DevSecOps, and customer engineers**

Start with the job stage and the evidence. “Did the scanner return a policy decision for a package, or did the integration stop before it could evaluate one?”

## Read the result

- **Policy Block.** In our PyYAML 6.0.2 example, `potentialVulnerability` had `policy: error`, the scan was unhealthy, and the command exited 1. Review the exact dependency and the alert with the dependency owner and security team before considering changes.
- **Policy Warn.** The same finding had `policy: warn`. The scan was healthy and exited 0. A warning can remain actionable even when the build passes. Use `--report-level=warn` on the compatible report command to see it.
- **Authentication failure.** GitHub Actions returned HTTP 401 and the Python CLI exited 3 before a scan result was available. Ask the CI owner to validate the secret reference and actual credential in the intended organization. Keep the value out of logs.

## Handle common objections

**“The build is red. Is the package malicious?”** A red result tells us where to investigate. Look for the package, finding, and policy action, or for an infrastructure error. Use the surrounding log to interpret exercise exit codes.

**“Can we switch Block to Warn to ship?”** That changes enforcement. Confirm the finding’s relevance and exposure, identify the risk owner, and use the agreed review process for any exception or policy change.

**“The token was present. Why did it still fail?”** A masked value shows the workflow received something. Our successful rerun followed correction of the stored value to the actual Socket API token. Separately, a diff-scan permission denial triggered a streaming fallback and the job passed. Check which operation failed and whether the scan eventually completed.

## Agree on the next owner

Ask for the scan or run link, failed stage, package and version if present, and the policy action or HTTP error. Send policy findings to the dependency and security owners. Send authentication failures to the CI owner. If the evidence is incomplete, say what you observed and which log or report you’ll check next.

**Exercise evidence** · [CLI Block and Warn](part-i-briefing.md#3-security-policy-experiment-ignore--block--warn--inherit) · [GitHub Actions run](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/44557864628)
