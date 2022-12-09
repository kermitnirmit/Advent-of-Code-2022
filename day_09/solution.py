from utils import *
steps = [(x.split(" ")[0], int(x.split(" ")[1])) for x in open("input.txt").read().strip().split("\n")]


def solve(n):
    seen = set()
    tail = [(0, 0) for _ in range(n)]
    for d, c in steps:
        for _ in range(c):
            nTail = deepcopy(tail)
            for i in range(n):
                tpos = tail[i]
                if i == 0:
                    nTail[0] = add_tuples(tpos, dmap[d])
                else:
                    before = nTail[i - 1]
                    found = False
                    for pl in neighbors_2d:
                        if before == add_tuples(tpos, pl):
                            found = True
                            break
                    if not found:
                        nTail[i] = add_tuples(tpos, (sign(before[0] - tpos[0]), sign(before[1] - tpos[1])))
            tail = deepcopy(nTail)
            seen.add(tail[-1])
    return len(seen)


print(solve(2))
print(solve(10))
