from  utils import ints, _neighbors_3d

f = [x for x in open("input.txt").read().strip().split("\n")]


points = set()

for line in f:
    x,y,z = ints(line)
    points.add((x,y,z))

print(sum(6 - sum(q in points for q in _neighbors_3d(point)) for point in points))
knownout = set()
trapped = set()

def getout(point):
    if point in knownout:
        return True
    if point in trapped:
        return False
    s = set()
    q = [point]
    while q:
        curr = q.pop(0)
        if curr not in points and curr not in s:
            s.add(curr)
            if len(s) > 2000: #searching a ton and couldnt get stuck inside
                knownout.update(s)
                return True
            q.extend(_neighbors_3d(curr))
    # if queue's done, we've seen things that are trapped
    trapped.update(s)
    return False
print(sum(sum(getout(q) for q in _neighbors_3d(point)) for point in points))
