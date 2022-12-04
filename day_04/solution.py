from parse import parse
f = open("input.txt").read().strip().split("\n")
c = d = 0
for line in f:
    q,w,e,r = parse("{:d}-{:d},{:d}-{:d}", line)
    if q <= e <= r <= w or e <= q <= w <= r:
        c += 1
    if max(q,e) <= min(w,r):
        d += 1
print(c)
print(d)
