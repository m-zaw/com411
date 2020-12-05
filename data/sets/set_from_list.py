def observed():
    observations = []

    for i in range(0, 7):
        print("Please enter an observation:")
        observation = input()
        observations.append(observation)

    return observations


def run():
    print("Counting observations...")
    observations = observed()
    observation_set = set()

    for observation in observations:
        observation_set.add((observation, observations.count(observation)))

    for observation in observation_set:
        print("{} observed {} times.".format(observation[0], observation[1]))


run()
