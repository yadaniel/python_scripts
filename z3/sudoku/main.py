#!C:/Python3/python

import sys
import numpy as np
import matplotlib.pylab as plt
import z3

print(sys.version)

s = """
    |1,2,3|4,5,6|7,8,9|
    |4,_,_|_,_,_|_,_,_|
    |5,_,_|_,_,_|_,_,_|
    -
    |_,_,_|1,_,_|_,_,_|
    |_,_,_|2,_,_|_,_,_|
    |_,_,_|3,_,_|_,_,_|
    -
    |_,_,_|_,_,_|6,_,_|
    |_,_,_|_,_,_|8,_,_|
    |_,_,_|_,_,_|9,_,_|
"""[1:-1]

# create solver
solver = z3.Solver()

# create variables
X = [[None for i in range(9)] for i in range(9)]
for r in range(9):
    for c in range(9):
        X[r][c] = z3.Int(f"X_{r}_{c}")

# fill in constraints from given sudoku
f = np.arange(1,82).reshape(9,9)
r = 0
for line in s.splitlines():
    if line.strip() == "-":
        continue
    xs = line.strip(" |").replace("|", ",").replace("_", "0").split(",")
    # print(xs)
    for c,x in enumerate(xs):
        # print(x)
        f[r,c] = int(x)
        if int(x) != 0:
            solver.add(X[r][c] == int(x))
    r += 1

# print(f)

# add range constraints
for r in range(9):
    for c in range(9):
        solver.add(X[r][c] >= 1)
        solver.add(X[r][c] <= 9)

# add row and column constraints
for i in range(9):
    # solver.add(z3.Distinct(X[i][:]))  # not working
    # solver.add(z3.Distinct(X[:][i]))  # not working
    solver.add(z3.Distinct([X[i][j] for j in range(9)]))
    solver.add(z3.Distinct([X[j][i] for j in range(9)]))

# add 3x3 submatrix constraints
solver.add(z3.Distinct([X[r+0][c] for r in range(3) for c in range(0,3)]))
solver.add(z3.Distinct([X[r+3][c] for r in range(3) for c in range(0,3)]))
solver.add(z3.Distinct([X[r+6][c] for r in range(3) for c in range(0,3)]))
solver.add(z3.Distinct([X[r+0][c] for r in range(3) for c in range(3,6)]))
solver.add(z3.Distinct([X[r+3][c] for r in range(3) for c in range(3,6)]))
solver.add(z3.Distinct([X[r+6][c] for r in range(3) for c in range(3,6)]))
solver.add(z3.Distinct([X[r+0][c] for r in range(3) for c in range(6,9)]))
solver.add(z3.Distinct([X[r+3][c] for r in range(3) for c in range(6,9)]))
solver.add(z3.Distinct([X[r+6][c] for r in range(3) for c in range(6,9)]))

if solver.check() == z3.sat:
    model = solver.model()
    print(solver.model)
    for r in range(9):
        for c in range(9):
            print(model.eval(X[r][c]), " ", end="")
        print()
else:
    print("no sat")

# for r in range(9):
#     for c in range(9):
#         z3.ForAll([i,j], z3.Implies(i!=j, X[r][i]!=X[r][j]))
#         z3.ForAll([i,j], z3.Implies(i!=j, X[i][c]!=X[j][c]))

# x = np.arange(1,82).reshape(9,9)
# plt.matshow(x, cmap="gray")
# # plt.imshow(x, cmap="gray", interpolation="nearest")
# # plt.imshow(x, cmap="copper")
# for i in range(9):
#     for j in range(9):
#         plt.text(j, i, str(i*10 + j + 1), ha="center", va="center", fontsize=10)
# # plt.grid()
# plt.show()

