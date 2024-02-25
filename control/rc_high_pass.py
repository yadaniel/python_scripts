#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt
import pint

print(sys.version)

ureg = pint.UnitRegistry()

# x(t) --|C|-------- y(t)
#              | 
#             ___
#             ___ R
#              |
#      -------------

# 1) i=(x-y)/R = C*(x-y)'
# 2) y = i*R
# y = C*(x-y)'*R = RC*(x-y)'
# y/RC + y' = x'
# Y/RC + sY = sX
# G = s / (s + 1/RC)


R = 10e3 * ureg.ohm
C = 100e-9 * ureg.F
T = (R*C).magnitude

print(f"R={R}, C={C}, T={T}")

s1 = c.tf([1, 0], [1, 1/T])

# print(u_step.inputs, len(u_step.inputs))
# print(u_step.outputs, len(u_step.outputs))

u_step = c.step_response(s1)
plt.plot(range(len(u_step.inputs)), u_step.inputs, "r", range(len(u_step.outputs)), u_step.outputs, "b")
plt.title("RC high pass step response")
plt.grid()
plt.legend(["step","response"])
plt.show()

# u_t, u_v = c.step_response(s1)
# N = len(u_v)
# plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
# plt.title("RC high pass step response")
# plt.grid()
# plt.legend(["step","response"])
# plt.show()

# u_v,u_t = cm.step(s1)
# N = len(u_v)
# plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
# plt.title("RC high pass step response")
# plt.grid()
# plt.legend(["step","response"])
# plt.show()

