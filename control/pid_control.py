#!C:/Python3/python

import sys
import control as c
from control import matlab as cm
import matplotlib.pylab as plt

# plant
T = 0.001
p = c.tf([1,0], [1, 1/T])

# controller
KP,KI,KD = 0.001, 1, 0.01
ctrl = c.TransferFunction([KP,KI,KD], [1,0])

# feedback system
s = c.feedback(p*ctrl)

u_t, u_v = c.step_response(s)
N = len(u_v)
plt.plot(u_t, [1]*N, "r", u_t, u_v, "b")
plt.title("RC low pass step response")
plt.grid()
plt.legend(["step","response"])
plt.show()

