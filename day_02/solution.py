f = [x.split(" ") for x in open("input.txt").read().strip().split("\n")]
# rock      =       a/x
# paper     =       b/y
# scissors  =       c/z
# key: lose/draw/win
ldw_map = {
    'A': "YXZ",
    'B': "ZYX",
    'C': "XZY"
}
# your choice to [shape score, p2 w/l/d indexes, p2 outcome score]
super_map = {
    'X': [1, 2, 0],
    'Y': [2, 1, 3],
    'Z': [3, 0, 6]
}
wdl_score = [6, 3, 0]
score1 = 0
score2 = 0
for l,r in f:
    score1 += wdl_score[ldw_map[l].index(r)] + super_map[r][0]
    score2 += super_map[ldw_map[l][super_map[r][1]]][0] + super_map[r][2]
print(score1)
print(score2)

# # Initial Solution:
# score = 0
# for l, r in f:
#     if l == 'A':
#         if r == 'X':
#             score += 4
#         elif r == 'Y':
#             score += 8
#         else:
#             score += 3
#     elif l == 'B':
#         if r == 'X':
#             score += 1
#         elif r == 'Y':
#             score += 5
#         else:
#             score += 9
#     else:
#         if r == 'X':
#             score += 7
#         elif r == 'Y':
#             score += 2
#         else:
#             score += 6
# print("p1", score)
#
#
# # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
# score = 0
# for l, r in f:
#     if l == 'A': # rock
#         if r == 'X':
#             score += (3)
#         elif r == 'Y':
#             score += (1+3)
#         else:
#             score += (2+6)
#     elif l == 'B': # paper
#         if r == 'X':
#             score += (1)
#         elif r == 'Y':
#             score += (2+3)
#         else:
#             score += (3+6)
#     else: # scissors
#         if r == 'X':
#             score += (2)
#         elif r == 'Y':
#             score += (3+3)
#         else:
#             score += (1+6)
# print("p2", score)