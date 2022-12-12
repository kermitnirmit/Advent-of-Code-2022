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
    queue = [(start, 0)]
    seen.add(start)
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


def solvep1():
    start = (20,0)
    return bfs(start, end)


def solvep2():
    all_as = []
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] in "Sa":
                all_as.append((i, j))
    return min(list(filter(lambda x: x is not None, [bfs(start, end) for start in all_as])))


print(solvep1())
print(solvep2())