#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt
import pint

print(sys.version)

ureg = pint.UnitRegistry()

# x(t) --R---------- y(t)
#           | 
#          ___
#          ___ C 
#           |
#      -------------

# 1) i=(x-y)/R
# 2) y = 1/C*int i
# y = 1/C * int (x-y)/R = 1/RC * int (x-y)
# y' = 1/RC * (x - y)
# RC*y' + y = x
# T*sY + Y = X
# Y(sT+1) = X
# Y/X = 1/(sT+1) = (1/T) / (s + 1/T)


R = 10e3 * ureg.ohm
C = 100e-9 * ureg.F
T = (R*C).magnitude

print(f"R={R}, C={C}, T={T}")

s1 = c.tf([1/T], [1, 1/T])

# print(u_step.inputs, len(u_step.inputs))
# print(u_step.outputs, len(u_step.outputs))

# u_step = c.step_response(s1)
# plt.plot(range(len(u_step.inputs)), u_step.inputs, "r", range(len(u_step.outputs)), u_step.outputs, "b")
# plt.title("RC low pass step response")
# plt.grid()
# plt.legend(["step","response"])
# plt.show()

u_t, u_v = c.step_response(s1)
N = len(u_v)
plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
plt.title("RC low pass step response")
plt.grid()
plt.legend(["step","response"])
plt.show()

# u_v,u_t = cm.step(s1)
# N = len(u_v)
# plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
# plt.title("RC low pass step response")
# plt.grid()
# plt.legend(["step","response"])
# plt.show()

