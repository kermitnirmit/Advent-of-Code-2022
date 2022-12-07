from collections import defaultdict

f = [x for x in open("input.txt").read().strip().split("\n")]
d = {}
path = []
for line in f:
    if line.startswith("$"):
        if line == "$ cd ..":
            path = path [:-1]
        elif line.startswith("$ cd "):
            path.append(line[5:])
            d[str(path)] = [[], 0]
    elif line.startswith("dir"):
        d[str(path)].append([line[4:], 0])
    else:
        size, name = line.split(" ")
        size = int(size)
        d[str(path)].append([name, size])
        tempPath = path
        while len(tempPath) > 1:
            tempPath = tempPath[:-1]
            d[str(tempPath)][1] += size

total = 0
for k,v in d.items():
    s = 0
    for item in v:
        if type(item) == list and len(item) == 2:
            s += item[1]
        elif type(item) == int:
            s += item
    if s <= 100000:
        total += s
print(total)
qwer = []
for k,v in d.items():
    s = 0
    for item in v:
        if type(item) == list and len(item) == 2:
            s += item[1]
        elif type(item) == int:
            s += item
    if 70000000 - 44274331 + s > 30000000:
        qwer.append((k, s))
qwer = sorted(qwer, key= lambda x: x[1])
print(qwer[0][1])
