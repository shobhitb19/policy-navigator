# claim-0200

Within the United States, a patent is approximately 5–10 times more likely to cite another patent from the same metropolitan area than would be predicted by the geographic distribution of patenting activity, providing direct evidence that knowledge spillovers are strongly geographically localised.

**Sources:** [Jaffe, Trajtenberg & Henderson (1993)](../sources/source-0033.md) — [Section IV: Main results](../sources/source-0033.md#section-4-results)

> "We find that citations are indeed more likely to come from the same state as the cited patents than one would expect if citations were made without regard to location... the localization is particularly strong at the SMSA level." (Jaffe, Trajtenberg & Henderson, 1993, p. 577)

**Qualifiers:**
- The ratio of localisation (5–10x) is approximate; the paper reports the probability of same-state and same-MSA citation relative to a matched control set of non-citing patents.
- The result is based on USPTO patent data; it may not generalise fully to countries with different intellectual property systems or scientific publication cultures.
- Patents are an imperfect proxy for knowledge spillovers — they capture only codified, applied knowledge; tacit and pre-commercial knowledge spillovers may be more localised still.
- The finding is for the US in the 1970s–1980s; subsequent work (see claim-0205, Li 2014) finds that localisation has not decreased over time.

**Related:**
- [claim-0201](claim-0201.md) — national borders further concentrate knowledge spillovers
- [claim-0202](claim-0202.md) — localisation does not fade quickly with patent age
- [claim-0203](claim-0203.md) — Audretsch & Feldman: tacit knowledge mechanism

---

```yaml
claim_id: claim-0200
claim_type: stylized_fact
scope:
  spatial: metropolitan
  sectoral: innovation
context_tags:
  - united_states
  - advanced_urbanisation
mechanism_tags:
  - knowledge_spillovers
  - learning_spillovers
  - proximity
outcome_tags:
  - innovation
  - patent_citations
policy_lever_tags:
  - agglomeration
  - clustering
evidence_strength: empirical
geographic_scope: united_states
sources:
  - source-0033#section-4-results
relationships:
  supports:
    - claim-0201
    - claim-0202
  qualifies: []
  contradicts: []
  depends_on: []
created: 2026-07-01
last_reviewed: 2026-07-01
```
