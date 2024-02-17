#!C:/Python3/python

import sys
import numpy as np
import matplotlib.pylab as plt
import z3

print(sys.version)

# create solver
solver = z3.Solver()

# f(x) = (x - 5)*(x + 3) = x**2 -5*x + 3*x - 15 = x**2 -2*x - 15
# f(x) != 0 => x1 = 5, x2 = -3

# create variables
x = z3.Real("x")

solver.add(x**2 - 2*x - 15 == 0)
solver.add(x != -3)
solver.add(x != 5)

if solver.check() == z3.sat:
    model = solver.model()
    print(solver.model)
    print("x =", model.eval(x))
else:
    print("no sat")


