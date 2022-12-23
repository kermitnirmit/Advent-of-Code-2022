from collections import defaultdict

from utils import ints, words, find_neighbors_2d_8, add_tuples

f = [x for x in open("input.txt").read().split("\n")]


def solve(part=1):
    norths = ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)])
    souths = ((1, 0), [(1, -1), (1, 0), (1, 1)])
    wests = ((0, -1), [(-1, -1), (0, -1), (1, -1)])
    easts = ((0, 1), [(-1, 1), (0, 1), (1, 1)])
    dirList = [norths, souths, wests, easts]
    oldElves = set()
    for i, l in enumerate(f):
        for j, letter in enumerate(l):
            if letter == "#":
                oldElves.add((i, j))
    numElves = len(oldElves)
    roundNum = 0
    while True:
        if roundNum == 10 and part == 1:
            break
        roundNum += 1
        proposals = defaultdict(list)
        for c, elf in enumerate(oldElves):
            i, j = elf
            added = False
            # check neighbors. if none, it stays put (also means no one can get to this one!)
            if all(x not in oldElves for x in find_neighbors_2d_8(i, j)):
                added = True
                proposals[elf].append(elf)
            if not added:
                for (ni, nj), dirs in dirList:
                    if all((i + di, j + dj) not in oldElves for di, dj in dirs):
                        proposals[(i + ni, j + nj)].append(elf)
                        added = True
                        break
            # something in every direction so it doesn't move
            if not added:
                proposals[elf].append(elf)
        newElves = set()
        if set(proposals.keys()) == oldElves and part == 2:
            print(roundNum)
            break
        for newPos, p_elves in proposals.items():
            if len(p_elves) > 1:
                newElves.update(p_elves)
            else:
                newElves.add(newPos)
        assert len(newElves) == numElves, (oldElves, newElves, proposals)
        oldElves = newElves.copy()
        dirList = dirList[1:] + [dirList[0]]
    top, left = min(x[0] for x in oldElves), min(x[1] for x in oldElves)
    bottom, right = max(x[0] for x in oldElves), max(x[1] for x in oldElves)
    if part == 1:
        print(sum(1 for j in range(left, right + 1) for i in range(top, bottom + 1) if (i, j) not in oldElves))

solve(1)
solve(2)
#
# roundNum = 0
# while True:
#     if roundNum == 10:
#         break
#     roundNum += 1
#     # print("firstDir: ", dirList[0])
#     proposals = defaultdict(list)
#     for c, elf in enumerate(oldElves):
#         i,j = elf
#         added = False
#         if all(x not in oldElves for x in find_neighbors_2d_8(i, j)):
#             # literally no neighbors
#             # print("no neighbors at all", elf)
#             added = True
#             proposals[elf].append(elf)
#         if not added:
#             for nextPos, dirs in dirList:
#                 if all(add_tuples(elf, n) not in oldElves for n in dirs):
#                     proposals[add_tuples(elf, nextPos)].append(elf)
#                     # print("stopped on index: ", c,  elf, nextPos, "proposal: ", add_tuples(elf, nextPos))
#                     added = True
#                     break
#         if not added:
#             proposals[elf].append(elf)
#     # print("this many elves", len(oldElves))
#     # print("this many were going to unique places: ", len([x for x,v in proposals.items() if len(v) == 1]))
#     # print("this many were going to nonunique places: ", sum([len(v) for x, v in proposals.items() if len(v) > 1]))
#     newElves = set()
#
#     if set(proposals.keys()) == oldElves:
#         print(roundNum)
#         break
#     for newPos, p_elves in proposals.items():
#         if len(p_elves) > 1:
#             newElves.update(p_elves)
#         else:
#             newElves.add(newPos)
#     assert len(newElves) == numElves, (oldElves, newElves, proposals)
#     oldElves = newElves.copy()
#     dirList = dirList[1:] + [dirList[0]]
# top = min(x[0] for x in oldElves)
# left = min(x[1] for x in oldElves)
# bottom = max(x[0] for x in oldElves)
# right = max(x[1] for x in oldElves)
#
#
# print(sum(1 for j in range(left, right + 1) for i in range(top, bottom + 1) if (i,j) not in oldElves))
# for i in range(top, bottom + 1):
#     for j in range(left, right + 1):
#         if (i,j) not in oldElves:
#             a +=1
# print(a)
