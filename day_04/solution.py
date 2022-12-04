import string
f = open("input.txt").read().strip().split("\n")
c = d = 0
for line in f:
    l,r = line.split(",")
    q,w = l.split("-")
    q = int(q)
    w = int(w)
    e,r = r.split("-")
    e = int(e)
    r = int(r)
    if q <= e <= r <= w or e <= q <= w <= r:
        c += 1
    if max(q,e) <= min(w,r):
        d += 1
print(c)
print(d)
