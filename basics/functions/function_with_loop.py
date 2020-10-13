def cross_bridge(distance):
    if (distance > 5):
        for a in range(distance, 0, -1):
            print("Crossed step.")
        print("The bidge is collapsing!")
    elif (distance <= 5):
        for a in range(distance, 0, -1):
            print("Crossed step.")
        print("We must keep going!")

cross_bridge(3)
cross_bridge(5)