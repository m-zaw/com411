def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods), max(likelihoods))

def run():
    li = likelihood()
    print("Minimum likelihood of falling: {}% \nMaximum likelihood of falling: {}%".format(li[0], li[1]))

run()