---
name: progressive-disclosure-docs
description: Use when a dense technical product page mixes everyday tasks, administration choices, and specialist reference material, or when asked for a persona-based or progressive-disclosure documentation rewrite. Applies to restructuring the page for readers with different decisions to make.
---

# Progressive disclosure for technical docs

Rebuild the page in the order readers need information. The main path should let a reader understand the product, complete a routine task, and know when to escalate. Put rollout decisions and deeper diagnostic detail where the people who need them can find them.

## Read the source and map the decisions

- Read the original page. Verify consequential claims against the current primary docs for the relevant product, mode, and version. Keep observed behavior, documented behavior, and editorial advice distinct. If sources disagree or leave a gap, flag it for review rather than guessing.
- Identify the actual readers and their decisions. Usually the everyday user needs to interpret an outcome and take the next step, an admin needs to choose or configure a path, and a specialist needs to explain an edge case or diagnose a failure. Adapt the roles to the product and the request.
- Sort facts by the first decision they affect. An exception that changes a routine action belongs beside that action, even if its mechanics belong farther down. Preserve prerequisites, scope, defaults, and failure conditions that change the answer.

## Write the page in reading order

1. **Introduce the concept in context.** Explain what it is, where the reader encounters it, and why it matters. Give the value in one concrete outcome. Add a short practical payoff paragraph only if it contributes something new.
2. **Explain what readers do most often.** Give a realistic situation, the signal or control they will see, how to interpret it, and what to do next. Show which observations justify a conclusion and which call for verification. A reader who stops here should still be able to handle the common case.
3. **Explain the decisions an admin owns.** Compare alternatives by situation, responsibility, and consequences. Use a compact table when choices are parallel. Make the next action clear and link to the matching setup or reference. Reserve internal mechanics and exhaustive options for the next layer.
4. **Put specialist detail last.** Explain mechanisms that change troubleshooting or interpretation. Give the evidence that distinguishes similar outcomes. Use a labeled expandable section when the target renderer supports it and the content is optional. Otherwise use a named section near the end. Link to the full reference for catalogs, exhaustive settings, and methodology that do not serve this page.

Use natural headings such as “When an install is blocked,” “Choose where to deploy,” and “Trace a download decision.” The persona map guides the structure. Keep numeric depth labels out of the article. Write a replacement page in the requested format. Keep editorial provenance, reviewer notes, and draft status outside the customer-facing article. Include relevant product documentation links in the article where they support a decision or claim.

## Check the result

- **Everyday reader:** Can identify the relevant signal and act without expanding anything.
- **Admin:** Can choose a path, name the tradeoff, and find the matching implementation guide.
- **Specialist:** Can distinguish look-alike outcomes and trace the claim to a source.
- **Fidelity:** Spot-check exact product terms, scope, version limits, and exceptions. Use original wording and link primary sources near relevant claims. Describe verification that actually happened.
