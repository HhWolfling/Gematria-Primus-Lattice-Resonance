#!/usr/bin/env python3
"""
Module: dot_region_wager.py
Description: Scoring instrument for W-002 (locked 2026-11-23, commit after
             `parsers/dot_centroid_sieve.py`, which it imports unmodified).
             Region: x full width, y in [50%, 100%] (bottom half).
             Branches (four-branch correction, per-branch p < 0.0125):
               W2-POW2   : >=75% of row-band counts are powers of two
                           from {2,4,8,16,32,64}
               W2-MULT4  : >=75% of row-band counts are multiples of 4
               W2-COUNT24: number of single-linkage spatial clusters
                           (linkage 1.5 x median NN gap) == 24
               W2-24MOD  : total region dot count == 24 (mod 29)
             Nulls: position shuffle x1000 (seed 2026); synthetic uniform
             field matched intensity; transfer control page 11.
"""
import sys
import numpy as np
from scipy import ndimage

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from dot_centroid_sieve import extract_dots, rows_from_y, nn_gaps  # frozen W-001 extraction

POW2 = {2, 4, 8, 16, 32, 64}


def region_pts(pts, w, h, xr=(0.0, 1.0), yr=(0.50, 1.00)):
    x1, x2 = xr[0] * w, xr[1] * w
    y1, y2 = yr[0] * h, yr[1] * h
    m = (pts[:, 0] >= x1) & (pts[:, 0] <= x2) & (pts[:, 1] >= y1) & (pts[:, 1] <= y2)
    return pts[m], x1, x2, y1, y2


def rowband_stats(reg):
    ys, counts = rows_from_y(reg[:, 1])
    n = len(counts)
    frac_pow2 = sum(1 for c in counts if c in POW2) / max(n, 1)
    frac_mult4 = sum(1 for c in counts if c % 4 == 0) / max(n, 1)
    return counts, frac_pow2, frac_mult4


def spatial_clusters(pts, factor=1.5):
    if len(pts) < 2:
        return len(pts)
    g = nn_gaps(pts)
    med = np.median(g)
    if med <= 0:
        return len(pts)
    thr = factor * med
    from scipy.spatial import cKDTree
    t = cKDTree(pts)
    pairs = t.query_pairs(thr, output_type="ndarray")
    parent = list(range(len(pts)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for a, b in pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return len({find(i) for i in range(len(pts))})


def shuffle_null(reg, x1, x2, y1, y2, iters=1000):
    n = len(reg)
    rng = np.random.default_rng(2026)
    pow2, mult4, clus = [], [], []
    for _ in range(iters):
        p = np.stack([rng.uniform(x1, x2, n), rng.uniform(y1, y2, n)], 1)
        _, fp, fm = rowband_stats(p)
        pow2.append(fp)
        mult4.append(fm)
        clus.append(spatial_clusters(p))
    return np.array(pow2), np.array(mult4), np.array(clus)


def synthetic_null(intensity, w, h, iters=1000):
    rng = np.random.default_rng(2026)
    n = max(int(round(intensity * (yfrac := 0.5) * w * h)), 4)
    pow2, mult4, clus = [], [], []
    for _ in range(iters):
        p = np.stack([rng.uniform(0, w, n), rng.uniform(0.5 * h, h, n)], 1)
        _, fp, fm = rowband_stats(p)
        pow2.append(fp)
        mult4.append(fm)
        clus.append(spatial_clusters(p))
    return np.array(pow2), np.array(mult4), np.array(clus)


def run(path):
    pts, w, h, ink = extract_dots(path)
    reg, x1, x2, y1, y2 = region_pts(pts, w, h)
    print(f"=== {path.split('/')[-1]} | page {w}x{h} | extracted dots {len(pts)} | in-region {len(reg)}")
    if len(reg) < 4:
        print("[!] fewer than 4 in-region dots — W-002 not scoreable on this artifact")
        return
    counts, fp, fm = rowband_stats(reg)
    nclusters = spatial_clusters(reg)
    mod = len(reg) % 29
    print(f"row-band counts (top->bottom): {counts.tolist()}")
    print(f"W2-POW2   frac counts in powers of 2 : {fp:.3f}  (need >= 0.75)")
    print(f"W2-MULT4  frac counts multiple of 4  : {fm:.3f}  (need >= 0.75)")
    print(f"W2-COUNT24 spatial clusters          : {nclusters} (need == 24)")
    print(f"W2-24MOD  total region count mod 29  : {mod} (need == 24)")

    P2, M4, C = shuffle_null(reg, x1, x2, y1, y2)
    S2, S4, SC = synthetic_null(len(pts) / (w * h), w, h)
    print("-- nulls (shuffle x1000 | synthetic x1000) --")
    print(f"POW2   p: {(P2 >= fp).mean():.4f} | {(S2 >= fp).mean():.4f}")
    print(f"MULT4  p: {(M4 >= fm).mean():.4f} | {(S4 >= fm).mean():.4f}")
    obs_d = abs(nclusters - 24)
    print(f"COUNT24 p: {(np.abs(C - 24) <= obs_d).mean():.4f}   "
          f"(null clusters median {np.median(C):.0f}) | synthetic median {np.median(SC):.0f}")
    print(f"24MOD  null p: 1/29 = {1 / 29:.4f} per realization family")
    print("corrected decision rule: branch p < 0.0125")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        run(p)
        print()
