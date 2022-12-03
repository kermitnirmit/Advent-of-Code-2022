import string
f = open("input.txt").read().strip().split("\n")

vals = "." + string.ascii_lowercase + string.ascii_uppercase

score = 0
for line in f:
    qwe = line[:len(line)//2], line[len(line)//2:]
    print(qwe)
    l = qwe[0]
    r = qwe[1]
    l = set(l)
    r = set(r)
    i = list(l.intersection(r))[0]
    print(i, vals.index(i))
    score += (vals.index(list(l.intersection(r))[0]))
print(score)

score = 0
for i in range(0, len(f), 3):
    q,w,e = set(f[i]), set(f[i+1]), set(f[i+2])
    i = list(q.intersection(w).intersection(e))[0]
    score += vals.index(i)
print(score)
