# Part III · Teach it back

**Topic** · Prepare and present a Socket demo comparing what engineers see in GitHub Actions and the Socket GitHub App.

## Three deliverables

1. **[Hands-on lab · 30 minutes](part-iii-lab.md).** Prepare both integration paths for Courtney at Widgets Mfg, then demo the same dependency change from the engineer’s point of view. Includes a [GitHub template](https://github.com/mlddragon/activitypulse-demo-template) and downloadable setup files.
2. **[One-page customer talk track](part-iii-talk-track.pdf)** ([text version](part-iii-talk-track.md)). Show the two workflows, handle questions about enforcement and developer friction, and recommend a pilot.
3. **[Practical readiness assessment](part-iii-readiness-check.md).** The five-minute in-lab check observes the two-view demo, an unannounced question, and a customer-specific pilot recommendation. A separate proposed 50–60-minute field assessment adds discovery, an observed scan, policy judgment, enterprise troubleshooting, and a POC handoff, with scored evidence and a validation plan. Its five-minute panel walkthrough is a presentation of the design, not the learner's assessment duration.

The [original comparison](integration-comparison.md) provides authentic PR and Actions results for an evidence-based rehearsal. Widgets Mfg is fictional. The [Part II results](part-ii-firewall-results.md) are available separately for install-time enforcement questions.

## Verification

Both private training repos were generated from the template. The shared patch applied cleanly in each, the starter workflow was added to the CI path, and the patched CLI ran with the fictional sample. A fresh [verification PR](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) ran the same patch and workflow where Socket access was already configured. Both integrations passed and posted the dependency change. The [Actions job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/45214727375/job/137832674814) completed in streaming mode after the preferred diff comparison was denied. This pass used one verification PR with both integrations. The learner run uses two repos.

The five-minute readiness check still needs a timed learner trial. The extended field assessment and its enterprise symptom are proposed, not yet learner-tested or validated in a customer environment. No baseline-to-post-training improvement or live enterprise integration is claimed.
