# Claim Extraction Guidelines

## One sentence, one idea

Each claim card must contain exactly one atomic idea. If you find yourself writing "and" to join two findings, split into two claims.

## Causal direction

- If the source states a causal direction ("A causes B", "A leads to B"), capture that direction in the claim text.
- If the source only states an association without claiming causality, use neutral language: "is associated with", "correlates with".
- Do not upgrade an association to a causal claim.

## Hedging language

- If the source says "suggests", "is consistent with", "may reflect", or "tentatively supports", preserve that hedge in the claim text.
- Do not write "X causes Y" when the source says "X is associated with Y".

## Quantitative findings

- If the source states a specific number or range, include it precisely in the claim text.
- Do not round or paraphrase numbers in a way that changes the finding.
- Do not fabricate numbers that appear only in charts. Write "the chart shows an upward trend" rather than inventing a percentage.

## Boundary conditions

- If the source qualifies a finding ("this holds for OECD cities but not developing cities"), capture this in `qualifiers`, not by omitting the condition from the claim.
- If a finding only applies under specific conditions, note those conditions.

## Normative claims

- Do not extract policy prescriptions as empirical claims unless the source explicitly presents them as empirically supported.
- If the source says "cities should do X", classify that as a `design_principle` or `governance_requirement` claim type, not a `causal_association`.

## Duplicates

- Before creating a new claim, check whether an existing claim covers the same idea.
- If the new source adds a more recent data point or a different context, update the existing claim and add the new source to its `sources` list.
- If the new source provides a genuinely different angle (different mechanism, different context, conflicting finding), create a new claim and link it with `contradicts` or `qualifies`.

## Minimum viable claim

A claim is ready to commit when it has:
- `claim_text` (one sentence)
- `claim_type` (from ontology)
- `scope.spatial`
- At least one tag per tag group
- At least one `sources` anchor
