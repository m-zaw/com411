def movements():
    path = ["move forward",10,"move backwards",5,"move left",5,"move right",1]
    return path 

def run():
    print("Moving...")
    movements() 
    direction = movements()
    print("{} for {} steps".format(direction[0],direction[1]))
    print("{} for {} steps".format(direction[2],direction[3]))
    print("{} for {} steps".format(direction[4],direction[5]))
    print("{} for {} steps".format(direction[6],direction[7]))

run()