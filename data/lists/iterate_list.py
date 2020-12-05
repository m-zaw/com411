def directions():
    directions = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print("{}: {}".format(index, direction[index]))


def run():
    menu()


run()
