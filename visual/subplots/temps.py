import matplotlib.pyplot as plt


def read_data(file_name):
    temps = []
    with open(file_name) as file:
        for line in file:
            temps.append(float(line.replace("\n", "")))
    return temps


def run():
    data = read_data("visual/subplots/temps.txt")
    x = list(range(1, len(data)+1))
    fig, axs = plt.subplots(1, 2)
    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[0].plot(x, data)

    axs[1].set_xlabel("Day")
    axs[1].set_ylabel("Temperature")
    axs[1].bar(x, data)
    plt.tight_layout()
    plt.show()


run()
