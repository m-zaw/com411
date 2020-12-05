import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

pi = np.pi


def animate(frame):
    ax.cla()
    ax.set_xlim(0, pi * 2)
    ax.set_ylim(-1, 1)
    x = np.arange(0, 2 * pi, 0.01)
    y = np.sin(x + frame / 50)
    ax.plot(x, y, 'r')


def run():
    anim = animation.FuncAnimation(
        fig, animate, frames=720, interval=100)
    plt.show()


run()
