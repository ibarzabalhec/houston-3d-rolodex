# -*- coding: utf-8 -*-
"""Build 70. DFW county outlines from TxDOT's county boundary layer.

The research pack drew DFW's counties from Census 1:5,000,000 cartographic
files, the coarsest the Census publishes, cut to 30 to 108 points a county.
Rivers came out as straight lines and neighbouring counties did not share a
border, so the map read as a sketch next to Houston's.

These are TxDOT's outlines, the same layer as Houston's
(gis-txdot.opendata.arcgis.com, Texas County Boundaries), downloaded as
txdot_dfw_counties.geojson and simplified the way Houston's were: to about 130
metres, rounded to three decimals.

The simplification works on shared borders, not on counties. Each ring is cut
into arcs wherever the set of counties it bounds changes. Every arc is simplified
once, and each county that shares it gets the same points. Two neighbours
therefore draw one seam, not two lines that almost meet.

Lakes come from TxDOT's Texas Water Bodies layer (owner TXDOT_GIS), queried for
water bodies above 1,000 acres that are not a stream or a dam, in WGS84, at the
service's own 0.0002 degree generalisation. A lake is kept if any of its points
falls inside the eleven counties, and the page clips it to them. That leaves 17,
from Lake Lewisville and Ray Hubbard to Tawakoni and Cedar Creek, which reach
into the metro from outside. txdot_dfw_lakes.geojson records the query.

Lakes are simplified to 200 metres, under a pixel at the size the map draws. An island under a square kilometre,
about three pixels across at the size the map draws, is left as water.

    python3 dfw/geo/outline.py      writes dfw/geo/outlines.json and water.json
"""
import json, math, pathlib

HERE = pathlib.Path(__file__).parent
TOL_M = 130.0
MIN_KM2 = 1.0
WATER_TOL_M = 200.0


def key(p):
    return (round(p[0], 7), round(p[1], 7))


def dp(pts, tol, lat0):
    """Douglas-Peucker in metres on a local equirectangular projection."""
    kx = 111320.0 * math.cos(math.radians(lat0))
    ky = 110540.0
    xy = [(p[0] * kx, p[1] * ky) for p in pts]
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = xy[a]; bx, by = xy[b]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy)
        best, bi = -1.0, None
        for i in range(a + 1, b):
            px, py = xy[i]
            d = (abs(dy * px - dx * py + bx * ay - by * ax) / L) if L else math.hypot(px - ax, py - ay)
            if d > best:
                best, bi = d, i
        if bi is not None and best > tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def main():
    src = json.load(open(HERE / "txdot_dfw_counties.geojson", encoding="utf-8"))
    rings = {}
    names = {}
    for f in src["features"]:
        fips = f["properties"]["FIPS_ST_CNTY_CD"]
        names[fips] = f["properties"]["CNTY_NM"]
        g = f["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        rings[fips] = [p[0] for p in polys]          # outer rings; no county here has a hole
    own = {}
    for fips, rs in rings.items():
        for r in rs:
            for p in r:
                own.setdefault(key(p), set()).add(fips)
    lat0 = sum(p[1] for rs in rings.values() for r in rs for p in r) / sum(len(r) for rs in rings.values() for r in rs)
    cache = {}

    def simplify_arc(arc):
        k = tuple(key(p) for p in arc)
        if k in cache:
            return cache[k]
        rk = k[::-1]
        if rk in cache:
            return cache[rk][::-1]
        s = dp(arc, TOL_M, lat0)
        cache[k] = s
        return s

    out = []
    for fips, rs in rings.items():
        polys = []
        for r in rs:
            r = r[:-1] if key(r[0]) == key(r[-1]) else r[:]
            n = len(r)
            mem = [frozenset(own[key(p)]) for p in r]
            # a vertex is a junction where the set of counties it bounds changes
            junction = [mem[i] != mem[i - 1] or mem[i] != mem[(i + 1) % n] for i in range(n)]
            if not any(junction):
                junction[0] = True
            start = junction.index(True)
            r = r[start:] + r[:start]
            junction = junction[start:] + junction[:start]
            idx = [i for i, j in enumerate(junction) if j] + [n]
            pts = []
            for a, b in zip(idx, idx[1:]):
                arc = [r[i % n] for i in range(a, b + 1)]
                s = simplify_arc(arc)
                pts += s[:-1]
            ring = []
            for x, y in pts:
                q = [round(x, 3), round(y, 3)]
                if not ring or ring[-1] != q:
                    ring.append(q)
            ring.append(ring[0])
            polys.append([ring])
        out.append({"fips": fips, "name": names[fips], "rings": polys})
    out.sort(key=lambda g: g["name"])
    json.dump(out, open(HERE / "outlines.json", "w"), separators=(",", ":"))
    for g in out:
        print("%-10s %4d points" % (g["name"], sum(len(r) for p in g["rings"] for r in p)))


def area_km2(r, lat0):
    kx = 111.320 * math.cos(math.radians(lat0)); ky = 110.540
    a = 0.0
    for (x0, y0), (x1, y1) in zip(r, r[1:] + r[:1]):
        a += (x0 * kx) * (y1 * ky) - (x1 * kx) * (y0 * ky)
    return abs(a) / 2


def water():
    src = json.load(open(HERE / "txdot_dfw_lakes.geojson", encoding="utf-8"))
    out = []
    for f in src["features"]:
        g = f["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        keep = []
        for poly in polys:
            rings = []
            for i, r in enumerate(poly):
                lat0 = sum(p[1] for p in r) / len(r)
                if area_km2(r, lat0) < MIN_KM2:
                    continue
                if i and not rings:
                    break                      # the outer ring was too small; so are its islands
                s = dp(r, WATER_TOL_M, lat0)
                q = []
                for x, y in s:
                    c = [round(x, 3), round(y, 3)]
                    if not q or q[-1] != c:
                        q.append(c)
                if len(q) >= 4:
                    rings.append(q)
            if rings:
                keep.append(rings)
        if keep:
            out.append({"name": f["properties"]["name"], "acres": f["properties"]["acres"], "rings": keep})
    out.sort(key=lambda w: -w["acres"])
    json.dump(out, open(HERE / "water.json", "w"), separators=(",", ":"))
    for w in out:
        print("%-24s %6d acres %4d points, %d islands" % (w["name"], w["acres"],
              sum(len(r) for p in w["rings"] for r in p), sum(len(p) - 1 for p in w["rings"])))


if __name__ == "__main__":
    main()
    water()
