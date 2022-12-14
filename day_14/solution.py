import functools
import ast
import time
import timeit
from math import prod
from itertools import combinations, permutations, takewhile
import numpy as np
from collections import defaultdict

f = open("input.txt").read().strip().split("\n")
# f = open("test.txt").read().strip().split("\n")

# print(f)

start = (500,0)

rocks = set()

horizontal_rows = []


rows = defaultdict(list)

for line in f:
    # print(line)
    spots = line.split(" -> ")
    xys = []
    for spot in spots:
        q = spot.split(",")
        x,y = int(q[0]), int(q[1])
        xys.append((x,y))
    for (x1,y1), (x2, y2) in zip(xys[:-1], xys[1:]):
        for nx in range(min(x1, x2), max(x1, x2) + 1):
            for ny in range(min(y1, y2), max(y1, y2) + 1):
                rows[ny].append(nx)
                rocks.add((nx, ny))
        if max(x1, x2) - min(x1, x2) >= 2 and y1 == y2:
            horizontal_rows.append((min(x1, x2), max(x1, x2), y1))


sands = set()

lowest_rock = max(x[1] for x in rocks)

def check_below(pos):
    return (pos[0], pos[1] + 1) in rocks or (pos[0], pos[1] + 1) in sands


def check_below_left(pos):
    return (pos[0] - 1, pos[1] + 1) in sands or (pos[0] - 1, pos[1] + 1) in rocks

def check_below_right(pos):
    return (pos[0] + 1, pos[1] + 1) in sands or (pos[0] + 1, pos[1] + 1) in rocks


height = lowest_rock + 2
def solve(p1=True):
    if not p1:
        for i in range(500 - height * 2, 500 + height * 2):
            rocks.add((i, lowest_rock + 2))
    donezo = False
    while not donezo:

        if (500, 0) in sands:
            donezo = True
        not_placed = True
        new_sand = start
        while not_placed:
            if check_below(new_sand):
                # there's a sand below so check left
                if check_below_left(new_sand):
                    # there is a sand below left so check right
                    if check_below_right(new_sand):
                        # then place it right here
                        sands.add(new_sand)
                        # sandsadded.append(new_sand)
                        not_placed = False
                    else:
                        new_sand = (new_sand[0] + 1, new_sand[1])
                else:
                    new_sand = (new_sand[0] - 1, new_sand[1])
            new_sand = (new_sand[0], new_sand[1] + 1)
            if new_sand[1] > lowest_rock + 2 * (0 if p1 else 1):
                donezo = True
                break
    return len(sands)
def triangles():
    all_sands = set()
    m1, m2 = 500, 500
    for i in range(lowest_rock + 2):
        for j in range(m1, m2 + 1):
            all_sands.add((j,i))
        m1 -= 1
        m2 += 1
    all_sands = all_sands.difference(rocks)
    def ranges(nums):
        nums = sorted(set(nums))
        gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
        edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
        return list(filter(lambda x: x[-1] - x[0] >= 2, list(zip(edges, edges))))
    horizontal_rows = []
    blocked_by_rows = set()
    while True:
        before = len(blocked_by_rows)
        for row, places in rows.items():
            asdf = ranges(places)
            for a in asdf:
                horizontal_rows.append((a[0], a[1], row))
        for l, r, h in horizontal_rows:
            n_l, n_r, n_h = l+1, r, h+1
            while n_l <= n_r:
                for q in range(n_l, n_r):
                    rocks.add((q, n_h))
                    blocked_by_rows.add((q, n_h))
                    rows[n_h].append(q)
                n_l += 1
                n_r -= 1
                n_h += 1
        after = len(blocked_by_rows)
        if after == before:
            break

    all_sands = all_sands.difference(blocked_by_rows)
    # Lines below print the final state
    # grid = []
    # for i in range(300, 700):
    #     builder = []
    #     for j in range(lowest_rock + 2):
    #         if (i, j) in rocks:
    #             builder.append("#")
    #         else:
    #             if (i,j) in sands and (i,j) in all_sands:
    #                 builder.append("o")
    #             elif (i,j) in sands and (i,j) not in all_sands:
    #                 builder.append("e")
    #             elif (i,j) not in sands and (i,j) in all_sands:
    #                 builder.append("x")
    #             else:
    #                 builder.append(".")
    #     grid.append(builder)
    # grid = np.array(grid)
    # grid = grid.T
    # for line in grid:
    #     print("".join(line))
    return len(all_sands)

print("p1", solve())
print("p2", solve(False))
print("p2 (triangle)", triangles())

