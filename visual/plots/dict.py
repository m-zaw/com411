import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}

    print("What type of line (:, -- or -)?")
    line_style = input()

    print("What colour (r, g or b)?")
    colour = input()

    print("What type of marker (o, s or ^)?")
    marker_style = input()

    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style

    return paths


def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for num_line in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


run()
