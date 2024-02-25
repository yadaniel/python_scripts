#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt
import pint

print(sys.version)

ureg = pint.UnitRegistry()

R = 10e3 * ureg.ohm
C = 100e-9 * ureg.F
T = (R*C).magnitude

print(f"R={R}, C={C}, T={T}")

s1 = c.tf([1/T], [1, 1/T])
s2 = c.tf([1, 0], [1, 1/T])
s3a = c.series(s1, s2)
s3b = c.series(s2, s1)

ta,ya = c.step_response(s3a)
tb,yb = c.step_response(s3b)

plt.subplot(2,1,1)
plt.plot(ta, ya)
plt.grid()

plt.subplot(2,1,2)
plt.plot(tb, yb)
plt.grid()

plt.show()

