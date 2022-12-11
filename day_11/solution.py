from tqdm import trange
m = open("input.txt").read().strip().split("\n\n")

class Monkey:
    def __init__(self, items, operation, mod, iftrue, iffalse):
        self.items = items
        self.operation = operation
        self.mod = mod
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.count = 0
    def work(self):
        self.count += 1

    def __repr__(self):
        return "" + str(self.items) + " " +  self.operation + " " +  str( self.mod) + " " +  str( self.iftrue) + " " +  str(self.iffalse) + " " +   str(self.count)
monkeys = []
for monkey in m:
    q = monkey.split("\n")
    # print(q[1].split("Starting items: "))
    items = [ int(x) for x in q[1].split("Starting items: ")[1].split(", ")]
    operation = q[2].split("Operation: new = old ")[1]
    mod = int(q[3].split("Test: divisible by ")[1])
    iftrue = int(q[4].split("If true: throw to monkey ")[1])
    iffalse = int(q[5].split("If false: throw to monkey ")[1])

    monkeys.append(Monkey(items, operation, mod, iftrue, iffalse))


def throwTo(i, newItem):
    monkeys[i].items.append(newItem)


bigTestNum = 1
for monkey in monkeys:
    bigTestNum *= monkey.mod


def solve(its=20, divby=3):
    for _ in trange(its):
        for i in range(len(monkeys)):
            for j in range(len(monkeys[i].items) - 1, -1, -1):
                currMonkey = monkeys[i]
                newItem = currMonkey.items.pop(j)
                # print(currMonkey.operation)
                currMonkey.count += 1
                if currMonkey.operation[0] == "*":
                    if currMonkey.operation[-3:] == "old":
                        newItem *= newItem
                    else:
                        newItem *= int(currMonkey.operation.split(" ")[1])
                elif currMonkey.operation[0] == "+":
                    if currMonkey.operation[-3:] == "old":
                        newItem += newItem
                    else:
                        newItem += int(currMonkey.operation.split(" ")[1])
                if divby:
                    newItem //= divby
                else:
                    newItem = newItem % bigTestNum
                if newItem % currMonkey.mod == 0:
                    throwTo(currMonkey.iftrue, newItem)
                else:
                    throwTo(currMonkey.iffalse, newItem)
    counts = sorted([w.count for w in monkeys])
    return counts[-2] * counts[-1]
print(solve(20, 3))
print(solve(10000, None))


