digits = lambda x: [int(q) for q in str(x)]
f = [digits(x) for x in open("input.txt").read().strip().split("\n")]
dirs_2d_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = set()
for i in range(len(f)):
    maxsofar = -1
    for j in range(len(f[0])):
        if f[i][j] > maxsofar:
            seen.add((i, j))
            maxsofar = f[i][j]
    maxsofar = -1
    for j in range(len(f[0]) - 1, -1, -1):
        if f[i][j] > maxsofar:
            seen.add((i, j))
            maxsofar = f[i][j]
for j in range(len(f[0])):
    maxsofar = -1
    for i in range(len(f)):
        if f[i][j] > maxsofar:
            seen.add((i, j))
            maxsofar = f[i][j]
    maxsofar = -1
    for i in range(len(f) - 1, -1, -1):
        if f[i][j] > maxsofar:
            seen.add((i, j))
            maxsofar = f[i][j]
print(len(seen))


def seeing_distance(i, j):
    s = 1
    for di, dj in dirs_2d_4:
        seeing = 0
        ni, nj = i, j
        keep = True
        while keep:
            ni, nj = ni + di, nj + dj
            if 0 <= ni < len(f) and 0 <= nj < len(f[0]):
                seeing += 1
                if f[i][j] <= f[ni][nj]:
                    keep = False
            else:
                keep = False
        s *= seeing
    return s


print(max(seeing_distance(i, j) for j in range(len(f[0])) for i in range(len(f))))
