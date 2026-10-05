# claim-0179

Climate significantly affects a New Zealand city's Quality of Life: a one standard deviation increase in rainfall is associated with a 0.27 SD decrease in QL, while a one standard deviation increase in monthly hours of sunshine is associated with a 0.21 SD increase in QL.

**Source:** [Preston, Maré, Grimes & Donovan (2018)](../sources/source-0030.md) — [Table 3: QL regressions — climate, water, education, health, population](../sources/source-0030.md#table-3-ql-climate-education)

> With city fixed effects, 1996-2013: "a city with one SD higher rainfall can be expected to have 0.27 SD lower QL ... a city with one SD more hours of sunshine per month can be expected to have 0.21 SD greater QL" (both significant at 5%). (Preston, Maré, Grimes & Donovan, 2018, Table 3)

**Qualifiers:**
- Estimated with city fixed effects for the 1996-2013 period, controlling for time-invariant city characteristics.
- Climate variables are slow-moving and effectively fixed for a given city, so this primarily explains cross-city rather than within-city QL variation.

**Related:**
- [claim-0180](claim-0180.md) — Coastal/water location raises Quality of Life

---

```yaml
claim_id: claim-0179
claim_type: causal_association
context_tags:
  - new_zealand
  - high_income
mechanism_tags:
  - amenity_value
outcome_tags:
  - livability
policy_lever_tags: []
sources:
  - source-0030#table-3-ql-climate-education
evidence_strength: panel_fe
geographic_scope: new_zealand
```
