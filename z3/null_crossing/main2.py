#!C:/Python3/python

import sys
import random
import numpy as np
import matplotlib.pylab as plt
import z3

print(sys.version)

N = 20
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

# create solver
solver = z3.Solver()

# create variables
x = z3.Real("x")

solver.add(eval(f))

if solver.check() == z3.sat:
    model = solver.model()
    print(solver.model)
    print("x =", model.eval(x))
else:
    print("no sat")


