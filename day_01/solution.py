f = open("input.txt").read().strip().split("\n\n")
counts = sorted([sum(int(x) for x in y.split("\n")) for y in f])
print(max(counts))
print(sum(counts[-3:]))
