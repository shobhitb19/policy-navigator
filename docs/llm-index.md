# LLM Retrieval Index

This page is designed for LLM navigation. It lists every page in the wiki with direct links. Read the synthesis hub for the topic you need, then follow links to individual claim pages. Each claim is self-contained with evidence, qualifiers, and relationship links to related claims.

## How to retrieve selectively

1. **Choose a synthesis hub** below that matches your topic — each hub has a thematic summary and a curated claim index.
2. **Follow claim links** from the hub to individual claim pages. Each claim page has: one-sentence assertion, source citation, supporting quotation, qualifiers, and a YAML block with `mechanism_tags`, `outcome_tags`, `policy_lever_tags`, and `relationships`.
3. **Use the YAML `relationships` block** to traverse the evidence graph — `supports`, `qualifies`, `contradicts`, and `depends_on` fields name related claim IDs. Fetch those pages to expand context.
4. **Check evidence strength** in the YAML: `meta_analysis > rct > quasi_experimental > observational > expert_review`.
5. **Fetch source pages** for full bibliographic detail and section anchors.

---

## Synthesis hubs

| Hub | Topic |
|---|---|
| [01 Urbanisation and Spatial Systems](../synthesis/01-urbanisation-and-spatial-systems.md) | Urbanisation patterns, spatial structure, urban primacy, NZ monocentrism |
| [02 Agglomeration and Productivity](../synthesis/02-agglomeration-and-productivity.md) | Agglomeration economies, density effects, wage elasticities |
| [03 Governance and Institutions](../synthesis/03-governance-and-institutions.md) | Metropolitan governance, coordination failures, fragmentation |
| [04 Land Markets, Zoning, Urban Form](../synthesis/04-land-markets-zoning-urban-form.md) | Zoning, land supply, housing affordability, NZ reform |
| [05 Transport and Accessibility](../synthesis/05-transport-and-accessibility.md) | Transport investment, labour market catchment, Auckland |
| [06 Inclusion and Division](../synthesis/06-inclusion-and-division.md) | Inequality, informal settlements, targeted programs |
| [07 Resilience, Environment, Sustainability](../synthesis/07-resilience-environment-sustainability.md) | Climate resilience, emissions, urban sustainability |
| [08 Methods and Tools](../synthesis/08-methods-and-tools.md) | Measurement, econometrics, data sources |
| [09 Demographics and Population Strategy](../synthesis/09-demographics-and-population-strategy.md) | Demographics, migration, NZ population strategy |

---

## All claim pages

### Donovan et al. (2021) — Agglomeration meta-analysis

| Claim | Summary |
|---|---|
| [claim-0001](../claims/claim-0001.md) | Doubling city size → 2.7–6.4% wage/productivity gain (median 4.6%) |
| [claim-0011](../claims/claim-0011.md) | Metropolitan-scale elasticity median 3.3% vs national-scale 6.4% |
| [claim-0012](../claims/claim-0012.md) | Agglomeration estimates in production peaked 1980–2000 and have since declined |
| [claim-0013](../claims/claim-0013.md) | Manufacturing elasticity ~0.6pp lower than economy-wide |
| [claim-0014](../claims/claim-0014.md) | More rigorous controls reduce estimates; OLS is upward biased |

### Gluckman et al. (2022) — Reimagining Auckland

| Claim | Summary |
|---|---|
| [claim-0015](../claims/claim-0015.md) | Auckland workers 11.1% more productive than rest-of-NZ |
| [claim-0016](../claims/claim-0016.md) | Auckland: 37.9% of NZ GDP with 35.5% of workforce |
| [claim-0017](../claims/claim-0017.md) | Auckland road congestion costs ~NZ$1.3bn/year |
| [claim-0018](../claims/claim-0018.md) | Auckland PT fares globally third highest (2018) |
| [claim-0019](../claims/claim-0019.md) | Auckland's economic footprint justifies asymmetric national investment |
| [claim-0020](../claims/claim-0020.md) | NZ cities underperform peers on density, mixed use, transit |

### OECD (2015) — The Metropolitan Century

| Claim | Summary |
|---|---|
| [claim-0021](../claims/claim-0021.md) | OECD metro areas: ~4% of land, ~50% of population, ~55% of GDP |
| [claim-0022](../claims/claim-0022.md) | Doubling city population → 2–5% higher GDP per worker (OECD analysis, primary: Ahrend et al. 2015) |
| [claim-0023](../claims/claim-0023.md) | Doubling municipalities per 100k in a metro → 5–6% lower labour productivity |
| [claim-0024](../claims/claim-0024.md) | Metropolitan governance body reduces the fragmentation-productivity penalty by ~50% |
| [claim-0025](../claims/claim-0025.md) | Metros with governance: declining sprawl 2000–2006; without: increasing |
| [claim-0026](../claims/claim-0026.md) | Dedicated transport authority → 14pp higher PT satisfaction |
| [claim-0027](../claims/claim-0027.md) | Floor-space prices in central London and Manhattan 2–8x construction costs |
| [claim-0028](../claims/claim-0028.md) | Per capita ground-transport CO₂ falls consistently as urban density rises; compact cities emit substantially less |
| [claim-0029](../claims/claim-0029.md) | Halving travel time city–hinterland → 0.2–0.4pp higher annual GDP growth |
| [claim-0030](../claims/claim-0030.md) | OECD metro areas (500k+) contributed ~50% of OECD GDP growth 2000–2010 |

### Collier et al. (2018) — African cities

| Claim | Summary |
|---|---|
| [claim-0031](../claims/claim-0031.md) | Developing-country cities: 5–6% productivity gain per doubling of population |
| [claim-0032](../claims/claim-0032.md) | African cities: agglomeration effect insignificant once infrastructure quality controlled |
| [claim-0033](../claims/claim-0033.md) | African cities: ~40% fewer potential interactions due to leapfrog development |
| [claim-0034](../claims/claim-0034.md) | Formal employment more than doubles with each doubling of market potential within 10km |
| [claim-0035](../claims/claim-0035.md) | Leapfrog development >40% of built-up growth in major African cities 2000–2010 |

### World Bank WDR (2009) — Inclusive Urbanisation

| Claim | Summary |
|---|---|
| [claim-0036](../claims/claim-0036.md) | Three-dimensional development: density, distance, division framework |
| [claim-0037](../claims/claim-0037.md) | Mumbai FSI restriction (1.33) → 4 sq m per person, 54% in slums |
| [claim-0038](../claims/claim-0038.md) | Land use reform more cost-effective than direct housing subsidies |
| [claim-0039](../claims/claim-0039.md) | Spatial policies must address all three dimensions simultaneously |
| [claim-0040](../claims/claim-0040.md) | Bogotá TransMilenio BRT: average travel time −15 minutes, larger gains for poor |

### Lall et al. (2021) — Pancakes to Pyramids

| Claim | Summary |
|---|---|
| [claim-0041](../claims/claim-0041.md) | Doubling income → +29% floor space per person; doubling population → −40% |
| [claim-0042](../claims/claim-0042.md) | Low-income cities: almost entirely horizontal; vertical layering is income-driven |
| [claim-0195](../claims/claim-0195.md)–[claim-0199](../claims/claim-0199.md) | Doubling density: +4% wages, +21% patents, −7% energy, **+13% pollution (corrected sign)**, −17% unit cost of local services (claim-0043 retired) |
| [claim-0044](../claims/claim-0044.md) | Urban containment without infill converts sprawl problem into restriction problem |
| [claim-0045](../claims/claim-0045.md) | Urban structures last 150+ years; early infrastructure determines form for generations |
| [claim-0046](../claims/claim-0046.md) | Mexico City metro: informality −4pp near stations; $1 invested → 20% real income gain |

### Duranton (2008) — Cities as Engines of Growth

| Claim | Summary |
|---|---|
| [claim-0047](../claims/claim-0047.md) | Urbanisation alone doesn't affect GDP growth; 15pp primacy increase → −1.5pp annual growth |
| [claim-0048](../claims/claim-0048.md) | Polycentric urban systems outperform monocentric at comparable national income |
| [claim-0049](../claims/claim-0049.md) | Exclusionary zoning causes squatter settlement growth; removing it lowers living costs |
| [claim-0050](../claims/claim-0050.md) | City specialisation and competition between cities drives national productivity |

### Maré & Graham (2009) — NZ Agglomeration Elasticities

| Claim | Summary |
|---|---|
| [claim-0051](../claims/claim-0051.md) | NZ agglomeration elasticity: 3–5% productivity gain per doubling of employment density |
| [claim-0052](../claims/claim-0052.md) | NZ elasticity consistent with international estimates but at lower end |
| [claim-0053](../claims/claim-0053.md) | Agglomeration effects in NZ strongest in high-skill service sectors |
| [claim-0054](../claims/claim-0054.md) | Worker sorting explains a significant share of observed urban wage premiums |

### Ahrend et al. (2015) — What Makes Cities Productive?

| Claim | Summary |
|---|---|
| [claim-0055](../claims/claim-0055.md) | Labour productivity 10–15% higher in OECD metro areas than non-metro |
| [claim-0056](../claims/claim-0056.md) | Doubling municipalities in a metro → 3.2% lower productivity; no governance body → ~6% penalty |
| [claim-0057](../claims/claim-0057.md) | Metropolitan governance quality matters more than city size for productivity |
| [claim-0058](../claims/claim-0058.md) | Integrated transport governance associated with higher PT mode share |

### Conway & Meehan (2013) — NZ Productivity

| Claim | Summary |
|---|---|
| [claim-0059](../claims/claim-0059.md) | NZ productivity gap vs OECD frontier is large and persistent |
| [claim-0060](../claims/claim-0060.md) | NZ underinvestment in physical and knowledge capital relative to peers |
| [claim-0061](../claims/claim-0061.md) | NZ's small, remote market limits competition intensity and technology diffusion |

### NZ Productivity Commission (2023)

| Claim | Summary |
|---|---|
| [claim-0062](../claims/claim-0062.md) | NZ multifactor productivity growth has slowed significantly since 2000 |
| [claim-0063](../claims/claim-0063.md) | Low management quality is a significant drag on NZ firm productivity |
| [claim-0064](../claims/claim-0064.md) | NZ resource allocation across firms is less efficient than comparable economies |

### Auckland Council Chief Economist (2025)

| Claim | Summary |
|---|---|
| [claim-0065](../claims/claim-0065.md) | Auckland GDP per capita only 13% above national average vs 25–35% typical for primate cities |
| [claim-0066](../claims/claim-0066.md) | Restrictive Auckland land use reduced NZ GDP 0.9–1.8% via spatial misallocation |
| [claim-0067](../claims/claim-0067.md) | Auckland congestion costs ~$0.7bn/year (~0.5% of Auckland GDP) |
| [claim-0226](../claims/claim-0226.md) | Auckland: 38% of national GDP, $157bn (YE March 2024), but only 9% GDP-per-hour premium |

### Maré (2016) — Urban Productivity Estimation

| Claim | Summary |
|---|---|
| [claim-0068](../claims/claim-0068.md) | Auckland firm labour productivity 17.9% above other NZ urban areas; 13.5% after industry composition adjustment |
| [claim-0071](../claims/claim-0071.md) | Worker sorting accounts for ~half of observed urban wage premium in NZ |
| [claim-0072](../claims/claim-0072.md) | True agglomeration effect in NZ remains significant after sorting controls |
| [claim-0073](../claims/claim-0073.md) | NZ agglomeration effects stronger for high-skill workers |
| [claim-0074](../claims/claim-0074.md) | Firm-level learning effects persist when workers move from dense to less-dense areas |

### MHuD (2024) — Housing and Productivity

| Claim | Summary |
|---|---|
| [claim-0070](../claims/claim-0070.md) | Housing/land constraints reduce productivity via misallocation — workers and firms cannot sort into high-productivity locations |
| [claim-0075](../claims/claim-0075.md) | Removing all NZ housing supply constraints: output/worker +1.1–1.6%, GDP +5.0–8.4% |
| [claim-0076](../claims/claim-0076.md) | NZ housing costs absorb disproportionate share of income for low-income households |
| [claim-0077](../claims/claim-0077.md) | Infrastructure funding gap is primary constraint on housing supply reform in NZ |
| [claim-0078](../claims/claim-0078.md) | NZ housing stock ~$1.6 trillion ≈ 4× GDP (was ~2× in 1990s) |

### Winter et al. (2025) — Innovation and Capital in NZ

| Claim | Summary |
|---|---|
| [claim-0079](../claims/claim-0079.md) | NZ capital intensity well below OECD frontier; investment rate insufficient to close gap |
| [claim-0080](../claims/claim-0080.md) | NZ firms using fully up-to-date technology declined from 51% (2007) to 44% (2022) |
| [claim-0081](../claims/claim-0081.md) | Technology diffusion from frontier to laggard firms is slower in NZ than peers |
| [claim-0082](../claims/claim-0082.md) | NZ innovation investment concentrated in few large firms; SME innovation rate low |
| [claim-0083](../claims/claim-0083.md) | R&D tax credit uptake in NZ lower than comparable OECD economies |
| [claim-0084](../claims/claim-0084.md) | NZ skills mismatch contributes to capital underutilisation and low innovation rate |

### Committee for Auckland et al. (2025) — State of the City 2025

| Claim | Summary |
|---|---|
| [claim-0085](../claims/claim-0085.md) | Auckland GDP growth underperformed Sydney, Melbourne, Wellington 2015–2024 |
| [claim-0086](../claims/claim-0086.md) | Auckland productivity premium over NZ average only ~15% vs 30–40% for comparable primate cities |
| [claim-0087](../claims/claim-0087.md) | Auckland housing completions per capita now exceed peer city average by 60% |
| [claim-0088](../claims/claim-0088.md) | Auckland labour force participation rate lower than Sydney and Melbourne |
| [claim-0089](../claims/claim-0089.md) | Auckland now top-third globally for new homes completed per capita |
| [claim-0090](../claims/claim-0090.md) | Auckland infrastructure backlog estimated at $30bn+ |

### Lala, Spoonley & Gluckman (2026) — Koi Tū Population Strategy

| Claim | Summary |
|---|---|
| [claim-0091](../claims/claim-0091.md) | NZ total fertility rate reached 1.55 in 2025, well below replacement rate of 2.1 |
| [claim-0092](../claims/claim-0092.md) | NZ population growth slowed sharply: 1.7%/year (2023–24) to 0.7%/year (2024–25) |
| [claim-0093](../claims/claim-0093.md) | BusinessNZ projects 250,000 labour shortage by 2045; LFPR to fall 70.5% (2021) → 63.22% (2073) |
| [claim-0094](../claims/claim-0094.md) | NZ GTCI rank fell 11th → 18th since 2015; 2024 net emigration of NZ citizens ~44,000, largest in 25 years |
| [claim-0095](../claims/claim-0095.md) | NZS cost to rise 5.1% → 8% of GDP by 2065; worker:retiree ratio 7:1 (1960s) → 4:1 (2025) → 2:1 (2065) |
| [claim-0096](../claims/claim-0096.md) | Auckland to be majority non-Pākehā before early 2040s: 42% Asian, 45% NZ European by 2043 |
| [claim-0097](../claims/claim-0097.md) | Auckland's ethnic minority communities contributed ~$50bn to Auckland's GDP in 2023 |

### OECD (2016) — Skills Matter

| Claim | Summary |
|---|---|
| [claim-0099](../claims/claim-0099.md) | ~22% of OECD workers overqualified; ~13% underqualified; ~40% in unrelated occupation |
| [claim-0100](../claims/claim-0100.md) | Skills mismatch reduces individual earnings by 10–20% |
| [claim-0101](../claims/claim-0101.md) | Mismatch rates higher in countries with rigid wage-setting and weak firm-level bargaining |
| [claim-0102](../claims/claim-0102.md) | Urban areas have lower mismatch rates than rural areas within the same country |
| [claim-0103](../claims/claim-0103.md) | Mismatch is persistent: half of mismatched workers remain mismatched after 5 years |
| [claim-0104](../claims/claim-0104.md) | Higher literacy/numeracy proficiency reduces mismatch probability |
| [claim-0105](../claims/claim-0105.md) | Employer-provided training strongly reduces mismatch risk |

### Nunns & Dodge (2022) — Te Waihanga: Decline of Housing Supply in NZ

| Claim | Summary |
|---|---|
| [claim-0106](../claims/claim-0106.md) | NZ housing supply elasticity declined 1/4 to 1/3 between mid-century and recent decades |
| [claim-0107](../claims/claim-0107.md) | 1% population rise → ~0.5% price rise (mid-century) vs ~2.0% (recent decades): fourfold increase |
| [claim-0108](../claims/claim-0108.md) | Auckland 1970 District Scheme halved housing capacity (475k→250k); FAR fell 1.28→0.80 |
| [claim-0109](../claims/claim-0109.md) | Auckland travel speeds +50% (1930s–1990s) then −1/3 by 2010s due to congestion |
| [claim-0110](../claims/claim-0110.md) | Avoiding 1970s downzoning + speed decline would have cut 1978–2018 price growth by ~70% |
| [claim-0111](../claims/claim-0111.md) | New road capacity induces demand; congestion pricing + new transport options more effective |
| [claim-0112](../claims/claim-0112.md) | RMA 1991 removed infrastructure planning requirements, decoupling development from provision |

### Kanoa RD (2026) — Population shifts

| Claim | Summary |
|---|---|
| [claim-0113](../claims/claim-0113.md) | NZ population grew 27.3% over 2006–2025 (4.18m → 5.32m) |
| [claim-0114](../claims/claim-0114.md) | Without international migration Auckland's population would have declined in 2024–25; internal out-migrants go primarily to Waikato, Northland, Bay of Plenty, Canterbury |
| [claim-0115](../claims/claim-0115.md) | Only the "golden triangle" (Auckland, Hamilton, Tauranga) grew faster than the national rate 2006–2025; Auckland added ~443,000 people |
| [claim-0116](../claims/claim-0116.md) | Selwyn District grew 151% and Queenstown Lakes 123% over 2006–2025; four of the ten fastest-growing TLAs were in Auckland |
| [claim-0117](../claims/claim-0117.md) | Year to June 2025: NZ grew by 34,700 (natural increase 21,000, net migration 13,700); 21 of 88 TLAs had natural population decrease |

### Te Waihanga (2026) — National Infrastructure Plan 2026

| Claim | Summary |
|---|---|
| [claim-0118](../claims/claim-0118.md) | NZ spent ~5.8% of GDP/year on infrastructure over 20 years (top OECD spender) but ranks near the bottom of the OECD for efficiency |
| [claim-0119](../claims/claim-0119.md) | Forward Guidance: infrastructure spending to rise from ~$20bn/year now to >$40bn/year by the 2050s, ~60% toward renewals — updates the earlier ~$30bn estimate |
| [claim-0120](../claims/claim-0120.md) | Consenting costs ~$1.3bn/year — ~5.5% of construction cost, up to 16% of project budgets |
| [claim-0121](../claims/claim-0121.md) | NZ has 1,175 land-use zones across 67 territorial authorities vs. Japan's 13 |
| [claim-0122](../claims/claim-0122.md) | NZ has >$330bn of existing infrastructure assets, mostly built post-1950, now reaching end of usable life |
| [claim-0123](../claims/claim-0123.md) | Infrastructure ownership: Commercial/Private 44% (~$10bn), Local Government 31% (~$7.1bn), Central Government 25% (~$5.8bn) |
| [claim-0124](../claims/claim-0124.md) | NZ infrastructure spend ~$5,000 per person in 2022 (2025 NZD) |
| [claim-0125](../claims/claim-0125.md) | Auckland modelling: time-of-use road charging could cut excess congestion delay ~35% with ~20% less new capital investment needed |
| [claim-0126](../claims/claim-0126.md) | Priority recommendation: upzone around key transport corridors so more people benefit from and pay for existing infrastructure capacity |
| [claim-0127](../claims/claim-0127.md) | Infrastructure Victoria (Australia): servicing a home costs ~AU$59,000 (~NZ$68,000) more in a dispersed city than a compact one |

### NZ Government (2026) — Government Response to the National Infrastructure Plan

| Claim | Summary |
|---|---|
| [claim-0128](../claims/claim-0128.md) | NZ Government "Supported" or "Supported In-Principle" all 16 NIP recommendations |
| [claim-0129](../claims/claim-0129.md) | NZ's 2026 Plan is its fourth infrastructure plan since 2010; some recommendations are identical to those from over a decade earlier |
| [claim-0130](../claims/claim-0130.md) | NZ spent ~5.8% of GDP/year on infrastructure over 20 years but ranks near bottom of OECD for efficiency (Government Response framing) |
| [claim-0131](../claims/claim-0131.md) | Treasury commits to using Te Waihanga's Forward Guidance as a regular input to medium-term fiscal/capital allowance advice |
| [claim-0132](../claims/claim-0132.md) | Rec 12 response: centrally-led regional spatial planning aligning LTMA/LGA funding, contingent on the Natural Environment Bill/Planning Bill |
| [claim-0133](../claims/claim-0133.md) | Multi-year budgeting recommendation only "Supported in-principle" — Government argues existing annual-appropriations system already has adequate multi-year features |
| [claim-0134](../claims/claim-0134.md) | Gas Transition Loan Guarantee Scheme, up to $1.2bn, announced for Budget 2026 (Rec 14 response) |
| [claim-0135](../claims/claim-0135.md) | Green Party: GPS on Land Transport 2024–2027 favours new state highway capex over renewals/maintenance, at odds with NIP Recommendations 1, 2, 7, 13 |

### NZ Productivity Commission (2022) — Immigration: Fit for the Future

| Claim | Summary |
|---|---|
| [claim-0136](../claims/claim-0136.md) | "Absorptive capacity" defined: infrastructure, housing, health/education services, community infrastructure — not fixed long-run but constrains short-run accommodation of growth |
| [claim-0137](../claims/claim-0137.md) | NZ infrastructure gap estimated at $104bn, plus a further $106bn future gap over 30 years |
| [claim-0138](../claims/claim-0138.md) | "Brain exchange": 40% of NZ's tertiary-educated residents are immigrants vs. 21% of NZ citizens offshore being tertiary-educated |
| [claim-0139](../claims/claim-0139.md) | Skilled temporary visa categories have grown less skilled since 2012, with rising approvals at ANZSCO levels 4–5 |
| [claim-0140](../claims/claim-0140.md) | NZ produced US$68/hour worked in 2019/20 vs. OECD average US$85 |
| [claim-0141](../claims/claim-0141.md) | NZ's GDP growth kept pace with OECD peers via more workers/hours, not higher output per hour |
| [claim-0142](../claims/claim-0142.md) | Migration may suppress wages in some sectors, reinforcing a low-skill, low-wage labour market trap |
| [claim-0143](../claims/claim-0143.md) | Returns to education in NZ are among the lowest in the OECD and declining |
| [claim-0144](../claims/claim-0144.md) | Tying migrant visas to a single employer increases monopsony power, suppressing wages and mobility |
| [claim-0145](../claims/claim-0145.md) | Recommendation: enable migrant job mobility across accredited employers under the AEWV |
| [claim-0146](../claims/claim-0146.md) | Skill Shortage Lists are backward-looking and prone to lobbying |
| [claim-0147](../claims/claim-0147.md) | Recommendation: favour wage-based scarcity signals over shortage lists, reviewed biennially |
| [claim-0148](../claims/claim-0148.md) | Central recommendation: a statutory Government Policy Statement tying visa settings to absorptive capacity |
| [claim-0149](../claims/claim-0149.md) | NZ had 1 Labour Inspectorate inspector per 40,000 workers vs. ILO benchmark of 1:10,000 |
| [claim-0150](../claims/claim-0150.md) | Te Tiriti o Waitangi has been largely disconnected from immigration policy; Crown-Māori engagement recommended |
| [claim-0151](../claims/claim-0151.md) | NZ ranks top-10 on MIPEX, yet more settlement-support resourcing recommended |
| [claim-0152](../claims/claim-0152.md) | Skilled migrants contribute to firm productivity similarly to high-skilled NZ-born workers |
| [claim-0153](../claims/claim-0153.md) | MBIE estimate: 8% (~20,000) of temporary migrant workers experienced rights violations or exploitation (2018 Migrant Survey) |
| [claim-0154](../claims/claim-0154.md) | Immigration is neither cause nor solution to NZ's productivity challenge — GDP growth driven by more workers/hours, not higher output per hour |

### Javed, Power & Richardson (2026) — Migration and the New Zealand economy

| Claim | Summary |
|---|---|
| [claim-0155](../claims/claim-0155.md) | NZ immigrant population share rose from 15% (1990) to 27% (2019), second only to Australia among comparators |
| [claim-0156](../claims/claim-0156.md) | Expansionary immigration shock → significant fall in unemployment rate, lasting ~18 months |
| [claim-0157](../claims/claim-0157.md) | Expansionary immigration shock → real GDP +0.4% at 6 months, significant ~18 months |
| [claim-0158](../claims/claim-0158.md) | Expansionary immigration shock → participation rate +0.10% on impact, significant >1 year |
| [claim-0159](../claims/claim-0159.md) | Expansionary immigration shock → real wages −0.18% on impact, likely positive long-term |
| [claim-0160](../claims/claim-0160.md) | Headline CPI unaffected; non-tradable prices rise significantly ~1 year after shock |
| [claim-0161](../claims/claim-0161.md) | Expansionary immigration shock → significant increases in house prices and household credit |
| [claim-0162](../claims/claim-0162.md) | Labour productivity shows muted response to immigration shock, corroborating NZPC (2022) |
| [claim-0163](../claims/claim-0163.md) | FEVD: immigration shock explains ~30% of GDP and unemployment variation at 3-year horizon |
| [claim-0164](../claims/claim-0164.md) | FEVD: immigration shock explains <10% of labour productivity variation, smallest of any variable |
| [claim-0165](../claims/claim-0165.md) | Younger (15-29) immigrant shock → significant fall in unemployment and tradable prices |
| [claim-0166](../claims/claim-0166.md) | Older (30-44) immigrant shock → labour productivity rises significantly ~1 year after shock |

### Coleman, Maré & Zheng (2019) — New jobs, old jobs: The evolution of work in New Zealand's cities

| Claim | Summary |
|---|---|
| [claim-0167](../claims/claim-0167.md) | NZ manufacturing employment share fell from 25% (1976) to <10% (2013) |
| [claim-0168](../claims/claim-0168.md) | Structural shift to services favoured large cities: 2/3 of finance-sector jobs growth 1976–2013 went to Auckland (which held ~1/3 of sector employment at the start) |
| [claim-0169](../claims/claim-0169.md) | Auckland captured 79% of national wholesale-employment growth 1976–2013 vs. 56% expected from its initial share |
| [claim-0170](../claims/claim-0170.md) | Slow-growing and small NZ cities show higher excess job churn; regression on 65 industries, 30 urban areas: −0.27 on log city growth, −0.017 on log city size (R²=0.80) |
| [claim-0171](../claims/claim-0171.md) | Negative shock to regionally specialised manufacturing → net 36-job loss per 100 jobs shocked; widespread manufacturing → net 60-job gain elsewhere |
| [claim-0172](../claims/claim-0172.md) | Negative shock to a city's primary sector is amplified: 100-job forecast loss → 108 total jobs lost, with no compensating expansion elsewhere |
| [claim-0173](../claims/claim-0173.md) | Initial industry mix explains only ~10% of cross-city employment growth differences 1976–2013; local within-industry performance explains the rest |
| [claim-0174](../claims/claim-0174.md) | NZ cities diversified rather than specialised 1976–2013: 23 of 30 urban areas saw Regional Specialisation Index decline |
| [claim-0175](../claims/claim-0175.md) | Long-run structural shift toward services has structurally favoured large cities via agglomeration; authors judge this unlikely to be reversed by regional policy |
| [claim-0176](../claims/claim-0176.md) | Productivity improvements in non-tradeable (local-serving) businesses produce more distributed regional benefits than sector- or place-specific interventions |

### Preston, Maré, Grimes & Donovan (2018) — Amenities and the attractiveness of NZ cities

| Claim | Summary |
|---|---|
| [claim-0177](../claims/claim-0177.md) | Roback framework separates Quality of Life (household welfare net of wages/rents) from Quality of Business (firm value net of wages/rents) across NZ cities |
| [claim-0178](../claims/claim-0178.md) | QL and QB are substantially negatively correlated across NZ cities (r = −0.57); only Christchurch, Tauranga, and Queenstown rank above average on both |
| [claim-0179](../claims/claim-0179.md) | 1 SD more rainfall → −0.27 SD Quality of Life; 1 SD more sunshine hours → +0.21 SD Quality of Life |
| [claim-0180](../claims/claim-0180.md) | Coastal/waterfront location → +0.36 SD Quality of Life, consistent across both periods studied |
| [claim-0181](../claims/claim-0181.md) | Education share unrelated to QL in 1976–1991; by 1996–2013 a 1 SD increase in education → +0.27 SD QL |
| [claim-0182](../claims/claim-0182.md) | 10% population growth → −0.09 SD QL (congestion disamenity), a relationship that weakened in 1996–2013 |
| [claim-0183](../claims/claim-0183.md) | 10% population growth → +0.1 SD Quality of Business, significant in both periods |
| [claim-0184](../claims/claim-0184.md) | High education/health workforce shares → lower Quality of Business (1 SD increase in education share → −0.43 SD QB; health → −0.37 SD QB) |
| [claim-0185](../claims/claim-0185.md) | Households and firms prefer systematically different NZ locations: households favour sunny, coastal cities (high QL); firms favour large cities (high QB) |

### Donovan (2019) — Triumph of the high-amenity city?

| Claim | Summary |
|---|---|
| [claim-0186](../claims/claim-0186.md) | In equilibrium, people migrate to cities until private agglomeration benefits of city size equal marginal congestion costs |
| [claim-0187](../claims/claim-0187.md) | Agglomeration economies arise from three sources: Matching (thicker labour markets), Sharing (split input costs), and Learning (knowledge spillovers); vary by sector and skill level |
| [claim-0188](../claims/claim-0188.md) | Congestion is a negative externality disproportionately afflicting publicly-provided goods (transport, education, recreation) where price signals are weak |
| [claim-0189](../claims/claim-0189.md) | Climate explains ~25% of variation in NZ location amenities; Tauranga and Auckland have the best climates among major cities |
| [claim-0190](../claims/claim-0190.md) | Policies that restrict urban development raise rents and lower wages simultaneously — squeezing workers on two fronts |
| [claim-0191](../claims/claim-0191.md) | NZ housing stock adjusts slowly to demand changes ("sticky quantities" — adjustment frictions present) |
| [claim-0192](../claims/claim-0192.md) | Urban development generates positive regional spillovers — development in one location can raise welfare in surrounding locations |
| [claim-0193](../claims/claim-0193.md) | Strong positive agglomeration economies differ by channel and skill: production benefits favour high-skilled workers; consumption benefits accrue to both |
| [claim-0194](../claims/claim-0194.md) | "Amenable City" framing proposed: cities that deliver valued household and firm amenity bundles, acknowledging pricing failures and heterogeneous preferences |

### Ahlfeldt & Pietrostefani (2019) — The economic effects of density: A synthesis

| Claim | Summary |
|---|---|
| [claim-0195](../claims/claim-0195.md) | Doubling urban density → ~4% higher wages in high-income countries; ~8% in non-high-income countries (causal interpretation judged justifiable) |
| [claim-0196](../claims/claim-0196.md) | Doubling urban density → ~21% more patent activity (citation-weighted; combines genuine spillovers and sorting) |
| [claim-0197](../claims/claim-0197.md) | Doubling urban density → ~7% lower energy consumption (associative) |
| [claim-0198](../claims/claim-0198.md) | Doubling urban density → ~13% higher local pollution concentration (not lower; causal IV evidence) |
| [claim-0199](../claims/claim-0199.md) | Doubling urban density → ~17% lower unit costs of local public services (associative) |

### Jaffe, Trajtenberg & Henderson (1993) — Geographic localisation of knowledge spillovers

| Claim | Summary |
|---|---|
| [claim-0200](../claims/claim-0200.md) | Within the US, a patent is ~5–10× more likely to cite a same-MSA patent than predicted by the geographic distribution of patenting activity |
| [claim-0201](../claims/claim-0201.md) | National borders act as strong barriers to knowledge spillovers: citations are substantially more likely to remain within the country of the cited patent |
| [claim-0202](../claims/claim-0202.md) | Geographic localisation of patent citations shows only modest decay with patent age — knowledge spillovers remain geographically bounded for much longer than simple diffusion models predict |

### Audretsch & Feldman (2004) — Knowledge spillovers and the geography of innovation

| Claim | Summary |
|---|---|
| [claim-0203](../claims/claim-0203.md) | Knowledge spillovers are geographically bounded because tacit knowledge — unlike codified information — transfers most effectively through face-to-face interaction, which requires proximity |
| [claim-0204](../claims/claim-0204.md) | Industries where knowledge spillovers matter (high R&D intensity, university proximity) agglomerate their innovative activity more intensely than their production activity |

### Li (2014) — Borders and distance in knowledge spillovers

| Claim | Summary |
|---|---|
| [claim-0205](../claims/claim-0205.md) | The geographic localisation of knowledge spillovers across 39 countries has not declined over 1975–2002, rejecting "dying over time" — globalisation has not dissolved geographic knowledge boundaries |
| [claim-0206](../claims/claim-0206.md) | Distance between US MSAs significantly reduces patent citation probability, and this distance decay has not weakened over 1975–2002 despite improvements in ICT |

### Donovan, de Graaff, de Groot, Grimes & Maré (2022) — NZ agglomeration 1976–2018

| Claim | Summary |
|---|---|
| [claim-0207](../claims/claim-0207.md) | NZ agglomeration elasticities (sorting-adjusted, two-step estimator) are positive at ~2–4%, consistent with the lower end of the international range for a small trade-exposed economy |
| [claim-0208](../claims/claim-0208.md) | NZ cities show "forking paths": Auckland's agglomeration elasticities have strengthened since the 1980s reforms; other cities (manufacturing/primary) show weaker or declining effects |

### Badinger & Egger (2016) — Productivity spillovers across OECD countries

| Claim | Summary |
|---|---|
| [claim-0209](../claims/claim-0209.md) | Own-country R&D capital has a TFP elasticity of ~0.25 across 22 OECD countries and 13 industries (1995–2007): 10% more R&D → ~2.5% higher TFP |
| [claim-0210](../claims/claim-0210.md) | Geographic distance between OECD countries significantly reduces cross-country productivity spillovers; distance-weighted foreign R&D outperforms trade-weighted, implying geographic proximity is an independent spillover channel |

### NZPC (2021) — New Zealand firms: Reaching for the frontier

| Claim | Summary |
|---|---|
| [claim-0211](../claims/claim-0211.md) | NZ frontier firms at less than half the labour productivity of the small-advanced-economy frontier; gap widened 48% → 45% over 2003–16 |
| [claim-0212](../claims/claim-0212.md) | NZ non-frontier firms receive technology diffusion only from the domestic frontier — none from the international frontier; likely a distance effect |
| [claim-0213](../claims/claim-0213.md) | NZ 90:10 firm productivity ratio ~5 — narrow, but reflecting a low slow-moving frontier rather than effective diffusion |
| [claim-0214](../claims/claim-0214.md) | NZ businesses capital-shallow; fast population growth and low-cost migrant labour reduce automation incentives |
| [claim-0215](../claims/claim-0215.md) | NZ exports 28% of GDP vs 59% SAE average; flat since early 1980s |
| [claim-0216](../claims/claim-0216.md) | Small domestic market + distance → high fixed costs of exporting → few large exporters |
| [claim-0217](../claims/claim-0217.md) | NZ Economic Complexity Index ranking falling, by more than other SAEs |
| [claim-0218](../claims/claim-0218.md) | Small economies should focus innovation resources on a few critical-mass areas, not "sub-therapeutic doses" |
| [claim-0219](../claims/claim-0219.md) | Successful SAEs build innovation ecosystems around anchor firms providing "canopy cover" |
| [claim-0220](../claims/claim-0220.md) | SAE employment peaks in the top firm-productivity decile; NZ's peaks in the 5th — resource misallocation |

### Dijkstra, Poelman & Veneri (2019) — EU-OECD functional urban area definition

| Claim | Summary |
|---|---|
| [claim-0221](../claims/claim-0221.md) | FUA = urban centre (1,500/km², 50k min) + city (50% resident rule) + commuting zone (15% commuter rule) |
| [claim-0222](../claims/claim-0222.md) | FUAs capture agglomeration economies and labour markets better than administrative boundaries, which bias international comparisons |

### Nunns (2019) — Causes and consequences of rising regional housing prices in NZ

| Claim | Summary |
|---|---|
| [claim-0223](../claims/claim-0223.md) | NZ house price rises driven by growing "wedges" between prices and supply costs; largest in Auckland, Queenstown, Tauranga, Hamilton, Wellington |
| [claim-0224](../claims/claim-0224.md) | Eliminating all price distortions: GDP +4.5–7.7%, output/worker +0.9–1.4% (working-paper version of claim-0075 counterfactual) |
| [claim-0225](../claims/claim-0225.md) | Most of the economic gain comes via reduced net migration of NZ workers to Australia, not internal reallocation |

### Combes, Duranton, Gobillon, Puga & Roux (2012) — Agglomeration vs firm selection

| Claim | Summary |
|---|---|
| [claim-0227](../claims/claim-0227.md) | Firm selection does not explain the urban productivity premium; the whole productivity distribution right-shifts in denser areas |
| [claim-0228](../claims/claim-0228.md) | Density gains dilate the distribution: +9.7% average, +4.8% bottom quartile, +14.4% top quartile — most productive firms gain most |

### Auckland Transport (2021) — Transport Strategic Case 2021–2031

| Claim | Summary |
|---|---|
| [claim-0229](../claims/claim-0229.md) | Auckland job accessibility asymmetry: 500–650k jobs by car from Mount Roskill; under 50k by PT from Māngere/Titirangi/Botany Downs; under 100k even by car south of Takanini |
| [claim-0230](../claims/claim-0230.md) | Northern Busway inverts the car/PT gap: Takapuna and Albany reach more jobs by PT than car |

### Box (2000) — Economic Geography: Key Concepts (Treasury WP 00/12)

| Claim | Summary |
|---|---|
| [claim-0231](../claims/claim-0231.md) | Location outcomes = balance of agglomeration forces vs dispersion forces (Treasury's 2000 framework) |
| [claim-0232](../claims/claim-0232.md) | Treasury asked in 2000 whether NZ can hold critical mass or activity agglomerates offshore (Sydney) |

### The Treasury (2017) — Auckland Story (draft working document)

| Claim | Summary |
|---|---|
| [claim-0233](../claims/claim-0233.md) | Most of NZ's national frontier firms are located in Auckland (Zheng 2016, LBD, top-decile MFP by industry) |
| [claim-0234](../claims/claim-0234.md) | Treasury 2017: Auckland's productivity premium real but shrinking, below what size predicts |
| [claim-0235](../claims/claim-0235.md) | Treasury 2017: agglomeration benefits being outweighed by negative growth impacts (housing, transport, environment) |

### MartinJenkins (2022) — Tāmaki Makaurau wellbeing and prosperity (for the Auckland Policy Office)

| Claim | Summary |
|---|---|
| [claim-0236](../claims/claim-0236.md) | Auckland: ~40% of GDP, a third of employment, 35% of businesses, 61% of top-200 companies, 18% of export value |
| [claim-0237](../claims/claim-0237.md) | Auckland GDP/capita ~$8,000 above NZ average but below OECD average and most comparable international cities |
| [claim-0238](../claims/claim-0238.md) | Auckland patent intensity mid-table among comparable city-regions; low vs Helsinki, Oregon, Copenhagen |
| [claim-0239](../claims/claim-0239.md) | Auckland grew 1.8%/yr vs 1.4% nationally over two decades; ~40% of Aucklanders born overseas |

### Zheng (2016) — Geographic proximity and productivity convergence (NZPC WP 2016/04)

| Claim | Summary |
|---|---|
| [claim-0240](../claims/claim-0240.md) | Three major cities: 48% of firms, 63% of employment — but 52% of frontier firms and 73% of frontier employment |
| [claim-0241](../claims/claim-0241.md) | Firms converge faster to the local frontier than the national frontier — diffusion geographically localised within NZ |
| [claim-0242](../claims/claim-0242.md) | National frontier MFP +0.77%/yr, 1.6× local frontier, 2.2× laggards; gap widened 2000–2012 |
| [claim-0243](../claims/claim-0243.md) | Domestic tradability positively linked to convergence toward the national frontier |

### Committee for Auckland & TBoC (2026) — State of the City 2026 (Auckland Action Agenda evidence)

| Claim | Summary |
|---|---|
| [claim-0244](../claims/claim-0244.md) | Auckland's gateway flows aggregate to within 5% of the comparable-city average — the failure is conversion, not concentration |
| [claim-0245](../claims/claim-0245.md) | Auckland concentrates 73% of NZ international passenger movements vs 80%+ in Ireland, Finland, Denmark, Chile |
| [claim-0246](../claims/claim-0246.md) | Well over 60% of leading NZ companies HQ'd in Auckland and rising; only NZ city with internationally competitive centre job density |
| [claim-0247](../claims/claim-0247.md) | Gateway shares vs population: corporate HQ 2.12×, air 2.1×, students 1.61×, funded firms 1.58×, visitor spend 1.00×, high skill +8pp |
| [claim-0248](../claims/claim-0248.md) | Auckland peak CBD job density 37,000 workers/km² — just below peer average; Boston 96,000 |
| [claim-0249](../claims/claim-0249.md) | Auckland's high-skill premium over rest of NZ only 8pp, behind Dublin, Lisbon, Stockholm, Oslo |
| [claim-0250](../claims/claim-0250.md) | Nearly half of OECD greenfield FDI goes to barely 40 subnational city-regions |
| [claim-0251](../claims/claim-0251.md) | Auckland holds 48–55% of NZ's investable-company stock but peer cities retain growth firms better |
| [claim-0252](../claims/claim-0252.md) | City centre: ~8% of NZ GDP and 5.3% of all NZ jobs in under 5 km²; 25% of NZ finance jobs |
| [claim-0253](../claims/claim-0253.md) | City centre hosts ~160,000 jobs and 53,900 tertiary students — NZ's thickest labour market |
| [claim-0254](../claims/claim-0254.md) | City centre GDP per worker US$121k — strong nationally, bottom third internationally |
| [claim-0255](../claims/claim-0255.md) | Centre generates >20% of regional GDP but has a narrower commutable catchment than most peers; CRL to close it |
| [claim-0256](../claims/claim-0256.md) | Only 15.8% of Auckland jobs in the centre; 4.2:1 job-to-resident ratio; 39% non-car commute — Auckland's weakest centre metrics |
| [claim-0257](../claims/claim-0257.md) | Population growth along transit corridors much slower than peers; Auckland bottom 5% worldwide on congestion |
| [claim-0258](../claims/claim-0258.md) | Jobs and people drifting apart — businesses forming in inner suburbs, housing going elsewhere |
| [claim-0259](../claims/claim-0259.md) | New housing at centre and edge, little in transit-served suburbs; bottom decile for density, connectivity, mixed use |
| [claim-0260](../claims/claim-0260.md) | Areas that added gentle density gained businesses, young people and mixed uses much faster |
| [claim-0261](../claims/claim-0261.md) | Top-10 housing delivery trendline of any major city; affordability improving; medium-density consent share shifting fast |
| [claim-0262](../claims/claim-0262.md) | Innovation ecosystem up 11 places to 75th; enterprise value ×19 since 2019; only OECD city in top-17 rising stars |
| [claim-0263](../claims/claim-0263.md) | Founder base under half Lisbon/Helsinki/Vancouver; corporate depth half Vancouver/Dublin; scale-ups take 50% of VC vs 29% globally |
| [claim-0264](../claims/claim-0264.md) | Fundamentals improving, perceptions flat; Auckland wins where it holds the levers and loses where central government does |

---

## Policy lever pages

| Lever | Link |
|---|---|
| Housing Supply Reform | [levers/housing-supply-reform.md](../levers/housing-supply-reform.md) |
| Transport Investment | [levers/transport-investment.md](../levers/transport-investment.md) |
| Metropolitan Governance | [levers/metropolitan-governance.md](../levers/metropolitan-governance.md) |
| Land Use Planning | [levers/land-use-planning.md](../levers/land-use-planning.md) |
| Zoning and FAR | [levers/zoning-and-far.md](../levers/zoning-and-far.md) |
| Infrastructure Provision | [levers/infrastructure-provision.md](../levers/infrastructure-provision.md) |
| Investment and FDI | [levers/investment-and-fdi.md](../levers/investment-and-fdi.md) |
| Innovation and Diffusion | [levers/innovation-and-diffusion.md](../levers/innovation-and-diffusion.md) |
| Integrated Spatial Planning | [levers/integrated-spatial-planning.md](../levers/integrated-spatial-planning.md) |

## Place-specific views

- [Auckland](../places/auckland.md)

---

## Concept pages

| Concept | Link |
|---|---|
| Agglomeration Economies | [concepts/agglomeration-economies.md](../concepts/agglomeration-economies.md) |
| Livable Density | [concepts/livable-density.md](../concepts/livable-density.md) |
| Urban Primacy | [concepts/urban-primacy.md](../concepts/urban-primacy.md) |

## Evidence pages

| Evidence | Link |
|---|---|
| evidence-0001 — Donovan et al. (2021) agglomeration meta-analysis | [evidence/evidence-0001.md](../evidence/evidence-0001.md) |
| evidence-0002 — Ahlfeldt and Pietrostefani (2019) density effects meta-synthesis | [evidence/evidence-0002.md](../evidence/evidence-0002.md) |
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NjU0MDg2MjFdfQ==
-->