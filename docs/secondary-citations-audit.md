# Secondary Citations Audit

**Date:** 2026-07-01
**Scope:** All source cards (source-0004 to source-0032) and all claim cards linked from them
**Purpose:** Identify claims where the cited source is itself relaying a finding from a named third party, so the true primary source can be tracked down and either ingested or noted.

A "secondary citation" in this context means: the claim card says "Source: X" but source X's own text reads "According to Y, ..." for the specific finding — the statistical result or empirical claim originates with Y, not X.

---

## Status key

- **ACTION REQUIRED** — primary source not yet in repo; needs to be found and ideally ingested
- **RESOLVABLE** — primary source is already a separate source card in this repo; claim can be re-attributed
- **RESOLVED** — already fixed

---

## Confirmed secondary citations

### source-0005 (Koi Tū / Gluckman et al., 2022)

The source card's own notes state it is "a policy provocation, not a peer-reviewed study — empirical claims in it cite primary sources which should be consulted for methodology details." All four NZ-facing claims it feeds are secondary citations.

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0015 | Auckland workers 11.1% more productive than rest of NZ | Infometrics (2021) | **ACTION REQUIRED** — Infometrics report not in repo; likely proprietary |
| claim-0016 | Auckland = 37.9% of NZ GDP, 35.5% of workforce | Infometrics (2021) | **ACTION REQUIRED** — same Infometrics report |
| claim-0017 | Auckland road congestion costs ~NZ$1.3bn/year | Leung et al. (2017) | **ACTION REQUIRED** — paper not in repo; note: source-0018 separately cites NZIER (2017) for a similar figure, suggesting multiple studies exist |
| claim-0019 (partial) | Nielsen 2018 Quality of Life Survey — Auckland lowest of NZ cities | Nielsen / Auckland Council (2018) | **ACTION REQUIRED** — survey not in repo |

Note: claim-0018 (Auckland PT fares third highest globally) traces through Koi Tū to Greater Auckland (2018), an advocacy organisation whose own source for the ranking is unclear. This needs a second step of investigation even after finding the Greater Auckland post.

---

### source-0006 (OECD, 2015 — The Metropolitan Century)

The OECD report is a synthesis document throughout. Its own notes field names the key underlying studies: Ahrend et al. (2014), Glaeser et al. (2005), Kennedy et al. (2009).

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0022 | Doubling city population → 2–5% increase in GDP per worker | Ahrend et al. (2014) | **RESOLVED** — source-0012 added as co-source; qualifier notes 2015 published version gives 3.8% pooled (1.6–6.3% range) |
| claim-0023 | Doubling municipalities per 100k → 5–6% lower labour productivity | Ahrend et al. (2014) | **RESOLVED** — source-0012 added as co-source; qualifier notes OECD's 5–6% likely reflects the no-governance-body scenario in source-0012 |
| claim-0024 | Metropolitan governance body halves the fragmentation productivity penalty | Ahrend et al. (2014) | **RESOLVED** — source-0012 added as co-source; finding confirmed in source-0012/claim-0056 |
| claim-0027 | Building regulations raise floor-space prices to 2–8× construction costs (central London, Manhattan) | Glaeser et al. (2005) | **ACTION REQUIRED** — Glaeser et al. (2005) not in repo |
| claim-0028 | Per capita ground-transport CO₂ emissions fall consistently as urban density rises | Kennedy et al. (2009) + OECD city data | **ACTION REQUIRED** — Kennedy et al. (2009) not in repo; note OECD also contributes original data here so attribution may be legitimately split |

---

### source-0007 (Collier, Jones & Spijkerman, 2018)

The specific comparative figures in claim-0033 and the African-cities structural claims in claim-0035 are relayed from named third-party studies. The core output elasticity findings in claims-0031, 0032, and 0034 are Collier et al.'s own econometrics and are unaffected.

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0033 | Urban wage premiums: ~45% China, ~122% India, ~176% Brazil; ~6–11% Africa | Chauvin et al. (2016) for large economies; Jones et al. (2017) for Africa | **ACTION REQUIRED** — neither study in repo |
| claim-0035 | Leapfrog patches >40% of African city growth 2000–2010; 40% fewer urban interactions than peers | Lall et al. (2017); Henderson & Nigmatulina (2016) | **ACTION REQUIRED** — neither study in repo |

---

### source-0008 (World Bank WDR 2009, Chapter 7)

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0036 | Atlanta vs Barcelona density/emissions comparison (CO₂, mode share, density figures) | Bertaud (2004); Kenworthy (2005) | **ACTION REQUIRED** — neither source in repo |

---

### source-0009 (Lall et al., 2021 — Pancakes to Pyramids)

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0043 | Density elasticities bundle (wages, patents, pollution, energy, public services) | Ahlfeldt & Pietrostefani (2019) | **RESOLVED** — claim-0043 retired; claims-0195–0199 now correctly attributed to source-0032 |
| claim-0045 | Urban structures persist >150 years; Dar es Salaam 1970s roads closely match current network | Hallegatte (2009); Michaels et al. (forthcoming at time of writing) | **ACTION REQUIRED** — neither source in repo |
| claim-0046 | Near Mexico City metro stations: informality fell 4pp; per $1 metro investment → 20% rise in real incomes | Zarate (2020) | **ACTION REQUIRED** — Zarate (2020) not in repo |

---

### source-0010 (Duranton, 2008 — Engines of Growth)

This is the most systematically secondary source in the set. It is a literature review throughout — every quantitative claim extracted from it is a relay from a named underlying study. The source card's own notes acknowledge this explicitly.

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0047 | Urban primacy increase of 1 SD → ~1.5pp/year reduction in GDP growth | Henderson (2003, *Journal of Economic Growth*) | **ACTION REQUIRED** |
| claim-0048 | Political/institutional factors drive primacy (not trade policy); administrative deregulation most powerful lever | Ades & Glaeser (1995); Nitsch (2006); Davis & Henderson (2003); Henderson, Lee & Lee (2001) | **ACTION REQUIRED** — none of these studies in repo |
| claim-0049 | Chinese cities undersized due to hukou; large income losses; costs of too-small exceed too-large | Au & Henderson (2006a, 2006b) | **ACTION REQUIRED** |
| claim-0050 | Minimum lot-size requirements → squatter settlements; titling effects on economic behaviour | Henderson (2007); Di Tella et al. (2007); Field (2007); De Soto (2000) | **ACTION REQUIRED** |

---

### source-0016 (Walley, 2026) — REMOVED

Source-0016 (Walley, 2026, unpublished working paper) was removed from the repo entirely on 2026-07-02: it only on-referred to primary sources already held. Resolution of its claims:

| Claim | Finding | Resolution |
|---|---|---|
| claim-0068 | Auckland labour productivity premium: 17.9% raw, 13.5% composition-adjusted | **RESOLVED** — re-attributed solely to source-0017 (Maré 2016, the true primary) |
| claim-0069 | NZ urban system concentrated, not polycentric (vs Switzerland/Netherlands) | **DELETED** — true primary (Dijkstra, Poelman & Veneri 2019) not in repo; claim removed rather than left relaying an unpublished source |
| claim-0070 | Housing as productivity enabler — misallocation mechanisms | **RESOLVED** — re-attributed to source-0018 (MHuD 2024); the Nunns (2021) secondary citation below is now also resolved via source-0041 |
| claim-0098 | Auckland ~38% of GDP, ~9% GDP-per-hour premium | **DELETED** — figures were the author's own Stats NZ analysis; stated as personal analysis in the position paper, no claim card needed |

---

### source-0018 (MHuD, 2024 — Housing as Enabler)

MHuD is a government aide-memoire that synthesises external research. All headline quantitative findings it relays have named primary sources.

| Claim | Finding | True primary source | Status |
|---|---|---|---|
| claim-0075 | Full housing reform scenario: 1.1–1.6% output per worker, 3.3–7.2% labour force, 5.0–8.4% GDP | Nunns (2021) | **RESOLVED (2026-07-02)** — Nunns (2019) EPC WP 003, the working-paper version of Nunns (2021), ingested as source-0041; claim-0224 records the WP figures and claim-0075 retains the journal figures with a version note |
| claim-0076 | NZ average agglomeration elasticity ~0.05; doubling employment → ~3.5% per worker | Donovan et al. (2022) | **ACTION REQUIRED** — this appears to be a separate Donovan et al. NZ-specific study, distinct from source-0004 (the 2021 international meta-analysis) |
| claim-0077 | Auckland agglomeration elasticity ~0.04; Auckland 5–8% more productive than secondary cities | Donovan et al. (2022/2024) | **ACTION REQUIRED** — same Donovan NZ study |

---

## Priority order for resolution

**Highest priority** (claims appear in the position paper or are central to the NZ productivity argument):

1. ~~**Nunns (2021)** → claims-0075~~ **RESOLVED (2026-07-02)**: working-paper version ingested as source-0041; also resolves the claim-0066 relay via Blick & Stewart.
2. **Donovan et al. (2022)** → claims-0076/0077, NZ-specific agglomeration elasticities. Separate from source-0004; needs ingestion.
3. **Infometrics (2021)** → claims-0015/0016, Auckland GDP and productivity share. Likely proprietary; if not obtainable, claims should be flagged as "via Koi Tū, citing Infometrics" and kept but noted.
4. **Maré (2016) for claim-0068** → source-0017 is already in repo; this is immediately resolvable with a claim card update.
5. **Ahrend et al. (2014/2015) for claims-0022/0023/0024** → source-0012 is already in repo; verify the specific figures match the 2015 published version before re-attributing.

**Medium priority** (appear in claims library but not yet in position paper draft):

6. Leung et al. (2017) → claim-0017
7. Glaeser et al. (2005) → claim-0027
8. Henderson (2003) → claim-0047; Au & Henderson (2006a/b) → claim-0049
9. Zarate (2020) → claim-0046

**Lower priority** (comparative/illustrative findings, less central to NZ argument):

10. Chauvin et al. (2016); Jones et al. (2017) → claim-0033
11. Bertaud (2004); Kenworthy (2005) → claim-0036
12. Di Tella et al. (2007); Field (2007); De Soto (2000) → claim-0050
13. Hallegatte (2009); Michaels et al. → claim-0045
14. Greater Auckland (2018) → claim-0018 (advocacy source; may not have a cleanly citable primary)

---

## Sources confirmed as primary research (no secondary citation concern)

- **source-0004** (Donovan et al., 2021) — original Bayesian meta-analysis
- **source-0011** (Maré & Graham, 2009) — original NZ LBD empirics
- **source-0012** (Ahrend et al., 2015) — original cross-country OECD FUA regressions
- **source-0013** (Conway & Meehan, 2013) — original NZ productivity statistics
- **source-0015** (Blick & Stewart, 2025) — authors' own benchmarking analysis
- **source-0017** (Maré, 2016) — original two-step TFP estimation using NZ LBD/IDI
- **source-0022** (OECD Skills Matter, 2016) — authors' own PIAAC survey analysis
- **source-0023** (Nunns & Dodge, 2022) — original housing market modelling
- **source-0028** (Javed, Power & Richardson, 2026) — original SVAR econometrics
- **source-0029** (Coleman, Maré & Zheng, 2019) — original NZ city empirics
- **source-0030** (Preston, Maré, Grimes & Donovan, 2018) — original spatial equilibrium estimation
- **source-0031** (Donovan, 2019) — primary dynamic Roback model
- **source-0032** (Ahlfeldt & Pietrostefani, 2019) — primary peer-reviewed meta-analysis
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTEzNDc1NDMwMl19
-->