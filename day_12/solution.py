from utils import *
import string
f = open("input.txt").read().strip().split("\n")
heights = string.ascii_lowercase
end = (20, 154)

def getHeight(x,y):
    if f[x][y] in heights:
        return heights.index(f[x][y])
    else:
        if f[x][y] == "S":
            return 0
        if f[x][y] == "E":
            return 25

def bfs(start, goal):
    seen = set()
    queue = []
    for s in start:
        queue.append((s, 0))
        seen.add(s)
    while queue:
        (point, length) = queue.pop(0)
        x,y = point
        if (x,y) == goal:
            return length
        currHeight = getHeight(x,y)
        for dx, dy in dmap.values():
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(f) and 0 <= ny < len(f[0]) and getHeight(nx,ny) - currHeight <= 1 and (nx,ny) not in seen:
                seen.add((nx, ny))
                queue.append(((nx,ny), length + 1))


def solve(t="S"):
    starts = []
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] in t:
                starts.append((i,j))
    return bfs(starts, end)

print(solve("S"))
print(solve("Sa"))