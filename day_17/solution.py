from tqdm import trange
from collections import defaultdict, Counter

f = open("input.txt").read().strip().split("\n")[0]
# f = open("test.txt").read().strip().split("\n")[0]
shapes = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""
shapes = shapes.split("\n\n")
d = {}
d["####"] = ((0, 0), (0, 0), (1, 0), (2, 0), (3, 0))  # width = 4 and the point is the left most
d["#\n#\n#\n#"] = ((0, 0), (0, 0), (0, 1), (0, 2), (0, 3))  # width = 1 and the point is the bottom one
d["##\n##"] = ((0, 0), (0, 0), (0, 1), (1, 0), (1, 1))  # width = 2 and the point is the bottom left one
d[".#.\n###\n.#."] = ((0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1))  # width = 3 and the point is the bottom left imaginary
d["..#\n..#\n###"] = ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2))  # width = 3 and the point is the bottom left


def solve(iter=2022):
    fin = 0
    c = -1
    placed = set()
    for i in range(7):
        placed.add((i, -1))
    seen_before = defaultdict(list)
    heights = {}
    peaks = {
        0: -1,
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    }
    for i in range(iter):
        j = i % len(shapes)
        currShape = shapes[j]
        sy = c + 3 + 1
        shapeDims = d[currShape]
        go = (2, sy)
        put = False
        while not put:
            inst = f[fin]
            if inst == "<":
                nextpoints = []
                foundIntersect = False
                for n in shapeDims:
                    nextpoints.append((go[0] + n[0] - 1, go[1] + n[1]))
                if len(nextpoints) == 6:
                    nextpoints = nextpoints[1:]
                for point in nextpoints:
                    if point in placed:
                        foundIntersect = True
                if not foundIntersect:
                    go = (max(go[0] - 1, 0), go[1])
            else:
                nextpoints = []
                foundIntersect = False
                for n in shapeDims:
                    nextpoints.append((go[0] + n[0] + 1, go[1] + n[1]))
                if len(nextpoints) == 6:
                    nextpoints = nextpoints[1:]
                for point in nextpoints:
                    if point in placed:
                        foundIntersect = True
                if not foundIntersect:
                    width = max(shapeDims, key=lambda x: x[0])[0]
                    go = (min(go[0] + 1, 7 - width - 1), go[1])
            fin += 1
            fin %= len(f)
            nextpoints = []

            for n in shapeDims:
                nextpoints.append((go[0] + n[0], go[1] + n[1] - 1))
            if len(nextpoints) == 6:
                nextpoints = nextpoints[1:]
            foundIntersect = False
            for point in nextpoints:
                if point in placed:
                    foundIntersect = True
            if foundIntersect:
                s = shapeDims
                if len(shapeDims) == 6:
                    s = shapeDims[1:]
                for point in s:
                    placed.add((go[0] + point[0], go[1] + point[1]))
                    oldVal = peaks[go[0] + point[0]]
                    peaks[go[0] + point[0]] = max(oldVal, go[1] + point[1])
                    c = max(c, go[1] + point[1])
                put = True
            go = (go[0], go[1] - 1)
        vals = list(peaks.values())
        lowestVal = min(vals)
        nvals = []
        for val in vals:
            if lowestVal > 0:
                nvals.append(val - lowestVal)
        nvals = tuple(nvals) + (currShape,)
        seen_before[nvals].append(i)
        heights[i] = c + 1
    diffs = defaultdict(int)
    for k, v in seen_before.items():
        if len(v) > 1:
            for l, r in zip(v[:-1], v[1:]):
                diffs[r - l] += 1
    return c + 1, placed, max(diffs, key=diffs.get), heights


(p1, placed, diff, heights) = solve(2022)
print("p1", p1)
start = 156
cycle = diff
baseline = heights[start]
per_cycle = heights[start + cycle] - baseline
print("p2", baseline + (per_cycle * ((1000000000000 - start) // cycle)) + (heights[start + ((1000000000000 - start) % cycle)] - baseline) - 1)
