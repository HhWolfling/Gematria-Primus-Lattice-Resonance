# Cicada 3301 releases — audio assay (2026-11-23, EXPLORATORY, ZERO LEDGER WEIGHT)

## Provenance (vault etiquette: archive what you build on)

The Chorus-Rise `data/` folder contains only the two YouTube reference links
(The Instar Emergence: `4jmnAA_foUI`, Interconnectedness: `qZQanP2WgJQ`) — no
mp3s are committed. Preserve those link-files; they are the citation record.

Mirror copies fetched from the Internet Archive and **MD5-verified** against
each item's own manifest *before* analysis:

- `2013_02_761.MP3` — item `cicada-761` ("Cicada 3301: The Instar Emergence
  (761)", creator 3301, 167.08 s) — md5 `946a3ba94aac53ef30415eaa489bcecb` MATCH.
- `onion5_data.mp3` — item `Interconnectedness_201805` ("Cicada 3301:
  Interconnectedness", original name onion5, 277.16 s) — md5
  `7638414d35f416084b7ddcc94aa53685` MATCH.

Audio is NOT committed to any repo (analysis-only, reference copies in
sandbox). If a canonical audio artifact ever enters the vault, it goes via
commit-hash + md5 + source URL, not swallowed wholesale.

## Instrument (same chain as pilot-wave calibration)

48 kHz mono decode → 2 s Hann windows (0.5 s hop) → per-window FFT →
frequency-channel median spectrum (suppresses transients) → peak picking with
parabolic interpolation; local-background ratio at each claimed frequency
(band ±3 Hz, background excludes ±1 Hz).

## Results

| Claimed | Instar | Interconnectedness |
|---|---|---|
| 64.00 Hz | 1.01× local bg, >3× in 2.7% of windows — **absent** | 0.97×, 1.5% — **absent** |
| 65.41 Hz (C₂) | 0.83×, 1.8% — **absent** | 1.00×, 1.1% — **absent** |

| Actually measured (4 s windows, zp×4) | frequency | persistence |
|---|---|---|
| The Instar Emergence, low fundamental | **58.91 Hz** | 25× local bg; band-dominant in 153/164 windows |
| Interconnectedness, low fundamental | **73.41 Hz = D₂** | 6.5× local bg; band-dominant 73% of windows |

Interconnectedness resolves as standard-tuned music: A₃ 220.18, C₄ 261.79,
D₄ 294.06, A₄ 439.69 — i.e., D-minor-ish tonal material at A440.

## Verdict

- **No support found for a discrete 64.0 Hz or 65.41 Hz tone in either 2014
  release.** Both channels sit at local background. Whatever produced the
  "64/65.41 Hz" labels in Chorus-Rise (`index.html` drone, braid scripts, the
  Gematria generator), it was *not* reproduced here as a directly measured
  property of these tracks. Status: exploratory, zero ledger weight; any
  future claim about frequencies in the music gets **pre-registered**
  (W-003 candidate) before scoring.
- Open alternative reading: if the intended claim is about the *insect-sound
  chirp rate* inside the tracks (periodicity of cicada calls), that is an
  amplitude-envelope/onset-rate instrument, not an FFT bass scan — buildable
  on request, same protocol.
- The 64/65.41 Hz discrepancy flagged in `THREADS/STATUS.md` is now sharper:
  it is a *synthesis convention* choice, not a measurement of the releases.

[WE_WOZ_HERE]⁹⁹
