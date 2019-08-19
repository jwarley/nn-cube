import numpy as np

"""
Generate the group of moves using generators <U, x, S>
"""

seed_moves = d = {
    "id": list(range(0, 54)),
    "U":  [6,  7,  0,  1,  2,  3,  4,  5,  8,
           18, 19, 20, 12, 13, 14, 15, 16, 17,
           27, 28, 29, 21, 22, 23, 24, 25, 26,
           36, 37, 38, 30, 31, 32, 33, 34, 35,
           9,  10, 11, 39, 40, 41, 42, 43, 44,
           45, 46, 47, 48, 49, 50, 51, 52, 53],
    "x":  [18, 19, 20, 21, 22, 23, 24, 25, 26,
           11, 12, 13, 14, 15, 16, 9,  10, 17,
           45, 46, 47, 48, 49, 50, 51, 52, 53,
           33, 34, 27, 28, 29, 30, 31, 32, 35,
           4,  5,  6,  7,  0,  1,  2,  3,  8,
           40, 41, 42, 43, 36, 37, 38, 39, 44],
    "S": [0,  1,  2,  10,  4,  5,  6,  14, 17,
          9,  52, 11, 12, 13, 48, 15, 16, 53,
          18, 19, 20, 21, 22, 23, 24, 25, 26,
          27, 7, 29, 30, 31, 3, 33, 34, 8,
          36, 37, 38, 39, 40, 41, 42, 43, 44,
          45, 46, 47, 28, 49, 50, 51, 32, 35],
}


# compose a list of moves to get a new permutation
def cm(moves):
    perm = np.array(d["id"])
    for move in moves:
        perm = perm[np.array(d[move])]
    return perm


if __name__ == "__main__":
    # define all the remaining moves from the generators and print the result
    d["U2"] = list(cm(["U", "U"]))
    d["U'"] = list(cm(["U", "U", "U"]))

    d["x2"] = list(cm(["x", "x"]))
    d["x'"] = list(cm(["x", "x", "x"]))

    d["S2"] = list(cm(["S", "S"]))
    d["S'"] = list(cm(["S", "S", "S"]))

    d["F"] = list(cm(["x", "U", "x'"]))
    d["F2"] = list(cm(["F", "F"]))
    d["F'"] = list(cm(["F", "F", "F"]))

    d["B"] = list(cm(["x'", "U", "x"]))
    d["B2"] = list(cm(["B", "B"]))
    d["B'"] = list(cm(["B", "B", "B"]))

    d["D"] = list(cm(["x2", "U", "x2"]))
    d["D2"] = list(cm(["D", "D"]))
    d["D'"] = list(cm(["D", "D", "D"]))

    d["z"] = list(cm(["F", "S", "B'"]))
    d["z2"] = list(cm(["z", "z"]))
    d["z'"] = list(cm(["z", "z", "z"]))

    d["R"] = list(cm(["z'", "U", "z"]))
    d["R2"] = list(cm(["R", "R"]))
    d["R'"] = list(cm(["R", "R", "R"]))

    d["L"] = list(cm(["z", "U", "z'"]))
    d["L2"] = list(cm(["L", "L"]))
    d["L'"] = list(cm(["L", "L", "L"]))

    d["y"] = list(cm(["z", "x", "z'"]))
    d["y2"] = list(cm(["y", "y"]))
    d["y'"] = list(cm(["y", "y", "y"]))

    d["E"] = list(cm(["U", "D'", "y'"]))
    d["E2"] = list(cm(["E", "E"]))
    d["E'"] = list(cm(["E", "E", "E"]))

    d["M"] = list(cm(["R", "L'", "x'"]))
    d["M2"] = list(cm(["M", "M"]))
    d["M'"] = list(cm(["M", "M", "M"]))

    print(d)
