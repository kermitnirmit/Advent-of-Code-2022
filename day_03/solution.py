import string
f = open("input.txt").read().strip().split("\n")

vals = "." + string.ascii_lowercase + string.ascii_uppercase

score = 0
for line in f:
    l, r = set(line[:len(line)//2]), set(line[len(line)//2:])
    i = list(l.intersection(r))[0]
    score += (vals.index(list(l.intersection(r))[0]))
print(score)

score = 0
for i in range(0, len(f), 3):
    q,w,e = set(f[i]), set(f[i+1]), set(f[i+2])
    i = list(q.intersection(w).intersection(e))[0]
    score += vals.index(i)
print(score)
