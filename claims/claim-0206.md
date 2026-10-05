# claim-0206

Within the United States, distance between metropolitan areas significantly reduces patent citation probability, with a steep decay at short distances — and this distance effect has not weakened over the 1975–2002 period despite improvements in information and communication technology.

**Sources:** [Li (2014)](../sources/source-0035.md) — [Section 5: US MSA-level results](../sources/source-0035.md#section-5-us-results)

> "Distance significantly reduces citation probability in the within-US estimation, replicating Jaffe et al. (1993). Crucially, this distance decay shows no evidence of weakening over time — the coefficient on the distance interaction with time trend is not significantly different from zero." (Li, 2014, Section 5, paraphrased)

**Qualifiers:**
- The within-US analysis covers 319 MSAs using the Jaffe et al. matching methodology extended with time interactions.
- The absence of a declining distance effect over 1975–2002 is a null result — a failure to reject the hypothesis that the coefficient is constant, not direct evidence that it is constant.
- The result may be consistent with ICT improvements helping maintain localisation by enabling more granular specialisation (clusters become more specialised, not less localised) rather than just failing to reduce it.
- As with all patent-citation evidence, this captures only codifiable applied knowledge.

**Related:**
- [claim-0200](claim-0200.md) — Jaffe et al. baseline: within-MSA localisation
- [claim-0205](claim-0205.md) — Li: international border effects also not declining
- [claim-0210](claim-0210.md) — Badinger & Egger: cross-country productivity spillovers decay with distance

---

```yaml
claim_id: claim-0206
claim_type: stylized_fact
scope:
  spatial: metropolitan
  sectoral: innovation
context_tags:
  - united_states
  - advanced_urbanisation
mechanism_tags:
  - knowledge_spillovers
  - proximity
  - distance_decay
outcome_tags:
  - innovation
  - patent_citations
policy_lever_tags:
  - clustering
evidence_strength: empirical
geographic_scope: united_states
sources:
  - source-0035#section-5-us-results
relationships:
  supports: []
  qualifies:
    - claim-0200
    - claim-0205
  contradicts: []
  depends_on:
    - claim-0200
    - claim-0205
created: 2026-07-01
last_reviewed: 2026-07-01
```
