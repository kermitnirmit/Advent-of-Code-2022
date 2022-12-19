import time

from tqdm import tqdm, trange
from  parse import parse
from utils import *
from heapq import heappush, heappop
from collections import defaultdict, Counter
from itertools import combinations
import numpy as np


f = open("input.txt").read().strip().split("\n")
# f = open("test.txt").read().strip().split("\n")

class Valve:
    def __init__(self, tunnels, flowRate):
        self.tunnels = tunnels
        self.flowRate = flowRate
# Valve VG has flow rate=15; tunnels lead to valves XZ, FT, PF, TF, LG


d = {}

edges = {}

for line in f:
    # print(line)
    q = line.split("Valve ")
    # print(q)
    valveName = q[1][:2]
    w = ints(line)[0]
    t = line.split("tunnel lead to valves")
    t = [x.strip() for x in t[1].split(", ")]

    # print(t)
    # print(valveName, w, t)

    d[valveName] = w
    edges[valveName] = t




    # best = max(best, recurse(cur, opened, time + 1))
    # return best

def dist(a,b):
    seen = set()
    q = [(a, 0)]
    while q:
        curr, distSoFar = q.pop(0)
        if b in edges[curr]:
            return distSoFar + 1
        else:
            for n in edges[curr]:
                if n not in seen:
                    seen.add(n)
                    q.append((n, distSoFar + 1))


dists = {}
for r1 in d.keys():
    for r2 in d.keys():
        if r1 != r2:
            dists[(r1, r2)] = dist(r1, r2)

# def solve():
#     asdf = 0
#     def recurse(cur, opened, sofar, time):
#         nonlocal asdf
#         if sofar > asdf:
#             asdf = sofar
#         if time >= maxTime:
#             return
#         if cur not in opened:
#             recurse(cur, tuple(opened + (cur,)), sofar + ((maxTime - time) * d[cur]), time + 1)
#         else:
#             for room in d:
#                 if room not in opened:
#                     recurse(room, opened, sofar, dists[(cur, room)] + time)
#
#     recurse("AA", (), 0, 1)
#     print(asdf)
# solve()


nonzeros = []
for k,v in d.items():
    if v != 0:
        nonzeros.append(k)

print(len(nonzeros))



# subsets =


maxTime = 30
m = 0
@functools.lru_cache(maxsize=None)
def recurse(cur, opened, time):
    if time > maxTime:
        # print(cur, opened, time)
        return 0
    best = 0
    if cur not in opened: # open it! and go or just don't
        # print(cur, opened, time)
        v = d[cur] * (maxTime - (time + 1)) # value of opening it
        possibles = [x for x in d.keys() if x not in opened and x != cur and d[x] > 0]
        for n in possibles:
            distance = dists[(cur, n)]
            if v != 0: # some use in opening it
                best = max(best, v + recurse(n, tuple(sorted(opened + (cur,))), time + 1 + distance))
            best = max(best, recurse(n, opened, time + distance))
    return best
before = time.time()
# p1 = recurse("AA", (), 0)
after = time.time()
# print("p1", p1, "time: ", after-before)

maxTime = 26
@functools.lru_cache(maxsize=None)
def recurse2(cur, opened, time):
    if time > maxTime:
        # print(cur, opened, time)
        return recurse("AA", opened, 0)
    best = 0
    if cur not in opened: # open it! and go or just don't
        # print(cur, opened, time)
        v = d[cur] * (maxTime - (time + 1)) # value of opening it
        possibles = [x for x in d.keys() if x not in opened and x != cur and d[x] > 0]
        for n in possibles:
            distance = dists[(cur, n)]
            if v != 0: # some use in opening it
                best = max(best, v + recurse2(n, tuple(sorted(opened + (cur,))), time + 1 + distance))
            best = max(best, recurse2(n, opened, time + distance))
    return best
before = time.time()
# p2 = recurse2("AA", (), 0)
after = time.time()
# print("p2", p2, "time: ", after-before)

# leaving my failures here :D

# print(d)
#
# print(edges)

# q = []
# # heap is curr value, curr place, dvalue
# heappush(q, (0, "AA", 0, 0, []))

# lowest = 0
# print(d.items())
# # curr and dval
# seen = set()
# seen.add(("AA", 0, 0))
# lows = []
# while q:
#     val, curr, dval, time, opens = heappop(q)
#     # print(val, curr, dval, time, opens)
#     # input("continue")
#     if time == 10:
#         # print("made it?")
#         # print(dval)
#         # print(val, dval, opens, "curr:", curr)
#         lowest = min(val, lowest)
#         lows.append(dval)
#     else:
#         # you're at an open one so move!
#         # if opens == ["DD", "BB"]:
#         #     print(val + dval)
#         if curr in opens:
#             for n in edges[curr]:
#                 if (val, n, dval, time + 1, "".join(sorted(opens))) not in seen:
#                     seen.add((val, n, dval, time + 1, "".join(sorted(opens))))
#                     heappush(q, (val + dval, n, dval, time + 1, opens))
#         else:
#             # move without opening!
#             for n in edges[curr]:
#                 if (val, n, dval, time + 1, "".join(sorted(opens))) not in seen:
#                     seen.add((val, n, dval, time + 1, "".join(sorted(opens))))
#                     heappush(q, (val + dval, n, dval, time + 1, opens))
#             # open it
#             heappush(q, (val + dval, curr, dval - d[curr], time + 1, opens + [curr]))
#             # heappush(q, (val + dval, curr, dval, time + 1, opens))
#
# lowest = 0
# print(d.items())
# # curr and dval
# seen = set()
# # seen.add(("AA", 0, ""))
# seen.add((0, "AA", 0, ""))
# lows = []
# q = []
# heappush(q, (0, "AA", 0, []))
# end = 15

# dp = []
#
# all_combs = []
# for i in range(15):
#     for pos in combinations(d.keys(), i):
#         all_combs.append(pos)
#



# for _ in range(time): # for each time
#     w = []
#     for _ in range(len(d)): # for each place you can stand
#         e = []
#         for _ in range(len(all_combs)):
#             e.append(-10000000)
#         w.append(e)
#     dp.append(w)

#
# time = 2
# dp = np.zeros((time + 1, len(d), len(all_combs)))
#
# print(dp.shape)
#
#
# standings = list(d.keys())
# print(standings.index("AA"))
#
# # print("index = ", all_combs.index(("AA",)))
# dp[0][0][1] = 0
#
#
# print(("CC","BB") in all_combs)

# print("can you add like this", (all_combs[3] + all_combs[5]) in all_combs)
# print(1)


# queue = [(0,0,0)]
#
# while queue:
#     i,j,k = queue.pop(0)
#     # print("at time:", i)
#     # print("standing at: ", standings[j])
#     # print("with these open:", all_combs[k])
#     # print("val = ", dp[i][j][k])
#     # input("continue")
#     # print(standings[j])
#     # print("with these open:", all_combs[k])
#     for j2 in range(len(d)):
#         # how long does it take you?
#         curr = standings[j]
#         next = standings[j2]
#         if curr != next and next not in all_combs[k]:
#             di = dist(curr, next)
#             newK = tuple(sorted(all_combs[k] + (next,)))
#             newK = all_combs.index(newK)
#             # print(all_combs[k], next, newK)
#             howMuchGain = 0
#             for opened in list(all_combs[k]):
#                 howMuchGain += d[opened]
#
#             if i >= 2 or howMuchGain > 20:
#                 print(howMuchGain, all_combs[k], "going to:", next)
#                 input("continue")
#             if i + di + 1 <= time:
#                 # print("going to and opening", next)
#                 dp[i + di + 1][j2][newK] = max(dp[i + di + 1][j2][newK], dp[i][j][k] + (howMuchGain * (di + 1)))
#                 queue.append((i + di + 1, j2, newK))
#     # or go nowhere
#     howMuchGain = 0
#     for opened in list(all_combs[k]):
#         howMuchGain += d[opened]
#     if i + 1 <= time:
#         dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + howMuchGain)
#         queue.append((i + 1, j, k))
#

# for i in trange(time):
#     for j in range(len(d)):
#         for k in range(len(all_combs)):
#             # where can you go?
#             for j2 in range(len(d)):
#                 # how long does it take you?
#                 curr = standings[j]
#                 next = standings[j2]
#                 if curr != next and next not in all_combs[k]:
#                     di = dist(curr, next)
#                     newK = tuple(sorted(all_combs[k] + (next,)))
#                     newK = all_combs.index(newK)
#                     # print(all_combs[k], next, newK)
#                     howMuchGain = 0
#                     for opened in list(all_combs[k]):
#                         howMuchGain += d[opened]
#                     # print(howMuchGain)
#                     if i + di + 1 <= time:
#                         dp[i + di + 1][j2][newK] = max(dp[i + di + 1][j2][newK], dp[i][j][k] + (howMuchGain * (di + 1)))
#             # or go nowhere
#             howMuchGain = 0
#             for opened in list(all_combs[k]):
#                 howMuchGain += d[opened]
#             dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k] + howMuchGain)
# print("done?")
# print("max", np.max(dp))
# print((dp.flatten()[np.argmax(dp)]))



# print(dist("AA", "FF"))

# x y z
# x = time x
# y = at y
# z open


# while q:
#     val, curr, time, opens = heappop(q)
#
#     if time == end:
#         lowest = min(val, lowest)
#         print("ends: ", val, lowest)
#         # print("opens:", opens, "val: ", val)
#     else:
#         # already open so move
#         if curr in opens:
#             for n in edges[curr]:
#                 if (val, n, "".join(sorted(opens))) not in seen:
#                     heappush(q, (val, n, time + 1, opens))
#         else:
#             for n in edges[curr]:
#                 if (val, n, "".join(sorted(opens))) not in seen:
#                     heappush(q, (val, n,time + 1, opens))
#             # open
#             nval = val - ((end - (time + 1)) * d[curr])
#             if (nval, curr, "".join(sorted(opens + [curr]))) not in seen:
#                 heappush(q, (nval, curr, time + 1, opens + [curr]))
# # print(min(lows))
# print(lowest * -1)


    # a, flow, t
