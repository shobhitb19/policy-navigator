# claim-0207

New Zealand agglomeration elasticities — the percentage wage gain from doubling effective density, estimated after controlling for worker sorting via person fixed effects — are positive but sit at the lower end of the international range (~2–4%), consistent with a small, trade-exposed economy facing different urban dynamics than large continental economies.

**Sources:** [Donovan et al. (2022)](../sources/source-0036.md) — [Section 3: Two-step estimation strategy](../sources/source-0036.md#section-3-two-step-estimation); [Section 4: Aggregate agglomeration elasticities](../sources/source-0036.md#section-4-aggregate-results)

> "We find positive agglomeration elasticities for New Zealand over 1976–2018, but these are smaller on average than the international literature suggests. The two-step approach... removes the upward bias from worker sorting that inflates single-step OLS estimates." (Donovan et al., 2022, pp. 7–9, paraphrased from Sections 3 and 4)

**Qualifiers:**
- The two-step estimator used here is more rigorous than the single-step OLS used in Maré & Graham (2009, claim-0051) and addresses the sorting bias identified in claim-0052.
- The ~2–4% range is approximate; the paper reports elasticities that vary across sub-periods and city types rather than a single headline figure.
- "Lower end of the international literature" reflects genuine small-economy effects (shorter supply chains, thinner labour markets) as well as possible data limitations in NZ census microdata.
- This estimate is consistent with quality-adjusted MFP results in Maré (2016) (claim-0072) showing NZ agglomeration effects below the global meta-analytic range.

**Related:**
- [claim-0051](claim-0051.md) — Maré & Graham (2009): NZ 10% density → 0.69% productivity (earlier, less rigorous estimate)
- [claim-0052](claim-0052.md) — 91% of NZ apparent elasticity is worker sorting
- [claim-0208](claim-0208.md) — Donovan et al.: Auckland vs other NZ cities diverging
- [claim-0001](claim-0001.md) — global meta-analysis: 2.7–6.4% per doubling

---

```yaml
claim_id: claim-0207
claim_type: stylized_fact
scope:
  spatial: metropolitan
  sectoral: economy-wide
context_tags:
  - new_zealand
  - high_income
  - oecd
mechanism_tags:
  - agglomeration
  - sorting
outcome_tags:
  - productivity
  - wages
policy_lever_tags:
  - agglomeration
  - land_use_planning
evidence_strength: empirical
geographic_scope: new_zealand
sources:
  - source-0036#section-3-two-step-estimation
  - source-0036#section-4-aggregate-results
relationships:
  supports: []
  qualifies:
    - claim-0051
    - claim-0052
  contradicts: []
  depends_on: []
created: 2026-07-01
last_reviewed: 2026-07-01
```
