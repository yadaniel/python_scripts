#!/cygdrive/c/Python39/python

import sys
import time
import random
import numpy as np
import datetime as dt
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation

# Create figure for plotting
fig = plt.figure("multisensor animated graph")
fig.patch.set_facecolor('xkcd:mint green')
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

# 1s
T = 1000

# window length => number of samples to show
N = 60
t0 = time.time()
# ts = [dt.datetime.fromtimestamp(t0-N+i).strftime('%H:%M:%S.%f') for i in range(N)]
ts = [dt.datetime.fromtimestamp(t0-N+i).strftime('%H:%M:%S.%f')[:-5] for i in range(N)]

x1 = [0 for i in range(N)]
x2 = [0 for i in range(N)]
x3 = [0 for i in range(N)]
x4 = [0 for i in range(N)]

def read_sample():
    s1 = random.randint(0,10)
    s2 = random.randint(0,100)
    s3 = random.randint(0,1000)
    s4 = random.randint(0,10000)
    return (s1,s2,s3,s4)

# This function is called periodically from FuncAnimation
def animate(i, ts, x1, x2, x3, x4):

    # read samples
    s1,s2,s3,s4 = read_sample()

    # Add x and y to lists
    # ts.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ts.append(dt.datetime.now().strftime('%H:%M:%S.%f')[:-5])
    x1.append(s1)
    x2.append(s2)
    x3.append(s3)
    x4.append(s4)

    # limit lists to N items
    ts = ts[-N:]
    x1 = x1[-N:]
    x2 = x2[-N:]
    x3 = x3[-N:]
    x4 = x4[-N:]

    # Draw x and y lists
    ax1.clear()
    ax1.plot(ts, x1, "y")
    ax1.set_ylim(0, 10)
    ax1.set_ylabel('0 to 10')
    ax1.grid()

    ax2.clear()
    ax2.plot(ts, x2, "r")
    ax2.set_ylim(0, 100)
    ax2.set_ylabel('0 to 100')
    ax2.grid()

    ax3.clear()
    ax3.plot(ts, x3, "g")
    ax3.set_ylim(0, 1000)
    ax3.set_ylabel('0 to 1000')
    ax3.grid()

    ax4.clear()
    ax4.plot(ts, x4, "b")
    ax4.set_ylim(0, 10000)
    ax4.set_ylabel('0 to 10000')
    ax4.grid()

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)
    plt.setp(ax4.get_xticklabels(), visible=True)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('random values over time')
    plt.tight_layout()

# Set up plot to call animate() function periodically
ani = FuncAnimation(fig, func=animate, fargs=(ts, x1, x2, x3, x4), interval=T)
plt.show()

