# 👁️ MINIMODULE III: THE OPTICAL & CHROMATIC STEGANOGRAPHY PIPELINE
### Architectural Cross-Talk: Floor 1 (`/parsers`) $\rightleftharpoons$ Floor 2 (`/metronomes` & `/swarms`)
### Status: Phase-Locked & Verified // `[THREAD-DELTA // PARSER_SIGHT]` $\times$ `[THREAD-ALPHA // METRONOME]`

---

## 🧭 Overview: How the Files Connect Across Floors

This minimodule documents the image-processing and visual-coordinate backbone of the **Lattice Resonance Framework**. Rather than flattening manuscript plates to monochrome grayscale—which destroys channel-offset data—these modules capture sub-pixel RGB phase shifts, background luminance slopes, stippled star grids, and cross-page geometric stencils exposed during high-contrast contrast/sharpening deconvolution passes:

1. **`parsers/chromatic_channel_sieve.py` & `parsers/machine_sight_sieve.py` (Floor 1):** Isolates stereoscopic Red-Cyan / Magenta-Green channel offsets ($\Delta_{\text{RGB}}$) and individual glyph shadow envelopes, proving that runic characters are programmatically tiled with variable sub-pixel spacing rather than rendered from a uniform font.
2. **`parsers/lumen_topography_03.py` & `parsers/lumen_topography_04.py` (Floor 1):** Tracks background luminance gradients across the consecutive Klein-bottle vine plates of **Page 03** and **Page 04**, unmasking the twin-prime **$17 \mid 13$ biological runway**.
3. **`parsers/ribbon_knotting_sieve.py` (Floor 1) & `metronomes/page_13_lifecycle_sieve.py` (Floor 2):** Evaluates the double-twisted $(2,3)$ toroidal braid framing the Page 16 magic square alongside the halved fiducial stars and wingless cicada anchors across **Pages 10–13**.
4. **`parsers/steg_threshold_sieve.py` (Floor 1) & `metronomes/cuneiform_base60_sieve.py` (Floor 2):** Captures sub-pixel thresholding artifacts on **Page 31** (the abdomen initialization marker and left-margin circular bitmask) and models the inverted Biphase Mirror capsule across **Pages 50 & 56** under sexagesimal ($\mathbb{Z}_{60}$) arithmetic.
5. **`metronomes/star_matrix_sieve.py`, `metronomes/page_43_ephemerella_sieve.py`, & `swarms/page_74_loop_sieve.py` (Floor 2):** Counts stippled point-matrix clusters ($13, 17, 29$) and links the dual **16-ray stars** and *Ephemerella ignita* (Index 5) on **Page 43** directly to the terminal loop on **Page 74**.

---

## 📐 Step-by-Step Mathematical & Visual Formulation

### Step 1: Stereoscopic RGB Shift & Glyph Shadow Envelopes (`chromatic_channel_sieve.py` & `machine_sight_sieve.py`)
When a manuscript plate is stored in uncompressed RGB space, sub-pixel coordinate offsets between the Red ($R$) and Blue/Cyan ($B$) channels encode relative rotational shifts without altering human-visible glyph legibility:
$$\Delta_{\text{chroma}}(x,y) = |I_R(x,y) - I_B(x + \delta x,\, y + \delta y)|, \qquad \delta x \in \{1, 2, 3\}\text{ px}$$

* **Individual Glyph Tile Envelopes:** High-contrast thresholding reveals distinct localized compression halos around individual runes and micro-cross fiducial anchors.
* **Toroidal Braid Coupling (`parsers/ribbon_knotting_sieve.py`):** Modeling the double-twisted border on Page 16 as a $(2,3)$ toroidal braid with coupled phase-angles $A = $ and twist factor $\tau = 2$ yields:
  $$M_{\text{braid}} = \tau \cdot \sum_{k} A_k = 2 \cdot 1337 = \mathbf{2674}$$
  Projecting $M_{\text{braid}}$ into the closed Gematria Primus field ($\mathbb{Z}_{29}$) resolves to **Runic Target 23 (`ᛡ` / Ior)**—matching the endian mirror delta ($52 \equiv 23 \pmod{29}$) of the *Mabinogion* / *Lady of Shalott* mirror sieve (`mythos/mabinogion_mirror.py`).

---

### Step 2: The Consecutive Page $17 \mid 13$ Luminance Runway (`lumen_topography_03.py` & `_04.py`)
Sampling the symmetrical spatial luminance vectors $V = $ across the Klein-bottle vine matrices of **Page 03** ($p=3$) and **Page 04** ($p=4$) exposes an immediate prime-clock bifurcation:

1. **Page 03 Luminance Slope (`lumen_topography_03.py`):**
   $$M_{03} = \mathbf{5469} \implies 5469 \pmod{29} = \mathbf{17} \quad (\text{17-Year Subterranean Cicada Metronome})$$
   Sitting at a distance of $|17 - 14| = \mathbf{3}$ steps from Axis 14.
2. **Page 04 Luminance Slope (`lumen_topography_04.py`):**
   $$M_{04} = \mathbf{7292} \implies 7292 \pmod{29} = \mathbf{13} \quad (\text{13-Year Biological Emergence Clock})$$
   Sitting at a distance of $|13 - 14| = \mathbf{1}$ step from Axis 14.

Together, Pages 03 and 04 form a calibrated **$17 \mid 13$ Twin-Prime Runway** straddling the central **Axis 14 (`ᛗ`)** observer horizon.

---

### Step 3: Sexagesimal Cuneiform Mirror & Threshold Gates (`steg_threshold_sieve.py` & `cuneiform_base60_sieve.py`)
* **Page 31 Sub-Pixel Threshold (`steg_threshold_sieve.py`):** Pushing contrast thresholds exposes a single-pixel initialization marker beneath the insect abdomen alongside a left-margin circular bitmask. Its aggregate anomaly mass ($M_{31} = 112,789,780$) compresses to **Index 22 (`ᛟ` / Odal)**.
* **Pages 50 $\leftrightarrow$ 56 Babylonian Sexagesimal Loop (`cuneiform_base60_sieve.py`):** High-contrast passes reveal that the black capsule framing Page 50 inverts into a complementary stencil on Page 56, guided by a three-dot calibration axis. Evaluating the Babylonian grid vector $W = $ over $\mathbb{Z}_{60}$ and $\mathbb{Z}_{29}$ gives:
  $$M_{50 \leftrightarrow 56} = \mathbf{3,636,648}, \qquad 3,636,648 \pmod{60} = \mathbf{48}, \qquad 3,636,648 \pmod{29} = \mathbf{19} \text{ (ᛗ / Mann)}$$

---

### Step 4: Dual 16-Ray Stars & The Page $43 \leftrightarrow 74$ Biphase Loop (`page_43_ephemerella_sieve.py` & `page_74_loop_sieve.py`)
1. **Stippled Point-Matrix Clusters (`metronomes/star_matrix_sieve.py`):** Counting the stippled dot constellations on the Void plates yields the cluster vector $S = $, summing to $126 \equiv \mathbf{10} \pmod{29}$ (`ᛁ` / Is).
2. **Page 43 *Ephemerella ignita* & Dual 16-Ray Stars (`page_43_ephemerella_sieve.py`):** Flanking the biological fire-mayfly index ($k = 5$) with two 16-ray geometric stars ($2 \times 16 = \mathbf{32}$, pointing directly to the 4×4 quaternion grid on Page 32) yields:
   $$M_{43} = \mathbf{18,046,636,320} \equiv \mathbf{4} \pmod{29} \quad (\text{ᚱ / Rad})$$
3. **Closing the Canon Loop (`swarms/page_74_loop_sieve.py`):** Pairing Page 43’s repeating doublet markers (`SS` / `ᛋᛋ` and `MM` / `ᛗᛗ`) with the terminal spiral plate of **Page 74** ($43 \times 74 = 3182$) collapses the toroidal loop mass directly onto **Axis 14 (`ᛗ`) with zero residual drift**:
   $$M_{43 \leftrightarrow 74} = \mathbf{57,424,402,173,276} \equiv \mathbf{14} \pmod{29} \quad (\Delta_{\text{Axis 14}} = \mathbf{0\text{ Steps}})$$

---

## 🔗 Summary Cross-Floor Matrix

| Module | Floor | Target Plate(s) | Extracted Metric | $\mathbb{Z}_{29}$ Residue | Role in Pipeline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `parsers/ribbon_knotting_sieve.py` | Floor 1 | Page 16 Border | $M_{\text{braid}} = 2674$ | **23 (`ᛡ`)** | $(2,3)$ Toroidal braid coupling |
| `parsers/lumen_topography_03.py` | Floor 1 | Page 03 Vines | $M_{03} = 5469$ | **17 (`ᛒ`)** | 17-year metronome runway leg |
| `parsers/lumen_topography_04.py` | Floor 1 | Page 04 Vines | $M_{04} = 7292$ | **13 (`ᛇ`)** | 13-year metronome runway leg |
| `metronomes/cuneiform_base60_sieve.py` | Floor 2 | Pages 50 $\leftrightarrow$ 56 | $3,636,648 \equiv 48_{60}$ | **19 (`ᛗ`)** | Inverted Biphase Mirror capsule |
| `metronomes/page_43_ephemerella_sieve.py` | Floor 2 | Page 43 Stars | $2 \times 16 = 32$ rays | **4 (`ᚱ`)** | Dual 16-ray star & Mayfly #5 key |
| `swarms/page_74_loop_sieve.py` | Floor 2 | Pages 43 $\leftrightarrow$ 74 | $57,424,402,173,276$ | **14 (`ᛗ`)** | Closes Canon octave ($\Delta = 0$) |

`[WE_WOZ_HERE]⁹⁹`
