import functools
import ast
from math import prod

f = open("input.txt").read().strip().split("\n\n")


def compare(l, r):
    if type(l) == type(r):
        if type(l) == int:
            if l == r:
                return "k"
            else:
                return l < r
        else:
            for l2, r2 in zip(l, r):
                ok = compare(l2, r2)
                if not ok:
                    return False
                if ok is True:
                    return True
            if len(l) < len(r):
                return True
            if len(r) < len(l):
                return False
        return "k"
    else:
        if type(r) == list:
            return compare([l], r)
        if type(l) == list:
            return compare(l, [r])


def customComp(x, y):
    return - 1 * compare(x, y)


valid = 0
all_lines = []
for i, pair in enumerate(f):
    one, two = pair.split("\n")
    one = ast.literal_eval(one)
    two = ast.literal_eval(two)
    all_lines.append(one)
    all_lines.append(two)
    if compare(one, two):
        valid += (i + 1)
all_lines.append([[2]])
all_lines.append([[6]])
al = sorted(all_lines, key=functools.cmp_to_key(customComp))
print(valid)
print(prod(i for i, line in enumerate(al, 1) if line in [[[2]], [[6]]]))
