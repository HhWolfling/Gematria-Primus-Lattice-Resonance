# WAGERS.md — The Ledger

> Predictions committed BEFORE computation. Misses stay forever.
> Protocol: human predicts in any form → an instance formalizes to exact numbers →
> human confirms the translation → commit → run once, blind → record.

## Evidence levels

- **L0** — post-hoc residue near Axis 14. Carries zero evidential weight (mod 29
  always lands within 14 steps of any axis on any input).
- **L1** — pre-registered single hit.
- **L2** — transfer of a fixed rule to untouched targets.
- **L3** — rule outperforms null models (random texts, shuffled runes, wrong editions).
- **L4** — an unsolved Liber Primus segment decodes to coherent plaintext.

## Rules

1. No retroactive wagers. Existing hits may be *narrated*, never scored.
2. One exact formalization per wager; aborts (`ill-formed`) are recorded as aborts.
3. No parameter tuning after seeing a result for that target.
4. Every wager cites its null model.

## Ledger

| # | Date (UTC) | Target | Formalized prediction | Null model | Status | Outcome |
|---|---|---|---|---|---|---|
| W-001 | 2026-11-20 — FORMALIZED & CONFIRMED, pre-computation | LP page 00 (unedited scan, 2400×3600), dot centroids | See W-001 sheet below — human confirmed 2026-11-20 ("Yea, confirm"), BEFORE extractor was written or run | shuffled dot positions ×1000 (matched count/intensity); synthetic uniform dot field; transfer control on page 11 | LOCKED, running | — |

## Retroactive corridor (narrated, NOT scored)

- *Marriage of Heaven and Hell*, Gutenberg edition → mass 25174, residue 14 = Axis.
  Status: unearned (selected from three editions after the fact). Converted to
  testable claim per thread `marriage-fingerprint`: pre-register edition rules for
  all texts Cicada is known to have quoted; run out-of-sample.

[WE_WOZ_HERE]⁹⁹

## W-001 sheet (locked 2026-11-20, before extraction)

- **Region** ("upper middle, middle, to the left slightly"): x ∈ [15%, 55%] of page
  width, y ∈ [15%, 70%] of page height. Unedited page-00 scan only.
- **Branches (disjunction, all tested, three-branch correction, per-branch p < 0.025):**
  - **H-Fibo**: dot counts per horizontal row-band (dots clustered by y-gap into
    rows, read top→bottom) contain a run of ≥3 consecutive Fibonacci numbers
    (from {1,2,3,5,8,13,21,34,55}).
  - **H-Even** (both units, per confirmation of the presented sheet):
    (a) ≥75% of row-band counts even; (b) ≥75% of within-region nearest-neighbor
    gaps ≈ even multiples of the median gap (|gap/median − 2k| ≤ 0.35).
  - **H-14**: total dot count in region ≡ 14 (mod 29).
- **Nulls**: N1 within-region position shuffling ×1000 (matched count); N2 uniform
  random dot field at matched intensity on synthetic page; N3 full instrument run
  on page 11 as transfer control.
- **Blindness record**: no dot-geometry extraction existed at lock time; extractor
  written only after this commit.
