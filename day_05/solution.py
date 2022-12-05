from parse import parse
f = open("input.txt").read().strip().split("\n\n")[1].split("\n")
# f = f[1].split("\n")
# [W] [V]     [P]
# [B] [T]     [C] [B]     [G]
# [G] [S]     [V] [H] [N] [T]
# [Z] [B] [W] [J] [D] [M] [S]
# [R] [C] [N] [N] [F] [W] [C]     [W]
# [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
# [C] [W] [B] [G] [S] [V] [F] [D] [N]
# [V] [G] [C] [Q] [T] [J] [P] [B] [M]
#  1   2   3   4   5   6   7   8   9

d = {
    1: list("VCDRZGBW"),
    2: list("GWFCBSTV"),
    3: list("CBSNW"),
    4: list("QGMNJVCP"),
    5: list("TSLFDHB"),
    6: list("JVTWMN"),
    7: list("PFLCSTG"),
    8: list("BDZ"),
    9: list("MNZW")
}

def move(c, s, e):
    for i in range(c):
        m = d[s].pop()
        d[e].append(m)

def move2(c, s, e):
    m = d[s][-c:]
    d[s] = d[s][:-c]
    d[e].extend(m)

for i in range(2):
    for line in f:
        c, s, e = parse("move {:d} from {:d} to {:d}", line)
        if i == 0:
            move(c, s, e)
        else:
            move2(c, s, e)
    b = ""
    for v in d.values():
        b += v[-1]
    print(b)
    d = {
        1: list("VCDRZGBW"),
        2: list("GWFCBSTV"),
        3: list("CBSNW"),
        4: list("QGMNJVCP"),
        5: list("TSLFDHB"),
        6: list("JVTWMN"),
        7: list("PFLCSTG"),
        8: list("BDZ"),
        9: list("MNZW")
    }