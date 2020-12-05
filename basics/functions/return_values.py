def sum_weight(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight


def avg_weight(beep_weight, bop_weight):
    average = (beep_weight + bop_weight) / 2
    return average


def run():
    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    action = input()

    if (action == "sum"):
        answer = sum_weight(beep_weight, bop_weight)
        print("The sum of Beep and Bop's weight is {}.".format(answer))
    elif (action == "average"):
        answer = avg_weight(beep_weight, bop_weight)
        print("The avg of Beep and Bop's weight is {}.".format(answer))
    else:
        print("Ation not recognised")


run()
