# Response log — feedback on v1

A running record of what was done with each piece of review feedback, including
points not taken up and why. This is the source for the thank-you note to Andrew
at the end, so decisions to decline matter as much as decisions to act.

Feedback received on **v1**; changes are being made from **v1.5** onward.

Reviewers: Andrew McCallum (18 inline comments + memo), Hamish (5 points),
Aaron Bacher (3 points).

## Status key

`DONE` acted on · `PARTIAL` acted on in part · `DECLINED` considered, not taken
up · `OPEN` not yet worked

---

## 1. Hamish #3 — successful cities all have congestion and expensive housing

> "It would be useful to give an example of a successful comparator city where
> better planning, timely infrastructure investment, etc has alleviated these
> issues. Most high performing (high productivity) cities that I can think of
> also suffer from congestion, high housing costs, etc too!"

**Assessment.** The strongest point in the batch. A genuine hole in the paper's
logic: if these costs are universal among high-performing cities, they cannot by
themselves explain Auckland's underperformance. v1.5 had no answer to it.

**Status: `DONE`.**

Four paragraphs added to the end of §3.6, where the objection bites hardest —
the section previously closed by calling these pressures "systemic features of
the growth model", which is equally true of London and Sydney.

The argument concedes Hamish's premise and uses it: costs are the price of
access, so the diagnostic question is not whether a city carries them but what
they buy. Auckland carries the cost structure of a successful agglomeration
while returning the productivity structure of an unsuccessful one. It closes on
a test the paper must meet — if the costs were simply the price of scale, the
premium should be commensurate; it is not. Sourced entirely from evidence
already in the paper (the 15% vs 30–40% premium, and the State of the City 2026
city-centre productivity finding).

Trimmed on review: the "this raises a question / here is the answer" scaffolding
between the first and second paragraphs was cut to go straight to the argument.

**Comparator example: `DECLINED`.** Hamish also asked for a city where better
planning and timely infrastructure alleviated these pressures. Not included, for
two reasons. No large city has eliminated them, and implying one has would be
easy to falsify — the defensible claim is about keeping costs proportionate to
benefits, not about solving them. And the striking example (Tokyo) cannot be
sourced from the current evidence base: the only Japan material held is the
land-use zoning count, nothing on housing outcomes. Copenhagen's By & Havn
mechanism in source-0048 was available and citable, but the section reads
better without a case study and the diagnosis is not the right place for one.

---

## 2. Andrew — §5.7 "weak secondary city system" and the §5.8 closer

> "I don't think this is right, or supported by the evidence... the spatial mapping
> work suggests New Zealand may be more polycentric in capability terms than in
> population terms." — and, on §5.8: "Improving Auckland's performance is
> sufficient to improve productivity throughout the national economy. I am much
> less convinced by that proposition."

**Assessment.** Half right, and the paper's own evidence settles which half.

Right that "limited agglomeration effects" overstates: Zheng (2016) shows the
three major cities hold 48% of firms and 63% of employment but 52% of
national-frontier firms and 73% of frontier employment. Christchurch and
Wellington carry more than their share of the country's most productive firms.

Right about the §5.8 closer. His necessary/sufficient distinction holds, and the
decisive point is that the paper already agreed with him in the executive
summary and §6 — it was §5.8 that was out of step with the paper's own position.

Overstating on the capability-node framing. Coleman et al. (2019) — cited in the
same section — found NZ cities became *more diversified, not more specialised*,
with 23 of 30 urban areas seeing their Regional Specialisation Index decline. He
also does not engage with Donovan et al. (2022), cited in §5.8, showing
Auckland's agglomeration elasticities strengthened since the 1980s while other
cities' weakened. And his evidence is unpublished spatial mapping work, which
cannot be cited.

**Status: `PARTIAL`.**

§5.7's closing sentence replaced with two paragraphs that concede the factual
point and then sharpen it. Zheng's frontier-concentration finding establishes
that capability exists outside Auckland; Zheng's local-frontier convergence
finding — all fifteen industries catch up to the local frontier, only nine to
the national — establishes that productivity diffusion is geographically
bounded. This finding was previously unused in the paper.

§5.8's closing sentence rewritten on the necessary/not-sufficient distinction,
aligning it with the executive summary and §6.

**Capability-node framing: `DECLINED`.** Unpublished sourcing, contradicted at
the employment level by a source the paper already cites, and the "network"
claim is not demonstrated — Andrew's own list is of isolated specialisations
with no connective tissue between them. The revised text takes the opposite
position, which the evidence supports better: the secondary city system is *not*
a network but a set of locally bounded economies, weakly coupled to one another
and to Auckland. Capability exists; it does not compound. That is a stronger
argument than either the original text or the proposed reframing, and it
converts Andrew's objection into support for the paper's central claim.

---

## 3. Andrew — intellectual lineage of the agglomeration discussion

> "One area that could be strengthened is the intellectual lineage... Marshall's
> work on industrial districts... Porter's cluster theory... Krugman and the New
> Economic Geography... McCann's 2009 analysis applied these insights directly to
> New Zealand."

**Assessment.** A real gap. §2 went straight to modern meta-analyses and cited
none of the tradition it sits in.

**Status: `DONE`.**

Three paragraphs added to §2, placed before the enumerated findings so the
lineage sets them up rather than trailing after them. The load-bearing claim is
that the paper's own matching/sharing/learning triad *is* Marshall's three
reasons by way of the modern formulation — which costs one sentence and makes
§2 look like it knows where it stands.

McCann's actual argument turned out to be sharper than the summary Andrew gave.
He is not merely saying geography matters; he argues the New Zealand
productivity debate has been conducted almost entirely in institutional and
free-market-versus-interventionist terms, and that viewed through economic
geography "there is nothing really paradoxical about New Zealand's productivity
performance" (p. 279). The paradox dissolves. That is a stronger statement of
this paper's own thesis than anything else in the lineage, so it is quoted
directly.

Andrew's meta-point is kept as the third paragraph: the argument was published
in a policy-facing journal seventeen years ago and did not take, and if spatial
factors really do determine productivity then that analytical gap is one of the
causes of the underperformance rather than just a failure to describe it.
Rewritten from the draft after review to state the mechanism rather than assert
the conclusion.

**Sourcing.** Krugman (1991) and McCann (2009) are now held in `sources/` and
their details were verified against the documents themselves — JPE 99(3),
483–499 and NZEP 43(3), 279–314 respectively. Porter (2000) is now held as
`sources/237674578.pdf` and verified against the document itself — the first-page
footer reads "ECONOMIC DEVELOPMENT QUARTERLY, Vol. 14 No. 1, February 2000
15-34", and the article ends on p.34. (The filename is opaque and there is no
source card mapping it, so the mapping is recorded here.) Marshall (1890) is
**paraphrased, not quoted**, because the exact wording of the "in the air"
passage could not be checked — the environment's network policy blocked every
attempt to retrieve a copy. Restore the quotation only after checking it against
Book IV, Chapter X.

**Excluded from Andrew's version.** His material on New Zealand's peripherality
and dispersed population, which is already covered in §3 and §5. His five
paragraphs were compressed to three and rewritten in the paper's register.

---

## 4. Andrew — cite MBIE's own Long-term Insights Briefing

> "This was a core theme in the LTIB. E.g. in principle 3: Knowledge-intensive
> industries thrive in clusters that enable talent pooling, rapid feedback and
> close collaboration, especially when these clusters are connected to global
> networks. Be nice to cite MBIEs own work." — and, separately, that the paper's
> sentence "is actually narrower than the LTIB".

**Assessment.** Right that it should be cited, and the quote is verbatim
(Principle 3, p. 54). But reading it produced a better use than a supportive
citation.

The briefing endorses the paper's mechanism explicitly — "industrial clusters
and agglomeration effects are critical for knowledge-intensive industries" (p.
25) — and its glossary is precise that spillovers "diminish with distance,
making clusters and urban density especially powerful". It also adopts the
core–periphery frame and applies it accurately to New Zealand's position in the
world (p. 15). What it never does is turn that lens inward. Across 68 pages:
New Zealand's own core is never identified, and Auckland's
position as the only metropolitan economy of international scale plays no part
in the analysis — it is named twice, once as a publisher's address and once in a
table cell about aviation hubs.

**Status: `DONE`.**

Supportive citation added to the §5 preamble, at the sentence Andrew anchored
his comment to.

Three paragraphs added to §8, after the opening statement that national policy
has spatial incidence. They observe that the Briefing establishes clusters work
through proximity and density, then prescribes region-tailored cluster strategy
without asking whether New Zealand's regions carry that density — and answer the
question with claim-0076 (Auckland's elasticity ~0.04, identical to other major
cities; only 5–8% more productive than Hamilton, Tauranga, Wellington and
Christchurch from size alone) and claim-0242 (the local-to-national frontier gap
widening).

The third paragraph is the concession that keeps the argument defensible:
regional clusters are not futile, but the lever is connection rather than
proximity. Zheng's tradability finding supports the connection channel;
Christchurch's aerospace firms are productive because they are globally
connected, not because Christchurch is dense. This concedes Andrew's examples
while denying his mechanism, and is consistent with §5.7's "capability exists;
it does not compound".

**Fairness note carried into the text.** The Briefing's remit is international
productivity and trade, so the outward framing is a scoping choice rather than
an oversight, and the paper says so explicitly.

**Revised twice on review.** First, the §8 passage evidenced the point with word
frequencies; removed at the author's direction, since arguing from word counts
invites the rebuttal that "region" is simply the policy vocabulary. Second, the
whole passage was rewritten in a collegial register: the original read as
prosecuting a sister document ("the gap this leaves", "a prescription that
outruns its mechanism", "the question is not asked"). The paper now states
plainly that the Briefing asks a different question — how a small, distant
economy connects to the world — answers it correctly in those terms, and that
the two analyses meet on clusters without producing quite the same answer.

The substance is unchanged and the density line is held. What changed is that
the passage now ends on convergence rather than criticism: the Briefing's own
Principle 3 emphasises clusters "connected to global networks", which is where
this paper's evidence lands too. The domestic corollary — that outside Auckland
connection does nearly all the work and density very little — extends the
Briefing rather than contradicting it.

**"Narrower" claim: `DECLINED`.** Andrew is correct that the paper's sentence is
narrower than the LTIB's, but the LTIB is the broader of the two and the paper's
is the better supported. Widening §5 to match would undercut §5.7.

**Ingestion.** source-0049 created, `ingestion_status: cited_not_extracted` —
held because the paper argues *about* this document and the page references need
an anchor, but no claim cards, since nothing in the wiki depends on it.

---

## 5. Andrew — the history framing in §6

> "My reading… of New Zealand economic history is almost the opposite. For much of
> the twentieth century, economic policy was strongly oriented toward supporting
> spatially dispersed economic activity… The post-1984 reforms arguably
> represented a sharp break from this historical model."

**Assessment.** Andrew identified a real problem but proposed the wrong fix, and
the author landed on a better one.

The clearest objection did not require settling the history at all. §6's list —
abolition of the provinces, the country quota, post-war spreading of opportunity,
Think Big, regional development funding — is almost entirely dispersal-favouring.
There was no example of a policy favouring the major centres. The paragraph
enumerated evidence pointing one way and concluded there had been movement in
two. It also contradicted its own preceding sentence, which said the underlying
tension "has remained remarkably consistent".

Andrew's three-phase alternative was itself vulnerable. The abolition of the
provinces was a centralising act; post-war policy dispersed industry while
simultaneously accommodating enormous metropolitan growth in Auckland; and the
post-1984 period is not "spatially neutral in intent" — the Provincial Growth
Fund was $3bn explicitly for regions, which Hamish separately criticises in the
same feedback bundle. Andrew's framing and Hamish's do not sit comfortably
together.

**Status: `PARTIAL`.**

"Oscillated" replaced with an enduring tension "successive governments have
managed rather than settled" — the author's formulation. This resolves the
internal inconsistency without adjudicating the historical dispute, and it
matches the sentence two lines above it.

**Added beyond Andrew's comment.** Two paragraphs explaining *why* the tension
endures, which was the author's point rather than Andrew's: New Zealand's
extreme centralisation. Councils hold land use, consenting, local roads, water,
waste and public transport, and deliver a substantial share of infrastructure —
but not health, education, tertiary, welfare or justice, and their revenue base
is almost entirely property rates. When the centre allocates, places compete for
allocation, because that is the only agency available to them. The zero-sum
framing §6 objects to is therefore a rational response to the institutional
structure rather than a failure of imagination. This gives the following
paragraph's "therefore" a real warrant for the first time.

No spending-share figure was used: none is held, and claim-0123 cuts the other
way on infrastructure (local government $7.1bn against central government's
$5.8bn). The centralisation claim is about services and revenue, not delivery.

**Correction found while checking.** §5.5 listed transport planning and social
housing among functions that "in some jurisdictions" sit with local authorities,
implying they do not here. Both are wrong: regional councils prepare Regional
Land Transport Plans and Auckland Transport is a CCO, and councils do provide
social housing (Wellington and Christchurch hold portfolios of roughly 2,000
units each; Auckland divested its pensioner housing to Haumaru in 2017). The list
is now narrowed to the unambiguous central functions, with transport planning and
social housing described as formally shared in ways that blur accountability —
which strengthens the "stealth fragmentation" argument rather than weakening it.
Flagged for the author to verify, as the current figures could not be checked
from the repository or online.

**Capability-destruction claim: `OPEN`.** Andrew's second argument — that the
reforms destroyed regional productive capability rather than merely relocating
activity — is not yet addressed. Partially evidenced (claim-0167 on manufacturing
employment halving; claims 0171–0172 on shocks amplifying in specialised local
economies) but his specific list of apprenticeships, supplier networks and
management capability is assertion. Note the trap: claim-0174 finds NZ cities
became *more* diversified over the same period.

---

## 6. Hamish — complexity vs restrictiveness, and "the worst of both worlds"

> "Page 15 notes that 'New Zealand's land use regulatory system is also unusually
> complex by international standards' — yes I agree… However just checking that
> statement is true as it follows Figure 5 which highlights a cluster of higher
> performing networked smaller cities Amsterdam, Copenhagen, Utrecht, Basel,
> Geneva… Many of these areas I would also speculate have complex land use
> regulatory systems."
>
> "It strikes me that with Auckland we have the worst of both worlds — i.e. the US
> problem of urban sprawl and poor public transport along with the restrictive
> land use policies and high housing costs often associated with the European
> model."

**Assessment.** Both correct, and the first is stronger than Hamish made it. The
underlying data for Figure 5 was extracted from the chart in the Word file: it
plots New Zealand cities against Austria, Belgium, Denmark, Finland, France, the
Netherlands and Switzerland, naming Amsterdam, Copenhagen, Utrecht, Basel,
Zurich, Geneva, Bern, Rotterdam, Eindhoven and Paris among others. Every
comparator country there has a plan-led planning tradition. The paper's own
illustration, sixteen lines above the claim, was a chart of high performers with
complex planning systems.

**Status: `DONE`.**

The claim is now about **fragmentation** rather than complexity, which is what
the Te Waihanga evidence actually shows — 1,175 zones across 67 territorial
authorities is a statement about how many hands hold the pen. The paragraph now
sets out two coherent models: simple and permissive (Japan), or complex but
plan-led and predictable with infrastructure committed in advance (northern
Europe). New Zealand is neither, "which is the combination that imposes cost
without buying direction".

Hamish's second point is added as its own paragraph, in the paper's voice rather
than his phrase: Auckland has the dispersed car-dependent form of permissive
North American development without the affordability, and the restrictive
processes and costs of the European model without the directed growth. "Auckland
has taken on the costs of both approaches and the benefits of neither." Both
halves are now evidenced by State of the City 2026 — bottom decile for
residential density, street connectivity and mixed-use access; transit-corridor
population growth far below peers.

**Housekeeping.** Inserting the second paragraph duplicated the bottom-decile
finding twice within §5.1, four paragraphs apart in identical words. The later
instance was trimmed to its distinctive content (the walkability gap).

---

## 7–10. Remaining points, triaged

At the author's direction the remaining queue was filtered to substantive
points and no-regrets fixes only, excluding minor quibbles and conversational
one-liners.

### 10. Devolution — `PARTIAL`

Andrew's comment 16 is a real argument: whether a highly centralised state can
optimally manage a metropolitan economy holding a third of the country.
Comments 29 and 30 ("Devolve most of the decision making to Auckland. Too much
wgtn"; "Or get out of the way") are conversational and not actioned.

Most of the analytical content was already banked by the §6 centralisation
material added under point 5. What remained was whether the paper should
*recommend* moving decision rights. It does not, and deliberately: §9 is pitched
as what MBIE can do with its own advice, and a devolution recommendation would
shift the register to how the state should be reorganised — outside MBIE's remit
and an easy reason to dismiss the paper.

Added instead as its own short paragraph in §9: the distribution of levers is
itself a spatial variable, evidenced by claim-0264 (Auckland performs best where
it holds the levers it controls). Observation, not prescription. The groundwork
is there if a later draft wants to go further.

### 9. Dublin/Helsinki comparator caution — `DONE`

Comments 13 and 14 added to the Auckland Productivity Premium box: those cities
sit within far more densely connected regional economic systems, so the gap is
not like-for-like; but Auckland is also larger than Dublin and Helsinki, which
makes the direction of the gap harder to explain away on scale. The second is a
one-line remark of Andrew's that strengthens the paper's argument rather than
complicating it.

### 7. Tax and financial settings — `DONE`

A qualification added to the end of §5.6: the spatial account is not the only
explanation for capital flowing to land and housing, and presenting it as such
would be over-claiming. Tax settings and spatial constraints are complements —
constrained supply raises the returns to holding land, tax settings determine
how much is retained. Protects the section against the charge of over-claiming
for spatial factors.

### 12. §3 density — `DONE`

Aaron asked for more space tying Section 3 together, and the problem had since
got worse: §3.6 gained four paragraphs answering Hamish. A closing paragraph
added to §3.10 restating the causal chain in plain terms — growth, migration,
metropolitan concentration, absorption failure, capital diversion, dispersal —
ending "a country that runs hard and converts less of the effort into output per
worker than it should."

### Declined

- **NZ Initiative housing literature** (Andrew c.15). `DECLINED`, confirmed by
  the author, who does not want further sources added unless unavoidable. Never
  drafted into the paper, so nothing was removed — verified as zero mentions in
  both formats. The housing evidence is already carried by Nunns, Te Waihanga,
  MHUD and Blick & Stewart; a think tank would broaden the range of perspectives
  without strengthening the evidence. The author name ("Benno Blaschke") was
  never verifiable and is now moot.
- **SCIRT and infrastructure capability** (Andrew). Interesting but a different
  paper's argument, and unsourceable from the current evidence base.
- **Capability destroyed by the reforms** (Andrew). His specific list is
  assertion, and claim-0174 cuts against it.
- **Form-based codes, SmartCode, the transect** (Aaron). His own description was
  "probably way too far down in the weeds".

### Note on editing the call-out box

The Auckland Productivity Premium box is a single-cell table in the .docx.
`paper_docx_to_md.py` renders single-cell tables by joining the cell text and
splitting on ". ", so the box's Markdown line structure is *generated*, not
authored. Editing the Markdown box directly produces line boundaries the
converter would never produce, and parity fails. Edit the .docx, then regenerate
the Markdown block from the converter output.


## Convention: the paper's changelog

The changelog in the paper is a public-facing record. It should say
"responded to internal comments" and summarise what changed, with no reviewer
names and no characterisation of anyone's argument or of other agencies'
documents. The v1.6 row initially named all three reviewers and described the
Long-term Insights Briefing as having been "tested"; both were removed. Detail
about who said what, and about where advice was declined, belongs in this log
and in the reply to reviewers, not in the paper.

---

## Reply to reviewers

A single note to all three reviewers is drafted in
`reply-to-reviewers-DRAFT.md`, organised by substance rather than by reviewer,
and updated as each point closes. One note rather than three at the author's
direction — it also removes an asymmetry problem, since separate notes would
have meant Andrew's explaining a partial rejection while Hamish's was entirely
affirmative, and they would certainly have compared.

This log stays internal. It contains judgements that should not go to
reviewers: where evidence was assessed as insufficient, where proposals were
declined, and where Andrew's and Hamish's accounts of the same period conflict.

---

## 11. Hamish — MBIE's own institutional history

> "How we organise ourselves… within MBIE is important. Many years ago we used to
> have a cities and regions branch that provided the spatial lens to our thinking.
> Dropping the cities focus with the creation of the Provincial Development Unit
> in 2017… shifted the spatial focus away from cities and towards the most
> underperforming regions and reinforced the zero-sum game mentality (regions v
> cities). The formation of MHUD in 2018 stripped out of MBIE any remaining urban
> expertise."

**Assessment.** Substantive, first-hand, and squarely on §9's subject. Andrew
made a related point about MCERT ("will mean the loss of domain knowledge and
expertise as happened with the formation of MBIE").

**Status: `DECLINED`** — author's decision. The paper is being prepared for
publication, and a published account of MBIE's own institutional decisions is
more public criticism of the author's employer than the paper can carry.

This is a decision about what a published paper can say, not a judgement on the
point itself. The substantive claim — that no institution owns the productivity
performance of the spatial system — is already made in §9 under "The Missing
Institution", and Hamish's history explains how that gap arose rather than
establishing that it exists. The argument does not depend on it.

Worth revisiting if the paper is ever circulated internally rather than
published, where the history would be usable and probably valuable.

---

## Still open

None. All fourteen points are resolved: acted on, partially acted on, or
declined with reasons recorded above.

**Constraint carried throughout:** Andrew's capability-node argument rests on
unpublished spatial mapping and sector mapping work. The paper has been through
a publication-readiness sweep and cannot cite unpublished sources, so his
framing can steer revisions but each claim needs published backing.
