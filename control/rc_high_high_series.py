#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt
from scipy.signal import find_peaks
import pint

print(sys.version)

ureg = pint.UnitRegistry()

R = 10e3 * ureg.ohm
C = 100e-9 * ureg.F
T = (R*C).magnitude

print(f"R={R}, C={C}, T={T}")

s1 = c.tf([1, 0], [1, 1/T])
s2 = c.series(s1, s1)

t1,y1 = c.step_response(s1)
t2,y2 = c.step_response(s2)

idx_mins,_ = find_peaks(-y2)

for idx in idx_mins:
    print(f"min => {y2[idx]} at {t2[idx]}")

plt.subplot(2,1,1)
plt.plot(t1, y1)
plt.grid()

plt.subplot(2,1,2)
plt.plot(t2, y2)
plt.grid()

plt.show()

