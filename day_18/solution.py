from  utils import ints, _neighbors_3d

# f = [x for x in open("input.txt").read().strip().split("\n")]
f = [x for x in open("test.txt").read().strip().split("\n")]


points = {tuple(ints(l)) for l in f}

print(sum(6 - sum(q in points for q in _neighbors_3d(point)) for point in points))
knownout, trapped = set(), set()

def getout(point):
    if point in knownout: #priorly proven this is far out, we don't need to keep exploring
        return True
    if point in trapped: #priorly proven this is inside! we don't need to keep exploring
        return False
    s = set()
    q = [point]
    while q:
        curr = q.pop(0)
        if curr not in points and curr not in s:
            s.add(curr)
            if len(s) > 2000: #searching a ton and couldnt get stuck inside
                knownout.update(s) #add all the ones we've seen in this search to the "what's outside set"
                return True
            q.extend(_neighbors_3d(curr)) # add all of its neighbors to the queue
    trapped.update(s) # if queue's done, we've seen things that are trapped
    return False


print(sum(sum(getout(q) for q in _neighbors_3d(point)) for point in points))
