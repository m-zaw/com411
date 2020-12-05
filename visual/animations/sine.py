import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()


def animate(frame):
    ax.cla()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = np.arange(0, frame)
    y = np.sin(x * (np.pi / 180))
    ax.plot(x, y, 'r')


def run():
    anim = animation.FuncAnimation(
        fig, animate, frames=720, interval=100)
    plt.show()


run()
