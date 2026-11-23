# Part III · Teach it back

**Topic** · Prepare and present a Socket demo comparing what engineers see in GitHub Actions and the Socket GitHub App.

## Three deliverables

1. **[Hands-on lab · 30 minutes](part-iii-lab.md).** Prepare both integration paths for Courtney at Widgets Mfg, then demo the same dependency change from the engineer’s point of view. Includes a [GitHub template](https://github.com/mlddragon/activitypulse-demo-template) and downloadable setup files.
2. **[One-page customer talk track](part-iii-talk-track.pdf)** ([text version](part-iii-talk-track.md)). Show the two workflows, handle questions about enforcement and developer friction, and recommend a pilot.
3. **[Practical readiness check](part-iii-readiness-check.md).** Observe a short demo, one customer question, and a recommendation. The five-minute check is included in the lab.

The [original comparison](integration-comparison.md) provides authentic PR and Actions results for an evidence-based rehearsal. Widgets Mfg is fictional. The [Part II results](part-ii-firewall-results.md) are available separately for install-time enforcement questions.

## Verification

Both private training repos were generated from the template. The shared patch applied cleanly in each, the starter workflow was added to the CI path, and the patched CLI ran with the fictional sample. A fresh [verification PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) ran the same patch and workflow where Socket access was already configured. Both integrations passed and posted the dependency change. The [Actions job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/45214727375/job/137832674814) completed in streaming mode after the preferred diff comparison was denied. This pass used one verification PR with both integrations. The learner run uses two repos.
