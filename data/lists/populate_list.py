def directiontions(): 
    directiontions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directiontions

def menu(): 
    route = []
    direction = directiontions()
    print ("Please select a directiontion: ")
    
    for count in range(0 , 5, 1):
        print("")
    for count in range(0 , 4, 1):
        print ("{0}:{1}" .format(count, direction[count]))
    
    user_reply = int(input())
    route.append(direction[user_reply])
    return route

def run(): 
    print ("Working out escape route...")
    route = menu()
    print ("Escape route {}" .format(route))

run()