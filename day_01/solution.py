f = sorted([sum(int(x) for x in y.split("\n")) for y in open("input.txt").read().strip().split("\n\n")])
print(max(f))
print(sum(f[-3:]))
