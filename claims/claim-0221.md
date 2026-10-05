# claim-0221

A functional urban area (FUA) under the EU-OECD definition is a city plus its commuting zone, identified in four steps: an urban centre (contiguous 1 km² grid cells of at least 1,500 residents/km² totalling at least 50,000 people), a city (local units with at least 50% of residents inside an urban centre), a commuting zone (contiguous local units with at least 15% of employed residents working in the city), and the FUA as the combination of the two.

**Source:** [Dijkstra et al. (2019)](../sources/source-0040.md) — [Section 2: The short definition](../sources/source-0040.md#section-2-short-definition)

> "1) Identify an urban centre: a set of contiguous, high density (1,500 residents per square kilometre) grid cells with a population of 50,000 in the contiguous cells; 2) Identify a city: one or more local units that have at least 50% of their residents inside an urban centre; 3) Identify a commuting zone: a set of contiguous local units that have at least 15% of their employed residents working in the city; 4) A functional urban area is the combination of the city with its commuting zone." (Dijkstra et al., 2019, p. 5)

**Qualifiers:**
- The definition is people-based (density, population, commuting) rather than morphology-based (built-up area), because built-up area per capita varies across city sizes, development levels, and time.
- Applying it requires a 1 km² population grid, local-unit boundaries, and commuting-flow data; results depend on the size of the underlying local units (discussed in Section 4 of the source).
- This is the definition underlying OECD metropolitan-area statistics, including the city-size and productivity comparisons cited elsewhere in this wiki (e.g. OECD 2015, Ahrend et al. 2015).

**Related:**
- [claim-0222](claim-0222.md) — FUAs capture agglomeration economies better than administrative boundaries
- [claim-0011](claim-0011.md) — spatial scope of measurement changes agglomeration elasticity estimates

---

```yaml
claim_id: claim-0221
claim_type: definition
scope:
  spatial: international
  sectoral: economy-wide
context_tags:
  - OECD
  - europe
mechanism_tags:
  - agglomeration
outcome_tags:
  - urban_form
policy_lever_tags:
  - integrated_planning
evidence_strength: methodological
geographic_scope: oecd
sources:
  - source-0040#section-2-short-definition
relationships:
  supports: []
  qualifies: []
  contradicts: []
  depends_on: []
created: 2026-07-02
last_reviewed: 2026-07-02
```
