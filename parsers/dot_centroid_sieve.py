import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

FIBS = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def extract_dots(path, area_min=12, area_max=300, round_min=0.45):
    im = Image.open(path).convert("L")
    w, h = im.size
    a = np.asarray(im, float)
    bg = np.asarray(im.filter(ImageFilter.GaussianBlur(25)), float)
    ink = (a / np.maximum(bg, 1)) < 0.72
    lab, n = ndimage.label(ink)
    if n == 0:
        return np.zeros((0, 2)), w, h, ink
    areas = ndimage.sum(ink, lab, range(1, n + 1))
    cy, cx = zip(*ndimage.center_of_mass(ink, lab, range(1, n + 1)))
    cy, cx = np.array(cy), np.array(cx)
    objs = ndimage.find_objects(lab)
    dots = []
    for i, sl in enumerate(objs):
        ar = areas[i]
        if not (area_min <= ar <= area_max):
            continue
        hh = sl[0].stop - sl[0].start
        ww = sl[1].stop - sl[1].start
        if hh == 0 or ww == 0:
            continue
        ecc = max(hh, ww) / min(hh, ww)
        fill = ar / (hh * ww)
        if ecc > 1 / 0.45 or fill < 0.45:
            continue
        dots.append((cx[i], cy[i]))
    return np.array(dots), w, h, ink


def rows_from_y(ys):
    ys = np.sort(ys)
    if len(ys) < 2:
        return ys.reshape(-1, 1)
    gaps = np.diff(ys)
    med = np.median(gaps) if len(gaps) else 1
    thr = 0.5 * max(med, 1e-9)
    rows, cur = [], [ys[0]]
    for v in ys[1:]:
        if v - cur[-1] > thr:
            rows.append(cur)
            cur = [v]
        else:
            cur.append(v)
    rows.append(cur)
    return np.array([np.mean(r) for r in rows]), np.array([len(r) for r in rows])


def fibo_run(counts):
    best, cur = 0, 0
    fs = set(FIBS)
    for i, c in enumerate(counts):
        if c in fs and (i == 0 or c in fs and (
                counts[i - 1] in fs and FIBS.index(c) == FIBS.index(counts[i - 1]) + 1)):
            cur = cur + 1 if (i > 0 and counts[i - 1] in fs and
                              FIBS.index(c) == FIBS.index(counts[i - 1]) + 1 and cur > 0) else 1
        else:
            cur = 1 if c in fs else 0
        best = max(best, cur)
    return best


def even_run(counts, k):
    return sum(1 for c in counts if c % 2 == 0) / max(k, 1)


def nn_gaps(pts):
    if len(pts) < 2:
        return np.array([])
    d = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(-1))
    np.fill_diagonal(d, np.inf)
    return d.min(axis=1)


def even_gap_frac(gaps):
    if len(gaps) < 3:
        return 0.0
    med = np.median(gaps)
    if med <= 0:
        return 0.0
    r = gaps / med
    k = r / 2
    frac = np.abs(k - np.round(k)) <= 0.35 * 0.5
    return float(even_frac := frac.mean())


def stats_for(pts, w, h):
    x1, x2 = 0.15 * w, 0.55 * w
    y1, y2 = 0.15 * h, 0.70 * h
    reg = pts[(pts[:, 0] >= x1) & (pts[:, 0] <= x2) & (pts[:, 1] >= y1) & (pts[:, 1] <= y2)]
    out = {"n_region": len(reg)}
    if len(reg) < 4:
        out.update({"counts": [], "n_rows": 0})
        return out
    ys, counts = rows_from_y(reg[:, 1])
    out["rows"] = counts.tolist()
    out["fibo_run"] = fibo_run(counts.tolist())
    out["even_frac_rows"] = even_run(counts.tolist(), len(counts))
    g = nn_gaps(reg)
    out["even_gap_frac"] = even_gap_frac(g)
    out["count_mod29"] = len(reg) % 29
    return out


def mc_shuffle(region_pts, x1, x2, y1, y2, iters=1000):
    n = len(region_pts)
    rng = np.random.default_rng(2026)
    nulls = {"fibo": [], "even_rows": [], "gap": [], "mod14": 0}
    for _ in range(iters):
        px = rng.uniform(x1, x2, n)
        py = rng.uniform(y1, y2, n)
        p = np.stack([px, py], 1)
        ys, counts = rows_from_y(p[:, 1])
        nulls["fibo"].append(fibo_run(counts.tolist()))
        nulls["even_rows"].append(even_run(counts.tolist(), len(counts)))
        nulls["gap"].append(even_gap_frac(nn_gaps(p)))
    return {k: np.array(v) for k, v in nulls.items()}


def report(path):
    pts, w, h, ink = extract_dots(path)
    x1, x2, y1, y2 = 0.15 * w, 0.55 * w, 0.15 * h, 0.70 * h
    S = stats_for(pts, w, h)
    print(f"=== {path} | page {w}x{h} | total extracted dots: {len(pts)} ===")
    print(f"region dots: {S.get('n_region', 0)} | rows: {S.get('n_rows', len(S.get('rows', [])))}")
    print(f"row counts (top->bottom): {S.get('rows')}")
    print(f"H-Fibo max consecutive-fib run: {S.get('fibo_run', 0)} (need >=3)")
    print(f"H-Even(a) fraction even row counts: {S.get('even_frac_rows', 0):.3f} (need >=0.75)")
    print(f"H-Even(b) even-gap fraction: {S.get('even_gap_frac', 0):.3f} (need >=0.75)")
    print(f"H-14 region count mod 29: {S.get('count_mod29')} (need ==14)")
    reg = pts[(pts[:, 0] >= x1) & (pts[:, 0] <= x2) & (pts[:, 1] >= y1) & (pts[:, 1] <= y2)]
    if len(reg) >= 4:
        N = mc_shuffle(reg, x1, x2, y1, y2, 1000)
        p_fibo = float((N["fibo"] >= S.get("fibo_run", 0)).mean())
        p_even = float((N["even_rows"] >= S.get("even_frac_rows", 0)).mean())
        p_gap = float((N["gap"] >= S.get("even_gap_frac", 0)).mean())
        print(f"p-values vs shuffled null (x1000): fibo={p_fibo:.4f} even_rows={p_even:.4f} even_gap={p_gap:.4f}")
        print(f"H-14 single-trial null p = 1/29 = {1/29:.4f}")
    return S


if __name__ == "__main__":
    for p in sys.argv[1:]:
        report(p)
        print()
