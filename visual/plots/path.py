import matplotlib.pyplot as plt


def coordinate():
    x = float(input("Please enter x value:"))
    y = float(input("Please enter y value:"))

    return (x, y)


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for i in range(0, 4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]


def run():
    values = path()

    plt.plot(values[0], values[1], "r--o")
    plt.show()


run()
