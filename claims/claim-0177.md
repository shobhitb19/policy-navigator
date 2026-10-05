# claim-0177

The Roback spatial-equilibrium framework decomposes a location's attractiveness into two distinct, separately estimable indices: Quality of Life (QL), reflecting how much households value living there net of wages and rents, and Quality of Business (QB), reflecting how much firms value operating there net of wages and rents.

**Source:** [Preston, Maré, Grimes & Donovan (2018)](../sources/source-0030.md) — [Section 2: Roback spatial-equilibrium model — Quality of Life and Quality of Business derivation](../sources/source-0030.md#section-2-roback-model)

> Quality of Life is derived as QL_ct = α·ln(r_ct) − ln(w_ct), with α = 0.2; Quality of Business is derived as QB_ct = [γ/(1−γ)]·ln(r_ct) + ln(w_ct), with γ = 0.11, following Maré and Poot (2018). Both indices are estimated via city/location fixed-effects regressions on quality-adjusted wages (w) and rents (r). (Preston, Maré, Grimes & Donovan, 2018, Section 2)

**Qualifiers:**
- QL and QB are estimated under the assumption that, in equilibrium, households and firms are indifferent between locations once amenity and disamenity values are fully capitalised into local wages and rents.
- The α and γ parameters are calibrated following Maré and Poot (2018) and are specific to this New Zealand application.

**Related:**
- [claim-0178](claim-0178.md) — QL and QB are negatively correlated across New Zealand cities

---

```yaml
claim_id: claim-0177
claim_type: definition
context_tags:
  - new_zealand
  - high_income
mechanism_tags:
  - amenity_value
outcome_tags:
  - livability
  - quality_of_business
policy_lever_tags: []
sources:
  - source-0030#section-2-roback-model
evidence_strength: theoretical
geographic_scope: new_zealand
```
