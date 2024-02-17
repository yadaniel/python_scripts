#!C:/Python3/python

import sys
import random
import numpy as np
import matplotlib.pylab as plt
import z3

print(sys.version)

N = 5
zeros = []
for i in range(N):
    zeros.append(random.randint(-10, 10))

kx = np.poly(zeros)
print(zeros)
print(kx)

t = []
for k,p in enumerate((reversed(kx))):
    if p != 0:
        if k == 0:
            t.append(f"{p}")
        elif k == 1:
            t.append(f"{p}*x")
        else:
            t.append(f"{p}*x**{k}")

f = "+".join(t) + " == 0"

print(f)
# sys.exit()

xs = []

while True:

    # create solver
    solver = z3.Solver()

    # create variables
    x = z3.Real("x")

    solver.add(eval(f))
    for xfound in xs:
        solver.add(eval(f"x != {xfound}"))

    if solver.check() == z3.sat:
        model = solver.model()
        print(solver.model)
        print("x =", model.eval(x))
        xs.append(model.eval(x))
    else:
        print("no sat")
        break

print(xs)

xs_ = []
for x in xs:
    xs_.append(x.as_long())

print(sorted(xs_))
print(sorted(zeros))

if sorted(xs_) == sorted(zeros):
    print("succeded to find all zeros")
else:
    # multiple zeros of same number will be found only once
    print("failed to find all zeros")


