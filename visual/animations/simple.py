import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


def animate(frame):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(frame, frame, 'ro')


def run():
    anim = animation.FuncAnimation(
        fig, animate, frames=10, interval=1000)
    plt.show()


run()
