# W-001 re-target run record — page 02 (2026-11-23)

## What was authorized

Human re-targeted the locked W-001 formalization (branches H-Fibo, H-Even a+b,
H-14; region x ∈ [15%, 55%] width, y ∈ [15%, 70%] height; nulls N1 shuffle
×1000 seed 2026, N2 synthetic, N3 page-11 transfer control) from the page-00
scan onto `s3iFIn3A-02.jpg`, believed to be the first dot-bearing LP scan.
Re-target authorization: human, 2026-11-23. Formalization and lock commit
`e0b044c` unchanged.

## What the artifact actually is

Blind single run of `parsers/dot_centroid_sieve.py` on
`/mnt/vibefs/uploads/5d36a0d1-77be-49f4-800a-76cf60846a87/s3iFIn3A-02.jpg`:

- Instrument as-committed extracts **0 dots** on this scan (initial crash on an
  empty extraction — `IndexError` on an empty centroid array — because the
  page's 13 components all exceed the committed area window [12, 300] px²).
- Component anatomy (background-ratio threshold 0.72, blur 25, Gaussian):
  - **13 components total**, total ink fraction 0.0033 — near-empty page.
  - Row A (y ≈ 19.6–20.7%): **8 glyphs**, x spanning 37.6%–62.4%, areas
    1255–3304 px².
  - Row B (y ≈ 32.1–32.8%): **5 glyphs**, x spanning 44.5%–55.0%, areas
    1521–2109 px².
- Visual inspection (VM) of the scan: the page reads **"Chapter 1"** and
  **"Intus"** — this is the Liber Primus **Chapter 1 divider page**, small caps
  decorative text. 8 + 5 = 13 glyph components matches the visual exactly.
- **No dot population exists on this page.** The human's page-numbering vs.
  the scan's content diverged again (same failure class as the "00" title page).

## Protocol consequence

- **W-001 remains SUSPENDED** — same status as 2026-11-20: target artifact
  invalid, formalization intact and locked, no hit, no miss, nothing scored.
- Notable zero-weight trivia: the page carries exactly 13 ink components; the
  5-glyph second row happens to sit inside the locked region. None of this is
  scoreable — H-14 counts *dot centroids* on a *dot-bearing* page, and a
  letter glyph is not a dot by the committed definition. Logged so it cannot
  later be re-framed as a "hit."

## What W-001 actually needs

1. A **genuinely dot-bearing** LP scan (the *00/02 index numbers don't carry
   dots in this scan family* — index ≠ page content).
2. Pages already XORed in-session (page 11, 220 dots) are burned as transfer
   control N3 and as exploratory odd-row material; scoring page 11 as W-001
   target would be L0 by construction (branch stats already observed). It
   would need a fresh formalization, not a re-target.

[WE_WOZ_HERE]⁹⁹
