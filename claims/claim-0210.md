# claim-0210

Geographic distance between OECD countries significantly reduces cross-country productivity spillovers: distance-weighted foreign R&D specifications outperform trade-weighted ones, implying that physical proximity — not just trade intensity — is an independent channel for international knowledge transfer. Countries at the geographic periphery of the innovation system, like New Zealand, therefore capture fewer foreign productivity spillovers.

**Sources:** [Badinger & Egger (2016)](../sources/source-0037.md) — [Section 5: Distance and cross-country productivity spillovers](../sources/source-0037.md#section-5-distance-spillovers)

> "Distance-weighted foreign R&D specifications consistently outperform trade-weighted ones in explaining TFP variation across countries and industries, suggesting that geographic proximity is an independent channel for knowledge spillovers beyond what trade can explain." (Badinger & Egger, 2016, pp. 513–515, paraphrased)

**Qualifiers:**
- The comparison of distance-weighted vs trade-weighted foreign R&D is the key identification strategy; it cannot rule out that distance is proxying for other barriers (language, legal systems, cultural similarity).
- The geographic distance effect is estimated on a 22-country OECD panel 1995–2007; New Zealand-specific effects cannot be directly read from this study.
- The NZ implication (geographic periphery → fewer spillovers) is an inference from the distance-coefficient; the paper does not include NZ in its analysis (NZ is not in all OECD industry panels for this period).
- This finding is consistent at the macro level with Jaffe et al. (1993) and Li (2014) at the patent-citation level, providing convergent evidence across methods and scales.

**Related:**
- [claim-0201](claim-0201.md) — Jaffe et al./Li: national borders contain knowledge spillovers
- [claim-0205](claim-0205.md) — Li: border effects persistent over time
- [claim-0209](claim-0209.md) — Badinger & Egger: own-country R&D elasticity ~0.25

---

```yaml
claim_id: claim-0210
claim_type: causal_association
scope:
  spatial: national
  sectoral: economy-wide
context_tags:
  - oecd
  - advanced_urbanisation
  - new_zealand
mechanism_tags:
  - knowledge_spillovers
  - technology_diffusion
  - distance_decay
  - proximity
outcome_tags:
  - productivity
policy_lever_tags:
  - innovation_policy
  - rd_investment
evidence_strength: empirical
geographic_scope: oecd
sources:
  - source-0037#section-5-distance-spillovers
relationships:
  supports: []
  qualifies:
    - claim-0209
  contradicts: []
  depends_on:
    - claim-0209
created: 2026-07-01
last_reviewed: 2026-07-01
```
