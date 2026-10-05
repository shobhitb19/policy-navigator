# claim-0198

Doubling urban population density is associated with approximately 13% higher local pollution concentration, not lower, and the authors judge a causal interpretation justifiable based on instrumental-variable studies.

**Source:** [Ahlfeldt and Pietrostefani (2019)](../sources/source-0032.md) — [Appendix 4.10: Pollution reduction — causal interpretation justified](../sources/source-0032.md#section-4-10-pollution-reduction)

> "Carozzi and Roth (2018) and Borck and Schrauth (2018) are the most credible estimates... we are confident in recommending the -0.13 elasticity... Given that both... use instrumental variable strategies... a causal interpretation seems justifiable." (Ahlfeldt and Pietrostefani, 2019, Section 4.10)

**Evidence base:** [evidence-0003](../evidence/evidence-0003.md)

**Qualifiers:**
- The paper's Table 6 reports this category as "pollution reduction" with a value of −0.13; because the category is framed as a reduction, the negative sign means the underlying effect is an *increase* in pollution concentration with density, not a decrease.
- This is one of only five categories the authors regard as causally interpretable, resting on Carozzi and Roth (2018) and Borck and Schrauth (2018), both using IV strategies, and confirmed by an original OECD-data analysis.
- This directly corrects claim-0043 (retired), which — via a second-hand citation in Lall et al. (2021), Box 1.4 — reported "8 percent less pollution" from doubling density. That figure inverted the sign of the primary source's own finding.
- Pollution here refers to local pollutant concentration (e.g. particulate matter), not transport-sector CO₂ emissions per capita; it should not be read as contradicting transport-CO₂ findings such as claim-0028 or claim-0036, which measure a different metric.

**Related:** Corrects: [claim-0043](claim-0043.md) (retired).

---

```yaml
claim_id: claim-0198
claim_type: causal_association
scope:
  spatial: metropolitan
  sectoral: environment
context_tags:
- OECD
- high_income
mechanism_tags:
- congestion
outcome_tags:
- emissions
policy_lever_tags:
- zoning
- land_use_planning
- integrated_planning
evidence_strength: meta_analysis
sources:
- source-0032#section-4-10-pollution-reduction
relationships:
  supports: []
  qualifies: []
  contradicts:
  - claim-0043
  depends_on: []
created: 2026-06-30
last_reviewed: 2026-06-30
```
