# LLM Compilation Instructions for Policy Wiki

## Purpose
Transform a linked Markdown knowledge base into a flattened format usable for large language models (LLMs) that cannot navigate files or follow links.

---

## Core Rule
Every unit (claim, mechanism, policy lever) must be understandable without opening another file.

---

## Output Structure
Create a /compiled/ folder containing:

- overview.md
- claims_full.md
- policy_levers_full.md

---

## Claim Conversion Template

For each claim, produce the following structure:

## {Claim ID}: {Title}

**Statement**  
Clear statement of the claim.

**Meaning (plain English)**  
Explain the claim in simple terms.

**Why it matters**  
Explain policy relevance.

**Dependency summaries**  
Summarise key dependencies inline:
- {Claim ID}: 1–2 sentence explanation

**Mechanism (short)**  
Explain causal logic briefly.

**Evidence (summary)**  
Summarise supporting evidence.

**Policy implications**  
List relevant implications.

**Relevant institutions**  
List key agencies (e.g. MBIE, Treasury).

---

## Policy Lever Template

## {Lever ID}: {Name}

**Objective**  
What it aims to achieve.

**Mechanism targeted**  
How it affects the system.

**Primary owner**  
Lead agency.

**MBIE role**  
Specific actions MBIE can take.

**Constraints**  
Key limitations.

**Related claims**  
List relevant claim IDs.

---

## Conversion Rules

1. Replace links with short summaries (do NOT keep "see X").
2. Inline first-order dependencies (1–3 levels only).
3. Preserve original IDs.
4. Keep sections concise (2–5 sentences max).
5. Prefer clarity over completeness.

---

## Anti-Patterns (avoid)

- "See other file"
- Raw link chains
- One-line claims without explanation
- Heavy cross-referencing without summaries

---

## Goal

Produce a small number of large, self-contained Markdown files that enable single-pass reasoning by an LLM.