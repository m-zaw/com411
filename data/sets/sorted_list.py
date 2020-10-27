def observed():
    observations = []
    for i in range(0, 5): 
        print("Please enter an observation:")
        item = input()
        observations.append(item)
        return observations

def remove_observations(observations):

    is_running = True
    while(is_running):
        print("Do you wish to remove an observation (yes/no)?")
        answer = input()

        if(answer == "yes"):
            print("What would you like to remove?")
            to_remove = input()
            observations.remove(to_remove)
        else:
            break
            # is_running = False - 2nd way

def run():
    observations = observed()
    remove_observations(observations)

    observations_set = set()
    for observation in observations:
        occurences = observations.count(observation)
        observations_set.add((observation, occurences))

    for key, value in sorted(observations_set):
        print(f"{key} observed {value} times")

run()