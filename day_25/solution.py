f = [x for x in open("input.txt").read().strip().split("\n")]

a = 0
d = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}
d1 = {v % 5: k for k, v in d.items()}
for l in f:
    n = 0
    letters = list(l)[::-1]
    for i in range(len(letters)):
        n += d[letters[i]] * 5 ** i
    a += n
print(a)
ret = ""
while a > 0:
    rem =  a % 5
    adding = d1[rem]
    ret = adding + ret
    a = (a - d[adding]) // 5
print(ret)
