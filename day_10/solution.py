f = open("input.txt").read().strip().split("\n")

x = 1
insts = []
imps = [20, 60, 100, 140, 180, 220]
v = 0
for line in f:
    if line != "noop":
        insts.append("noop")
    insts.append(line)

s = ""
p2 = []
for i, line in enumerate(insts):
    if x - 1 <= len(s) <= x + 1:
        s += "#"
    else:
        s += "."
    if len(s) % 40 == 0:
        p2.append(s)
        s = ""
    if i + 1 in imps:
        v += ((i + 1) * x)
    if line != "noop":
        x += int(line.split(" ")[1])
print(v)
for line in p2:
    print(line)
