# Part III · Teach it back

**Topic:** Show what engineers see when Socket scans the same dependency change through GitHub Actions and the Socket GitHub App.

## Three deliverables

1. **[Hands-on lab · 30 minutes](part-iii-lab.md).** Prepare both integration paths for Courtney at Widgets Mfg. Demo the same dependency change from the engineer’s point of view using the [GitHub template](https://github.com/mlddragon/activitypulse-demo-template) and downloadable starter files.
2. **[One-page customer talk track (PDF)](part-iii-talk-track.pdf).** Show both workflows, handle questions about enforcement and developer friction, and recommend a pilot. [Text version](part-iii-talk-track.md)
3. **[Practical readiness check · five minutes](part-iii-readiness-check.md).** Observe the learner’s two-view demo, one unannounced customer question, and a customer-specific recommendation. Run it in the last five minutes of the lab.

## Evidence and verification

The [original comparison](integration-comparison.md) provides authentic PR and Actions results for a saved-evidence rehearsal. Widgets Mfg is fictional. [Verification PR #2](https://github.com/mlddragon/socket-technical-enablement-exercise/pull/2) confirmed that both integrations could detect the same dependency change on one pre-authorized exercise repo. [Passing Actions job](https://github.com/mlddragon/socket-technical-enablement-exercise/actions/runs/45215148824/job/137834176673)

The patch was checked against the public template. In a November 23 walkthrough, the Actions job passed in the private CI training repo and the Socket App checks passed in the separate private App training repo. Each integration posted feedback for `picocolors@1.1.1` on its own PR. Timing with a new learner remains unmeasured. If access or processing delays get in the way, the lab includes saved results for rehearsal.
