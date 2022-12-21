import re
from collections import deque

from utils import ints

f = [x for x in open("input.txt").read().strip().split("\n")]


def solve(part=1):
    solved = {}
    expressions = {}
    somethingChanged = True
    if part == 1:
        while "root" not in solved:
            for l in f:
                nums = ints(l)
                if len(nums) > 0 and l.split()[0][:-1] not in solved:
                    solved[l.split()[0][:-1]] = nums[0]
                elif l.split()[0][:-1] not in solved:
                    q = l.split()
                    s1 = q[1]
                    s2 = q[-1]
                    op = q[2]
                    parent = q[0][:-1]
                    if s1 in solved and s2 in solved:
                        s1 = solved[s1]
                        s2 = solved[s2]
                        s = str(s1) + op + str(s2)
                        r = int(eval(s))
                        solved[parent] = r
        return solved["root"]

    def fix_string(s):
        letters = re.search("[\?A-z]", s)
        if letters is None:
            return int(eval(s))
        baseString = s
        change = False
        for word in re.findall("[A-z]{4}", s):
            i = baseString.index(word)
            if word in solved:
                change = True
                baseString = baseString[:i] + str(solved[word]) + baseString[i + 4:]
        if change:
            return fix_string(baseString)
        return baseString

    if part == 2:
        while somethingChanged:
            before = len(solved)
            before2 = len(expressions)
            for l in f:
                q = l.split()
                parent = q[0][:-1]
                i = ints(l)
                if len(i) > 0 and parent not in solved:
                    if parent == "humn":
                        solved[parent] = "?"
                    else:
                        solved[parent] = i[0]
                elif parent not in solved:
                    s1 = q[1]
                    s2 = q[-1]
                    op = q[2]
                    if s1 in solved:
                        s1 = solved[s1]
                    if s2 in solved:
                        s2 = solved[s2]
                    if s1 in solved and s2 in solved and type(s1) == type(s2):
                        s = str(s1) + op + str(s2)
                        r = int(eval(s))
                        solved[parent] = r
                    if s1 in expressions:
                        s1 = expressions[s1]
                    if s2 in expressions:
                        s2 = expressions[s2]
                    next = "(" + str(s1) + op + str(s2) + ")"
                    fixed_string = fix_string(next)
                    if type(fixed_string) == int:
                        solved[parent] = fixed_string
                    else:
                        expressions[parent] = str(fixed_string)
            after = len(solved)
            after2 = len(expressions)

            # input("continue")
            somethingChanged = after2 > before2
            somethingChanged = somethingChanged or after > before
        root = [x for x in f if x.startswith("root")][0].split()
        left = root[1]
        right = root[3]
        children = [left, right]

        equa = []
        for child in children:
            s = expressions[child]
            after = fix_string(s)
            if type(after) is int:
                equa.append(str(after))
            else:
                Q = deque([child])
                path = {}
                strs = []
                while Q:
                    curr = Q.popleft()
                    s = expressions[curr]
                    path[curr] = s
                    strs.append(s)
                    words = re.findall("[A-z]{4}", s)
                    for word in words:
                        Q.append(word)
                start = None
                for letters, equation in path.items():
                    if "?" in equation:
                        start = (letters, equation)
                        break
                canSimplify = True
                while canSimplify:
                    canSimplify = False
                    for letters, equation in path.items():
                        if start[0] in equation:
                            canSimplify = True
                            where = equation.index(start[0])
                            start = (letters, equation[:where] + start[1] + equation[where + 4:])
                equa.append(start[1])
        equa = "=".join(equa)

        def solve_linear(equation, var='?'):
            expression = equation.replace("=", "-(") + ")"
            grouped = eval(expression.replace(var, '1j'))
            return -grouped.real / grouped.imag

        return int(solve_linear(equa, "?"))


print(solve(1))
print(solve(2))
