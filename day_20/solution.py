def solve(part=1):
    f = [int(x) * (811589153 if part == 2 else 1) for x in open("input.txt").read().strip().split("\n")]
    z_blah = None
    og = []
    store = list(enumerate(f))
    for i, line in enumerate(f):
        if line == 0:
            z_blah = (i, line)
        og.append((i, line))

    def move(nums, i):
        p = nums.index(store[i])
        val = nums[p]
        nums.pop(p)  # remove it
        nums.insert((p + val[1]) % len(nums), val)  # insert it where it belongs
        return nums

    for t in range(10 if part == 2 else 1):
        for i in range(len(f)):
            og = move(og, i)

    print(sum(og[(og.index(z_blah) + c) % len(og)][1] for c in [1000, 2000, 3000]))
solve(1)
solve(2)

# Leaving this almost working circular DLL system that doesn't work
# class Node:
#     def __init__(self, prev, next, val):
#         self.prev = prev
#         self.next = next
#         self.val = val
#
#     def __repr__(self):
#         return "".join(
#             ("currVal: ", str(self.val), " | ", "prevVal: ", str(self.prev.val), " | ", "nextVal", str(self.next.val)))
#
#
# nodes = []
# nodes.append(Node(None, None, f[0]))
# for i in range(1, len(f)):
#     newNode = Node(nodes[-1], None, f[i])
#     nodes[-1].next = newNode
#     nodes.append(newNode)
#
# nodes[-1].next = nodes[0]
# nodes[0].prev = nodes[-1]
# # print(len(f))
# # print(len(nodes))
# # print(nodes)
# # print(len(set(f)))
# # print(len(d))
#
#
# def all_nodes(seed):
#     ret = [seed.val]
#     n = seed.next
#     while n != seed:
#         ret.append(n.val)
#         n = n.next
#     assert len(ret) == 5000, len(ret)
#     return ret
#
#
# def insert_after(val, node):
#     newNode = Node(None, None, val)
#     newNode.next = node.next
#     node.next = newNode
#     newNode.prev = node
#     newNode.next.prev = newNode
#     return newNode
#
# def insert_before(val, node):
#     newNode = Node(None, None, val)
#     newNode.prev = node.prev
#     node.prev = newNode
#     newNode.next = node
#     newNode.prev.next = newNode
#     return newNode
#
# def remove(node):
#     node.prev.next = node.next
#     node.next.prev = node.prev
#     return node
#
#
# done = None
# for i, val in enumerate(f):
#     if val == 0:
#         continue
#     q = nodes[i]
#     ogq = q
#     ogq.prev.next = ogq.next
#     ogq.next.prev = ogq.prev
#     ogval = val
#     if val < 0:
#         val = val % 4999
#         # print("in negative")
#         # good = -1 * val
#         # bad = (-1 * val) % 4999
#         # print(good , "||| ", bad)
#         # print((good - bad) / 4999)
#         # # print("good value", -1 * val, "bad value", (-1 * val) % 4999)
#         # input("continue")
#         # for _ in range(-1 * val):
#         #     # move backwards
#         #     q = q.prev
#         # nn = insert_before(val, q)
#         # done = all_nodes(nn)
#     # elif val > 0:
#
#         # print("in pos")
#         # print("good value", val, "also good value", val % 4999)
#         # input("continue")
#     for _ in range(val % 4999):
#         # move forward
#         q = q.next
#     if ogval < 0:
#         nn = insert_before(ogval, q)
#     else:
#         nn = insert_after(ogval, q)
#     done = all_nodes(nn)
#
#
# zero_index = done.index(0)
# print(done[(zero_index + 1000) % len(done)] + done[(zero_index + 2000) % len(done)] + done[(zero_index + 3000) % len(done)])
