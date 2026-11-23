# THREADS/STATUS.md — What Is Established & Who Owes What

> Living checklist. Maintained between sessions so no instance or human has to
> reconstruct state from memory. Append-only, newest wins per item.

## Established (agreed ground)

1. **Roles** — Human supplies signal (intuition, associations, corpus); instances
   formalize, code, compute, stress-test. See `ROOM.md`.
2. **Wager Protocol** — L0–L4 evidence levels; no retroactive scoring; misses stay.
   `WAGERS.md` seeded; W-001 (page 00 dot geometry) awaiting human prediction.
3. **Code audit** — 100/100 scripts execute (6 need numpy/PIL); independent checks
   pass: 77≡19, 15035≡13, 5469≡17, 7292≡13 (mod 29); Kuramoto R=0.9844 House 4.
4. **Known doc bug** — README + OPTICAL module claim 2674≡23 (mod 29); scripts
   resolve 6. Fix pending.
5. **"Zero dependencies"** — 6 numeric exceptions; reword README.
6. **Theme sorter** — χ²=13.2 (df 28) on 114 pairs: distribution flat vs uniform;
   current matches are hypothesis generation. Upgrade path: pre-registered 29-theme
   table, tested out-of-sample on future sieved texts.
7. **Couples/singles** — couple structure (pairs summing to 14) is definitional;
   frequencies testable once corpus universe is specified.
8. **FFT doctrine** — rings and X are regular (paper/JPEG noise; runic diagonal
   strokes; frames). Anomaly = sharp discrete radii or off-grid peaks. Full-page FFT
   is the wrong instrument for dot codes; dot-centroid geometry is the right one.
9. **Marriage fingerprint** — edition identification accepted as legitimate method;
   requires a pre-registered edition rule; other Cicada-quoted texts become
   out-of-sample trials. Independent corridor: LP's closing page quotes Blake's
   "For everything that lives is holy" (end of A Song of Liberty).
10. **Mabinogion tape** — cuts mid-sentence, no punctuation (Line 65 boundary).
    Riddle "how many lines left when Mabinogion paused" → LinesLeft is sieveable;
    wager candidate pending edition, total lines, and fixed formula.
11. **Vault policy** — external repos (e.g. krisyotam/cicada3301) okay as reference
    nodes: link + attribute + archive; no GPL code copied into CC-licensed repo.
12. **Fiji discipline** — Fiji operations run on UNedited scans only; edited images
    are separate presentation copies. Null models: synthetic rune page; shuffled
    dot positions; wrong editions.

## Open items — Human

- [ ] W-001 SUSPENDED ×2 (2026-11-20, 2026-11-23): "00" scan = title page;
      "02" scan (`s3iFIn3A-02.jpg`) = the *Chapter 1 / INTUS* divider page —
      13 letter-glyph components, zero dots (report:
      `THREADS/w001_page02_report.md`). Formalization + branches stay locked.
      **Needed: an actually dot-bearing page scan — index number ≠ page content
      in this scan family.** Page 11 is burned as transfer control + exploratory
      material; scoring it as target would be L0 by construction.
- [x] ~~W-002 (page 24 bottom-half dot clusters)~~ — **RESOLVED: LOSS, 4/4
      branches miss** (POW2 0.583<0.75 though 0/1000 shuffle reaches it —
      near-miss with structure; MULT4 0.25; COUNT24 23≠24; 24MOD 65≡7).
      Report: `THREADS/w002_page24_report.md`. W-003 (POW2 transfer, L2) is a
      DRAFT awaiting human confirm + untouched dot-bearing pages.
- [ ] W-002r: riddle wager — name the edition, total lines, cutoff line, and
      the fixed formula + target it should land on.
- [ ] 29-row theme table from the theme sorter (one theme per residue, committed
      before new books arrive).
- [ ] Pages 03/04 scans for the spectral X-profile comparison.
- [ ] Clarify RGB markers on 11exp (her annotation / enhancement artifact / in scan?).
- [ ] Marriage thread: write the fixed edition rule text.
- [ ] ### Phone-app audio readings vs bytes (2026-11-23): human's apps read
      Interconnectedness 75.6 Hz "D#2 dominant 94%", Instar "61 most, 64 right
      behind"; bytes (MD5-verified original AND human's own YT rip) show
      64.0/65.41/75.6 all at local background — real fundamentals 58.91 Hz
      (Instar) and 73.41 Hz = D₂ (Inter). "61/63.5" pattern = BPM halfing
      (122/2, 127/2), not Hz. BPM claims 127/122 plausible but weakly
      supported by spectral-flux tempo analysis. Any future music-frequency
      claim → pre-register as W-004 candidate.
- [ ] Naming + location of the new "project" repo (second copy of ROOM.md lives there).
- [ ] Counting convention for Gutenberg texts (boilerplate, whitespace, punctuation).

## Open items — Instances

- [ ] `mixtum_sorter.py` routes on `len(content) % 29` alone (length proxy).
      Plan: rebuild routing on measured structural features (self-symmetry metrics,
      13/17 periodicity in token spacing, link/reference density) so the Mixtum
      labels become tested quantities. Also fix `UnicodeDecodeError` (byte 0x91,
      cp1252 quotes) in `automated_ingestion_pipeline.py` — open with
      `errors='replace'` and log anomalies instead of crashing.

- [x] ~~Follow-up PR: fix 2674 doc drift + "zero dependencies" wording~~ — human
      already removed the zero-dependency claim in commit `eb56734`
      ("small_change_different_ring"); the 2674 doc fix remains open.
- [x] ~~Dot-centroid extractor~~ — built as `parsers/dot_centroid_sieve.py`,
      sanity-verified on page 11 (220 dots). Suspended W-001 target issue above.
- [x] ~~64 Hz pilot wave verification vs white-noise null~~ — done: wav didn't
      exist in-repo; generated via the repo's own generator, instrument is
      `parsers/pilot_wave_fft_sieve.py`, recovery 64.0000 Hz err 0.0000 @ 90 dB,
      null p=0.0000, 64.0 vs 65.41 separable. **Truth-by-construction: generator
      hard-codes 64.0 — calibration only, not a hit.** Report:
      `THREADS/pilot_wave_64hz_report.md`.
- [x] ~~Cicada releases audio assay (exploratory)~~ — done, MD5-verified Archive
      mirrors of both 2014 releases analyzed: **64.0 and 65.41 Hz ABSENT as
      discrete tones** (1.0× local bg); real LF fundamentals 58.91 Hz (Instar)
      and 73.41 Hz = D₂ (Interconnectedness, standard A440 tuning). Report:
      `THREADS/audio_instar_interconnected_report.md`. Chorus-Rise drone labels
      are synthesis conventions, not measurements — human may want to relabel
      or pre-register W-003 (chirp-rate instrument) for a real claim.
- [ ] ### 64 vs 65.41 Hz description discrepancy (needs human decision): both
      constants live in Magicicada-Chorus-Rise (drone: 64.0 + 65.41 Hz; braids:
      65.41 = C₂, 196, 293.66 Hz) while the Gematria generator uses 64.0 only.
      64 Hz ≠ C₂ (65.41). Instrument can settle which is intended on any real
      audio sample ≥ ~1 s.
- [ ] Synthetic rune-page FFT control + radial profiles for 00/01 (rings) and 03/04 (X).
- [ ] Null-model machinery for theme table and pair frequencies.
- [ ] Permission debugging: why instance-side git writes 403'd before; document fix.

[WE_WOZ_HERE]⁹⁹
