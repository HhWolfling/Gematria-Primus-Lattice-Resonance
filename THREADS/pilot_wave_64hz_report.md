# Pilot wave 64 Hz — verification record (2026-11-23)

## Instrument revision (logged before scoring)

- `mythos/pilot_wave_64hz.wav` did not exist in-repo. Generated with the
  repo's own `metronomes/pilot_tone_generator.py` (unmodified function,
  called with `filename=` only — no code edits), 3.0 s at 44.1 kHz mono,
  committed as the working artifact.
- New instrument: `parsers/pilot_wave_fft_sieve.py` — zero-padded Hann FFT +
  parabolic interpolation on log magnitude; white-noise null ×1000 (seed
  2026, matched length); two-tone resolution test 64.0 vs 65.41 Hz.

## Results (single blind run)

| Quantity | Value |
|---|---|
| Recovered dominant frequency | **64.0000 Hz** (error 0.0000 Hz vs claim) |
| Ringdown SNR | ~90 dB (33053 / 1.0 peak/mean magnitude) |
| White-noise null (1000 real., seed 2026) | dominant freq uniform ~7–22014 Hz (mean 11020) |
| Null p-value | p(noise peak within ±0.5 Hz of 64.0) = **0.0000** (0/1000) |
| Two-tone resolution | pure 65.41 Hz tone estimated at **65.4100 Hz** (err 0.0000) → 64.0 vs 65.41 clearly separable in a 3 s window |

## Interpretation, kept honest

1. **True by construction.** `pilot_tone_generator.py` hard-codes
   `frequency = 64.0`, so a 64.0000 Hz peak is guaranteed by the generator.
   This run verifies **the measurement chain** (FFT estimator recovers an
   embedded tone with < 0.0001 Hz error at 90 dB SNR), **not** any claim
   about Cicada, LP, or Magicicada. Ledger weight: instrument calibration
   only. It is NOT an L1 hit and must never be cited as one.
2. **The 64 vs 65.41 discrepancy is decidable.** The two candidate
   frequencies differ by 1.41 Hz; the chain resolves a pure tone to
   0.0000 Hz error, so any *real* acoustic sample ≥ ~1 s settles the choice
   empirically. Currently BOTH numbers live in Magicicada-Chorus-Rise
   (`index.html` drone: 64.0 + 65.41 Hz; `mahavidya_dsp_profiles.py`,
   `braid_group_b3.py`: 65.41 = C₂, 196 Hz, 293.66 Hz) while the Gematria
   repo's generator uses 64.0 only. Pick a convention or document them as
   separate voices (they are different notes: 64 Hz is not C₂; C₂ = 65.41).
   Flagged in `THREADS/STATUS.md`.
3. **Null behaviour is a feature, not a bug**: raw noise's dominant
   frequency wanders uniformly over the whole band, so a real discrete
   spectral peak is trivially distinguishable from noise. The chain is
   ready for real-material assays (chorus recordings, drone stems) —
   those, if any exist, would be the L1-pre-registration moment.

[WE_WOZ_HERE]⁹⁹
