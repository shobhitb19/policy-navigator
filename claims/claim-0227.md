# claim-0227

Firm selection does not explain the productivity advantage of larger cities: French establishment-level data show no sizeable differences in left-truncation of the firm productivity distribution between denser and less-dense areas — instead the entire distribution is right-shifted in denser areas, indicating agglomeration economies that benefit all firms rather than tougher competition culling weak ones.

**Source:** [Combes et al. (2012)](../sources/source-0042.md) — [Main findings](../sources/source-0042.md#section-1-main-findings)

> "There are no sizeable differences in left truncation between denser and less dense employment areas, indicating that selection does not play a major role in explaining the productive advantages of urban density. Instead, the entire log productivity distribution in denser areas is right-shifted relative to the distribution in less dense areas." (Combes et al., 2012, pp. 3–4)

**Qualifiers:**
- The test exploits a sharp distributional prediction from a nested model: selection left-truncates the productivity distribution, agglomeration right-shifts and dilates it.
- "Selection" here means the inability of weak firms to survive tougher competition in larger markets — distinct from *sorting* (productive firms and workers choosing large cities), which the paper does not test and which NZ evidence (claim-0052) finds substantial.
- Result is robust across sectors, city size thresholds, establishment samples, estimation techniques, and spatial unit definitions; based on French data, so the NZ application is by analogy.
- The paper does not adjudicate among the agglomeration channels (sharing, matching, learning) or address endogeneity of city scale.

**Related:**
- [claim-0228](claim-0228.md) — the dilation finding: top-quartile firms gain ~3× more from density than bottom-quartile
- [claim-0052](claim-0052.md) — 91% of the apparent NZ density-productivity elasticity is worker/firm sorting
- [claim-0001](claim-0001.md) — meta-analytic agglomeration elasticities

---

```yaml
claim_id: claim-0227
claim_type: causal_association
scope:
  spatial: metropolitan
  sectoral: economy-wide
context_tags:
  - europe
  - high_income
  - OECD
mechanism_tags:
  - agglomeration
  - sorting
outcome_tags:
  - productivity
policy_lever_tags:
  - land_use_planning
evidence_strength: econometric
geographic_scope: france
sources:
  - source-0042#section-1-main-findings
relationships:
  supports: []
  qualifies:
    - claim-0052
  contradicts: []
  depends_on: []
created: 2026-07-03
last_reviewed: 2026-07-03
```
