import functools
import time

from utils import ints, _neighbors_3d, floats
from collections import defaultdict, Counter, deque


f = [x for x in open("input.txt").read().strip().split("\n")]
# f = [x for x in open("test.txt").read().strip().split("\n")]


a = 0


class Blueprint:
    def __init__(self, id, ore, clay, obBotCost, obclay, gore, gobs):
        self.id = id
        self.ore = ore
        self.clay = clay
        self.obore = obBotCost
        self.obclay = obclay
        self.gore = gore
        self.gobs = gobs

    def __repr__(self):
        return " ".join((str(self.id), str(self.ore), str(self.clay), str(self.obore), str(self.obclay), str(self.gore),
                         str(self.gobs)))


bps = []

for l in f:
    i, o, c, ob, obc, gore, gobs = tuple(ints(l))
    bps.append(Blueprint(i, o, c, ob, obc, gore, gobs))

@functools.lru_cache(maxsize=None)
def solve(part=1):
    scores = []
    maxIndex = len(bps) if part == 1 else 3
    startTime = 24 if part == 1 else 32
    for bp in bps[:maxIndex]:
        state = (startTime, 0, 0, 0, 0, 1, 0, 0, 0,0)
        q = deque([state])
        maxOreSpend = max(bp.ore, bp.clay, bp.obore, bp.gore)
        maxClay = bp.obclay
        best = 0
        s = set()
        tq = time.time()
        while q:
            curr = q.popleft()
            (t, o, c, obs, g, obot, cbot, obsbot, gbot,forbidden) = curr
            if t == 0:
                best = max(g, best)
                continue
            if g + gbot * t + ((t-1) * t) // 2 <= best:
                continue

            obot = min(maxOreSpend, obot)
            cbot = min(maxClay, cbot)
            obsbot = min(bp.gobs, obsbot)
            o = min(o,t * maxOreSpend - obot * (t - 1))  # don't have more  resource than can spend
            c = min(c, t * maxClay - cbot * (t - 1))
            obs = min(obs, t * bp.gobs - obsbot * (t - 1))

            # orebot, claybot, obsidianbot 3 bits
            if (t, o, c, obs, g, obot, cbot, obsbot, gbot) in s:
                continue
            s.add((t, o, c, obs, g, obot, cbot, obsbot, gbot))
            # building a geode bot has to be best right? turns out sometimes no but that's rare
            if o >= bp.gore and obs >= bp.gobs:
                q.append((t - 1, o + obot - bp.gore, c + cbot, obs + obsbot - bp.gobs, g + gbot, obot, cbot, obsbot,
                          gbot + 1, 0))
            else:

                if o >= bp.obore and c >= bp.obclay and (forbidden & 1) == 0:
                    q.append((t - 1, o + obot - bp.obore, c + cbot - bp.obclay, obs + obsbot, g + gbot, obot, cbot,
                              obsbot + 1, gbot, 0))
                    forbidden = forbidden | 1
                if o >= bp.clay and (forbidden & 2) == 0:
                    q.append(
                        (t - 1, o + obot - bp.clay, c + cbot, obs + obsbot, g + gbot, obot, cbot + 1, obsbot, gbot, 0))
                    forbidden = forbidden | 2
                if o >= bp.ore and (forbidden & 4) == 0:
                    q.append((t - 1, o + obot - bp.ore, c + cbot, obs + obsbot, g + gbot, obot + 1, cbot, obsbot, gbot, 0))
                    forbidden = forbidden | 4
                # do nothing
                q.append((t - 1, o + obot, c + cbot, obs + obsbot, g + gbot, obot, cbot, obsbot, gbot, forbidden))
        scores.append(best * bp.id if part == 1 else best)
        tw = time.time()
        print("part:", part, " blueprint: \t", bp.id, " time taken: \t", tw - tq)
    if part == 1:
        return sum(scores)
    p = 1
    for score in scores:
        p *= score
    return p


t1 = time.time()
print(solve(1))
t2 = time.time()
print(t2 - t1)

t1 = time.time()
print(solve(2))
t2 = time.time()
print(t2 - t1)