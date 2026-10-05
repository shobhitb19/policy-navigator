# claim-0180

A New Zealand city located by the water (coastal or near a significant water body) has a Quality of Life measure approximately 0.36 standard deviations higher than an inland city, a relationship that holds consistently across both the 1976-1991 and 1996-2013 periods.

**Source:** [Preston, Maré, Grimes & Donovan (2018)](../sources/source-0030.md) — [Table 3: QL regressions — climate, water, education, health, population](../sources/source-0030.md#table-3-ql-climate-education)

> "Cities by the water can be expected to have a higher QL measure by about 0.36 SD in both time periods" (significant at 5%). (Preston, Maré, Grimes & Donovan, 2018, Table 3)

**Qualifiers:**
- Estimated with city fixed effects; the water-proximity variable is a near-time-invariant geographic dummy, so this captures cross-city rather than within-city variation.

**Related:**
- [claim-0179](claim-0179.md) — Climate significantly affects Quality of Life

---

```yaml
claim_id: claim-0180
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
