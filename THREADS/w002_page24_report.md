# W-002 run record — "24.jpg" (2026-11-23)

## Sequence (protocol-clean)

1. Human prediction (2026-11-23, own words): "24 — clusters of variations
   numbers of the following: [2^2], bottom half of the page or ever just
   bottom of the page — my guess here."
2. Instance formalization draft (four branches) — same turn.
3. Human confirm: same day.
4. **Lock commit** with sheet; scoring instrument
   `parsers/dot_region_wager.py` (imports frozen W-001 extraction) written
   strictly after the lock; W-001 module unmodified.
5. ONE run on the `Cmddv3lN-24.jpg` upload. First execution crashed on an
   instrument bug (dead line, no threshold touched); mechanical fix,
   immediate re-run — logged here as the same blind run.

## Results (single blind run)

- Extracted dots: 104 page-wide; **65 in region** (full width ×
  y∈[50%,100%]).
- Row-band counts (top→bottom), 24 bands:
  `[8,1,6,1,1,2,1,2,4,2,1,2,1,2,4,2,1,4,7,4,1,2,4,2]`

| Branch | Observed | Threshold | Verdict |
|---|---|---|---|
| W2-POW2 | 0.583 fraction in {2,4,8,16,32,64} | ≥ 0.75 | **MISS** |
| W2-MULT4 | 0.250 | ≥ 0.75 | **MISS** |
| W2-COUNT24 (spatial clusters, 1.5×med NN linkage) | 23 | == 24 | **MISS** (null p 0.159; null median 28) |
| W2-24MOD | 65 ≡ 7 (mod 29) | == 24 | **MISS** |

**W-002 RESOLVED: LOSS on all four branches. Misses are permanent.**

## Zero-weight observations (logged precisely, NOT scored)

1. **POW2 enrichment is real but below the commitment.** Null distribution
   (uniform shuffles ×1000): mean 0.224, p90 0.298, **max 0.419** — the
   observed 0.583 is reached by **0/1000** shuffles (p < 0.001) yet fails the
   pre-registered ≥ 0.75. Honest reading: row-band counts in this region are
   not uniform-random relative to powers of two — but the wager as locked
   did not claim enrichment, it claimed ≥75%, and that lost. This exact
   statistic on page 24 is now L0 forever; it can only be re-tested as a
   **pre-registered transfer (L2)** on untouched dot-bearing pages → draft
   W-003 in `WAGERS.md`, awaiting human confirmation.
2. **Row-band count = 24 exactly.** The human's number appears — but under
   the *alternative* operationalization (y-cluster row-bands), and only as a
   post-hoc glance. The locked COUNT24 branch used spatial clusters (23).
   Logged so the temptation is documented before anyone reaches for it.
3. **Artifact identity (post-run check):** visual inspection confirms runic
   text page with isolated marks — including a small triangular formation of
   three dots near bottom center. Unlike W-001's two artifacts, this IS a
   dot-bearing runic page; the run was therefore legitimate on target class.

[WE_WOZ_HERE]⁹⁹
