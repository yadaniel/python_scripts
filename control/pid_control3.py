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

# default
KP,KI,KD = 0.01, 0.5, 0.0

def colors():
    while True:
        yield 'b'
        yield 'g'
        yield 'r'
        yield 'c'
        yield 'm'
        yield 'y'
        yield 'k'
        yield 'gray'
        yield 'orange'

color = colors()

# KP_ = [0.01, 0.1, 1]
# KI_ = [0.5, 0.7, 0.9]

KP_ = [0.1, 1, 2]
KI_ = [0.7, 0.9, 1]

# test one
# KP_ = [1]
# KI_ = [0.9]

N = 0
legend = []
for KP in KP_:
    for KI in KI_:
        # controller
        ctrl = c.TransferFunction([KD,KP,KI], [1,0])
    
        # feedback system
        s = c.feedback(p*ctrl)
        u_t, u_v = c.step_response(s)
    
        N = len(u_v)
        plt.plot(u_t, u_v, next(color))
        legend.append(f"{KP},{KI},{KD}")

plt.plot(u_t, [1]*N, "r")
plt.title("step response of plant with PID controller")
plt.grid()
plt.legend(legend + ["step"])
plt.show()

