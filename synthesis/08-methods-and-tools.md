# 08: Methods and Tools

## Summary

Measuring urban phenomena — productivity, accessibility, density, inequality — requires methodological care. City boundary definitions are the most pervasive issue: functional urban areas (defined by commuting zones) produce systematically different estimates from administrative boundaries, because the economic city and the political city are rarely coterminous. Comparing city statistics across countries or over time without controlling for boundary definitions generates spurious differences that look like real productivity variation but reflect measurement inconsistency.

Causal identification of agglomeration effects is the second major challenge. The observed positive correlation between city size and productivity reflects two distinct phenomena: genuine agglomeration economies (the mechanism of interest) and productive workers and firms sorting into larger cities (selection). Untangling these requires either quasi-experimental variation in city size — historical instruments based on geography, early transport networks, or military decisions that are plausibly exogenous to current productivity — or firm and worker fixed effects that absorb the sorting component. NZ evidence applying firm fixed effects finds that 91% of the apparent density-productivity elasticity is compositional: high-productivity workers selecting into dense areas rather than density causally raising productivity. The true causal elasticity (0.015 at firm FE versus 0.171 OLS) is still positive and significant, but is an order of magnitude smaller — and that methodological gap has large implications for how aggressively density policy should be pursued on productivity grounds.

Infrastructure cost modelling faces different challenges. Lifecycle cost accounting — which includes maintenance, renewal, and operating costs over the full asset life — produces dramatically different conclusions from upfront capital cost comparisons. Dispersed development consistently looks cheaper in upfront comparisons (smaller initial pipe runs to the edge, smaller individual buildings) but more expensive in lifecycle comparisons (more lane-km per household to maintain, more pipe-km per dwelling, higher per-trip transit costs as catchment density is lower). Policy decisions based on upfront costs alone systematically understate the fiscal consequences of sprawl. Similarly, accessibility measurement — job catchment areas, transit travel times, network coverage — depends heavily on assumptions about acceptable travel time, mode, and trip purpose. Small methodological differences produce large differences in estimated accessibility levels and in the apparent ranking of investment options.

## Key claim index

- [claim-0001](../claims/claim-0001.md) Agglomeration elasticity estimates — understanding what they measure and how they are identified
- [claim-0011](../claims/claim-0011.md) Spatial scope of measurement matters: metropolitan-scope estimates are lower than national-scope estimates
- [claim-0014](../claims/claim-0014.md) Rigorous controls consistently reduce measured elasticities — raw OLS estimates are upward biased
- [claim-0221](../claims/claim-0221.md) The EU-OECD functional urban area definition: urban centre (1,500/km², 50k) + city (50% rule) + commuting zone (15% rule) (Dijkstra et al. 2019)
- [claim-0222](../claims/claim-0222.md) FUAs capture agglomeration economies and full labour markets better than administrative boundaries, which bias international comparisons (Dijkstra et al. 2019)

## Key methodological issues

- **City boundary definitions**: functional urban areas (commuting zones) vs. administrative boundaries produce systematically different estimates.
- **Causal identification**: OLS estimates of agglomeration effects are upward biased by sorting; quasi-experimental methods using historical instruments are preferred but difficult to implement.
- **Infrastructure cost modelling**: lifecycle cost accounting vs. upfront capital cost comparisons can produce very different conclusions.
- **Accessibility measurement**: job catchment areas depend heavily on assumptions about travel time, mode, and purpose.

## Key themes

### The boundary problem
No two analyses of urban productivity or density use exactly the same city boundaries. Some use the municipality (legal city), some use the statistical metropolitan area, some use functional urban areas defined by commuting flows. These choices are not merely cosmetic: the municipality is typically far smaller than the functional urban area (the commuting zone captures the actual economic unit), so municipality-level density understates true urban density, and municipality-level productivity comparisons mix urban and rural areas within administrative boundaries. This is why international city comparisons require careful attention to whether the source has applied consistent boundary definitions or is comparing apples to oranges.

### Sorting versus agglomeration
The sorting-vs-agglomeration problem is fundamental. Dense cities attract productive workers and firms; productive workers and firms make cities appear more productive. Without controlling for who is in the city, you cannot separate "density causes productivity" from "productive people choose density." The gold standard is either panel data with worker or firm fixed effects (which absorbs individual characteristics across moves) or quasi-experimental instruments for city size (typically historical geography, early rail networks, or administrative decisions that are plausibly unrelated to current productivity). In practice, both approaches have limitations: fixed effects panels require workers who move between cities (a selected sample), and instruments require defending the exclusion restriction. NZ agglomeration research has applied firm FE (Maré & Graham 2009) and found dramatic attenuation from OLS to FE estimates — a pattern consistent with international evidence.

### What the methods imply for policy
The methodological lesson is not that agglomeration effects are illusory — they are real and replicable — but that the OLS magnitudes used to motivate large policy interventions are inflated. The policy-relevant question is not "what is the elasticity in an OLS regression?" but "what productivity gain would a specific policy change — a given zoning reform, a given transit investment — produce for a given set of workers and firms?" That requires either a quasi-experimental evaluation of the specific intervention or a structural model calibrated to local conditions. Generic application of global meta-analytic elasticities to NZ policy choices overstates expected returns.

## Key levers

- Evidence assessment: all lever pages

## Open questions

- What data infrastructure is needed to track functional urban area performance in real time?
- How should cities measure and report on spatial inequality?
- What is the right unit for urban productivity measurement: the city, the neighbourhood, or the firm?
