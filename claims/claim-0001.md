# claim-0001

Doubling city population size is associated with a 2.7–6.4% increase in wages or productivity, with a median estimate of 4.6%, based on a meta-analysis of 6,684 estimates from 295 studies covering 54 countries over six decades.

**Source:** [Donovan et al. (2021)](../sources/source-0004.md) — [abstract](../sources/source-0004.md#abstract), [section 5](../sources/source-0004.md#section-5)

> "For our preferred combination of study attributes, we find a median elasticity of 4.6% and a 90% credible interval of 2.7–6.4%." (Donovan et al., 2021, section 5, p. 29)

**Evidence base:** [evidence-0001](../evidence/evidence-0001.md)

**Qualifiers:**
- 90% credible interval; there is a 10% probability the true elasticity lies outside 2.7–6.4%.
- Preferred specification uses wages as the outcome and population density as the agglomeration measure; other dependent variables yield different central estimates.
- Estimates vary by spatial scope: metropolitan-scale estimates have a lower median (3.3%) than national-scale estimates (6.4%). See claim-0011.
- More rigorous controls consistently reduce estimates; raw OLS estimates are upward biased. See claim-0014.
- Overall estimates in production peaked around 1980–2000 and have since declined. See claim-0012.
- Manufacturing sector estimates are approximately 0.6% lower than economy-wide estimates. See claim-0013.
- Models explain only approximately one-quarter to one-third of the variation in estimates.
- Evidence of publication bias in the underlying literature; the true elasticity may be somewhat lower.

---

```yaml
claim_id: claim-0001
claim_type: causal_association
scope:
  spatial: metropolitan
  sectoral: economy-wide
context_tags:
- OECD
- developing
- advanced_urbanisation
mechanism_tags:
- agglomeration
- matching
- learning_spillovers
outcome_tags:
- productivity
- wages
policy_lever_tags:
- integrated_planning
- metropolitan_governance
evidence_strength: meta_analysis
sources:
- source-0004#abstract
- source-0004#section-5
relationships:
  supports: []
  qualifies: []
  contradicts: []
  depends_on: []
created: 2026-06-03
last_reviewed: 2026-06-03
```
