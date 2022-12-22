from utils import ints, words
import numpy as np

f = [x for x in open("input.txt").read().split("\n\n")]
arr = [x for x in f[0].split("\n")]
maxRowLen = max(len(row) for row in arr)
board = np.zeros((len(arr), maxRowLen), int)

for i, row in enumerate(arr):
    for j, v in enumerate(row.ljust(maxRowLen)):
        board[i, j] = {" ": 2, "#": 1, ".": 0}[v]

dirs = f[1]

facing = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

inv_map = {v: k for k, v in facing.items()}

scores = ((0, 1), (1, 0), (0, -1), (-1, 0))

def turn(d, direction):
    i = scores.index(d)
    if direction == "R":
        return scores[(i + 1) % 4]
    elif direction == "L":
        return scores[(i - 1) % 4]


def move(curr, d, part):
    h, w = board.shape
    ni = (curr[0] + d[0]) % h
    nj = (curr[1] + d[1]) % w
    if part == 1:
        while board[(ni, nj)] == 2:  # skip empties and go back to where it should be
            ni = (ni + d[0]) % h
            nj = (nj + d[1]) % w
    else:
        if board[((ni, nj))] == 2: # we're in the ether
            startSquareRow = curr[0] // 50
            startSquareCol = curr[1] // 50
            howFarRow = curr[0] % 50
            howFarCol = curr[1] % 50
            check = (startSquareRow, startSquareCol, inv_map[d])
            if check == (0,1, "L"): # L on 1        R on 4
                ni = 149 - howFarRow
                nj = 0
                nd = facing["R"]
            elif check == (0,1, "U"):  # U on 1        R on 6
                ni = 150 + howFarCol
                nj = 0
                nd = facing["R"]
            elif check == (0, 2, "U"): # U on 2        U on 6
                ni = 199
                nj = howFarCol
                nd = facing["U"]
            elif check == (0,2, "R"):    # R on 2        L on 5
                ni = 149 - howFarRow
                nj = 99
                nd = facing["L"]
            elif check == (0,2, "D"):    # D on 2        L on 3
                ni = 50 + howFarCol
                nj = 99
                nd = facing["L"]
            elif check == (1,1, "L"):    # L on 3        D on 4
                ni = 100
                nj = howFarRow
                nd = facing["D"]
            elif check == (1, 1, "R"):  # L on 3        D on 4
                ni = 49
                nj = 100 + howFarRow
                nd = facing["U"]
            elif check == (2, 0, "L"):  # L on 4        R on 1
                ni = 49 - howFarRow
                nj = 50
                nd = facing["R"]
            elif check == (2, 0, "U"):  # L on 4        R on 3
                ni = 50 + howFarCol
                nj = 50
                nd = facing["R"]
            elif check == (2, 1, "R"):  # R on 5        L on 2
                ni = 49 - howFarRow
                nj = 149
                nd = facing["L"]
            elif check == (2, 1, "D"):  # R on 5        L on 6
                ni = 150 + howFarCol
                nj = 49
                nd = facing["L"]
            elif check == (3, 0, "D"):  # D on 6        D on 2
                ni = 0
                nj = 100 + howFarCol
                nd = facing["D"]
            elif check == (3, 0, "L"):  # L on 6        D on 1
                ni = 0
                nj = 50 + howFarRow
                nd = facing["D"]
            elif check == (3, 0, "R"):  # R on 6        U on 5
                ni = 149
                nj = 50 + howFarRow
                nd = facing["U"]
            return (ni, nj), nd

    # p2

    # 1 = row 0, col 1
    # 2 = row 0 col 2
    # 3 = row 1 col 1
    # 4 = row 2 col 0
    # 5 = row 2 col 1
    # 6 = row 3 col 0
    # R on 1        R on 2 easy
    # D on 1        D on 3 easy
    # L on 1        R on 4 done
    # U on 1        R on 6 done

    # R on 2        L on 5 done
    # D on 2        L on 3 done
    # L on 2        L on 1 easy
    # U on 2        U on 6 done

    # U on 3        U on 1 easy
    # D on 3        D on 5 easy
    # L on 3        D on 4 done
    # R on 3        U on 2 done

    # R on 4        R on 5 easy
    # D on 4        D on 6 easy
    # L on 4        R on 1 done
    # U on 4        R on 3 done

    # U on 5        U on 3 easy
    # L on 5        L on 4 easy
    # R on 5        L on 2 done
    # D on 5        L on 6 done

    # U on 6        U on 4 easy
    # D on 6        D on 2 done
    # L on 6        D on 1 done
    # R on 6        U on 5 done






    # currSquare = ni % 50, nj % 50



    # Down on 2 => Left on 3

    return (ni, nj), d


def solve(part = 1):
    curr = None
    for i, c in enumerate(arr[0].ljust(maxRowLen)):
        if c == ".":
            curr = (0, i)
            break
    cf = (0, 1)
    for dist, nextTurn in zip(ints(dirs), words(dirs) + ["X"]):
        for d in range(dist):
            n, nd = move(curr, cf, part)
            if board[n] == 1:  # hit wall, stop
                break
            else:
                if board[n] == 0:
                    curr = n
                    cf = nd
        if nextTurn == "X":
            break
        cf = turn(cf, nextTurn)
    f_row = curr[0] + 1
    f_col = curr[1] + 1
    print(1000 * f_row + 4 * f_col + scores.index(cf))

solve(1)
solve(2)