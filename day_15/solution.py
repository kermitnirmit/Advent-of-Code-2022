
from tqdm import tqdm, trange
from  parse import parse
f = open("input.txt").read().strip().split("\n")
# f = open("test.txt").read().strip().split("\n")

def mandist(x,y, q,w):
    return abs(q-x) + abs(w - y)

d = {}

minx = 1000000000
maxx = -10000000
# mindist = 0
maxdist = 0
beacons = set()
for line in f:
    x,y, q,w = parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line)
    minx = min(minx, x)
    maxx = max(maxx, x)
    dist = mandist(x,y,q,w)
    d[(x,y)] = dist
    beacons.add((q,w))
    maxdist = max(maxdist, dist)

spots = 0
for i in trange(minx - maxdist, maxx + maxdist + 1):
    nearAnySensor = False
    for point, dist in d.items():
        if mandist(point[0], point[1], i, 2000000) <= dist and (i, 2000000) not in beacons:
            nearAnySensor = True
            break
    if nearAnySensor:
        spots += 1
print(spots)


def findoutside(point, dist, m_in, m_ax):
    x,y = point
    p = dist + 1
    q = 0

    result = set()
    while p >= 0:
        if m_in <= x + p <= m_ax and m_in <= y + q <= m_ax and mandist(x, y, (x+p), (y + q)) == dist + 1:
            result.add((x+p, y+q))
        if m_in <= x - p <= m_ax and m_in <= y - q <= m_ax and mandist(x, y, (x - p), (y - q)) == dist + 1:
            result.add((x - p, y - q))
        if m_in <= x - p <= m_ax and m_in <= y + q <= m_ax and mandist(x, y, (x - p), (y + q)) == dist + 1:
            result.add((x - p, y + q))
        if m_in <= x + p <= m_ax and m_in <= y - q <= m_ax and mandist(x, y, (x + p), (y - q)) == dist + 1:
            result.add((x + p, y - q))
        p -= 1
        q += 1
    return list(result)

justoutsidepos = []
for point, dist in tqdm(d.items()):
    justoutsidepos.extend(findoutside(point, dist, 0, 4000000))
for x,y in tqdm(justoutsidepos):
    nearAnySensor = False
    for point, dist in d.items():
        if mandist(point[0], point[1], x, y) <= dist and (x, y) not in beacons:
            nearAnySensor = True
            break
    if not nearAnySensor and (x,y) not in beacons:
        print(x*4000000 + y)
        break

