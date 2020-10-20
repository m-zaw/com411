def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods), max(likelihoods))

def run():
    l = likelihood()
    print("Minimum likelihood of falling: {}% \nMaximum likelihood of falling: {}%".format(l[0], l[1]))

run()