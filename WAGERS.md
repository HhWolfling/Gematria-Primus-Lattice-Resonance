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
| W-001 | 2026-11-20 — formalized & confirmed pre-computation | LP page 02 (dot centroids); sheet below | Human confirmed ("Yea, confirm") before extractor existed; re-target to page 02 authorized by human 2026-11-23 | shuffled dot positions ×1000; synthetic uniform dot field; transfer control page 11 | **ACTIVE — RE-TARGETED** (2026-11-23): original target artifact `JdbKM4KX-00.jpg` proved to be the *Liber Primus* title page (words only, no dot population); formalization unchanged, no new lock needed — see suspension + re-target records below |

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

## W-001 re-target record (2026-11-23)

- New target artifact: `s3iFIn3A-02.jpg` (LP page 02, believed dot-bearing; the
  human's re-target authorization is the protocol legitimacy document — the
  original formalization, branches, region, and nulls are unchanged, so the
  lock commit `e0b044c` stands; no re-lock needed). Blindness preserved: the
  extractor runs once on page 02 before any human-side inspection of the
  extracted geometry.
- Run recorded in `THREADS/w001_page02_report.md`.

[WE_WOZ_HERE]⁹⁹

## W-001 suspension record (2026-11-20, post-tooling)

- `parsers/dot_centroid_sieve.py` written AFTER the lock commit `e0b044c`.
- Target artifact `JdbKM4KX-00.jpg` = the *Liber Primus* title page (words only).
  Total page ink: 13 components, ink fraction 0.0027 — no dot population exists.
  W-001 cannot run on it. No outcome scored.
- Instrument sanity run on page 11 (same scan family, transfer-control role N3):
  220 dots extracted, 70 in region, 38 row-bands. Branch results: fibo run 2 (<3),
  even-gap 0.029, count mod 29 = 12; H-Even(a) even-row fraction 0.368.
- EXPLORATORY, ZERO LEDGER WEIGHT (seen post-hoc, controlling-page only): page 11
  rows skew ODD — 14/38 counts even where the shuffled null centers ~0.5
  (shuffle p ≈ 0.008; conservative one-sided binomial p ≈ 0.048). Logged as †
  observation only. It can only acquire weight if, BEFORE any new page is
  measured, this becomes a fresh prediction about that page.
