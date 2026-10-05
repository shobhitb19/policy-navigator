# claim-0031

Urban productivity rises approximately 5–6% with each doubling of city population in developing economies (output elasticity 0.067–0.080 using LandScan population data); instrumental variable estimates raise this to approximately 8%.

**Source:** [Collier, Jones & Spijkerman (2018)](../sources/source-0007.md) — [Abstract](../sources/source-0007.md#abstract), [Section 3: agglomeration](../sources/source-0007.md#section-3-agglomeration)

> "After controlling for country, industry, and year fixed effects, we estimate an output elasticity with respect to city size of between 0.067 and 0.080. This implies that urban productivity increases by about 5% to 6% with each doubling of city population." (Collier et al., 2018, Abstract, p. 2)

**Qualifiers:**
- OLS estimates (0.067–0.080) fall by approximately half when firm quality controls are added, consistent with sorting bias; the IV estimate (0.107, ~8%) is preferred but requires the historical population instrument to be valid.
- The study covers formal-sector firms only (5+ permanent workers); results do not apply to the large informal sector that predominates in low-income cities.
- The Africa subsample drives different results — see [claim-0032](claim-0032.md); the 5–6% figure is most robust for Asian and Latin American cities.
- Agglomeration estimates in this study (5–6%) are somewhat above the Donovan et al. (2021) global meta-analysis median of 4.6% ([claim-0001](claim-0001.md)) but within the 2.7–6.4% credible interval.

**Related:** Consistent with: [claim-0001](claim-0001.md) (global meta-analysis, 2.7–6.4%, median 4.6%), [claim-0022](claim-0022.md) (OECD: 2–5%). Modified by: [claim-0032](claim-0032.md) (Africa exception). Mechanism: [claim-0034](claim-0034.md) (connectivity drives the productivity effect).

---

```yaml
claim_id: claim-0031
claim_type: causal_association
scope:
  spatial: metropolitan
  sectoral: economy-wide
context_tags:
- developing
- lower_middle_income
- upper_middle_income
- asia_pacific
- latin_america
- sub_saharan_africa
mechanism_tags:
- agglomeration
- matching
- learning_spillovers
- sharing
outcome_tags:
- productivity
- wages
policy_lever_tags:
- integrated_planning
- metropolitan_governance
evidence_strength: observational_iv
sources:
- source-0007#abstract
- source-0007#section-3-agglomeration
relationships:
  supports:
  - claim-0001
  - claim-0022
  qualifies: []
  contradicts: []
  depends_on: []
created: 2026-06-03
last_reviewed: 2026-06-03
```
