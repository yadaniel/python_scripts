#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt

# plant
T = 0.001
p = c.tf([1/T], [1, 1/T, 1/T])
# n,d = c.pade(0.001,1)
# p = c.series(p1, c.tf(n,d))

# controller
KP,KI,KD = 0.01, 1, 0.0
ctrl = c.TransferFunction([KD,KP,KI], [1,0])

# feedback system
s = c.feedback(p*ctrl)

u_t, u_v = c.step_response(s)
N = len(u_v)
plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
plt.title("step response of plan with PID controller")
plt.grid()
plt.legend(["step","response"])
plt.show()

