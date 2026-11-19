> **Review draft.** AI-assisted rewrite of Socket’s Registry Mode documentation. Technical claims were checked against the cited docs. No live deployment was run.

# Socket Firewall Enterprise in Registry Mode

Socket Registry Firewall runs as a container between the systems that request packages and the registries that serve them. For package downloads routed through Firewall, it identifies the package and version and uses Socket security data and your organization’s policy to decide whether to allow the download. This lets your organization stop a dependency at download time, before a developer or CI job can install it. [Registry Mode overview](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode)

## When an install fails

When Firewall blocks a download, it returns HTTP `403 Forbidden` with a reason and a request ID. If your package manager shows the Socket block message, follow the contact instructions in the message. Share the package name and version, the block reason, and the request ID so your team can find the decision.

If you only see a `403` or a fetch failure, share the exact error and the registry your package manager used with the team that manages it. The status code alone leaves the source of the error uncertain. A repository manager such as Artifactory or Nexus can replace the original Firewall response with its own error page. [Block message reference](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference#block-message-contact-sentence)

## Choose where to deploy Firewall

Choose a deployment based on which system sends requests to Firewall and where those requests go next.

| Deployment | When to use it | Request path and behavior |
| --- | --- | --- |
| Downstream | Developer and CI package managers can point directly to Firewall. | Client → Firewall → public or private registry. [Downstream guide](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-setup-downstream) |
| Upstream | Developers and CI already use a private mirror. | Client → mirror → Firewall → public registry. The mirror sends public package fetches through Firewall and can serve cache hits directly. [Upstream guide](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-upstream-deployment-guide) |
| Middle | Packages move between two private registries. | Private registry → Firewall → private registry. Use this path when the downstream registry needs to resolve the existing package URLs. [Deployment mode reference](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference#deployment-mode) |

For a first trial where you control the package manager’s registry setting, start with the downstream guide. Use an approved dependency and confirm the download appears in Firewall’s logs before treating a successful install as proof of routing. Before rollout, decide separately whether to allow downloads when Socket’s API returns an error and when it has no scan data for a package. [Fail-open settings](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference#fail-open-behavior)

## Trace a download decision

Check the response for the package download itself. For a security-checked download, `X-Socket-Decision` reports the outcome. A value of `blocked` confirms a Firewall block, and `X-Socket-Block-Reason` gives the reason when present. Use the request ID (by default, `X-Socket-Request-ID`) to find the corresponding log entry. Metadata and other passthrough requests can carry an ID without a decision header.

If a repository manager handled the request, check whether it served the download from cache. For a fetch that reached Firewall, use the original response or correlate the request with Firewall logs to identify the decision. [Response tracking headers](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference#response-tracking-headers)

If package metadata loads but the download follows an unexpected path, check the download URL returned in the metadata. The default `rewrite` route mode points download URLs back through Firewall. Middle deployments require `mode: proxy`, which leaves those URLs unchanged for the requesting registry to resolve. [Route modes](https://docs.socket.dev/docs/socket-firewall-enterprise-registry-mode-configuration-reference#route-mode-rewrite-vs-proxy)
