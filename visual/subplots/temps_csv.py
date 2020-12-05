import csv

import matplotlib.pyplot as plt


def read_data():
    data = {
        "week1": [],
        "week2": []
    }

    with open("visual/subplots/temps.csv") as file:
        csv_reader = csv.reader(file, delimiter=",", quotechar='"')

        for row in csv_reader:
            data["week1"].append(row[0])
            data["week2"].append(row[1])

    return data


def run():
    data = read_data()

    fig, axes = plt.subplots(2, 1, sharex="all")

    x = range(1, len(data["week1"]) + 1)

    axes[0].plot(x, data["week1"])
    axes[0].set_xlabel("Day")
    axes[0].set_ylabel("Temperature")

    axes[1].plot(x, data["week2"])
    axes[1].set_xlabel("Day")
    axes[1].set_ylabel("Temperature")

    plt.tight_layout()
    plt.show()


run()
