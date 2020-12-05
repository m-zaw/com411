def steps():
    likelihoods = []
    likelihoods.append(("step 1", 50))
    likelihoods.append(("step 2", 38))
    likelihoods.append(("step 3", 27))
    likelihoods.append(("step 4", 99))
    likelihoods.append(("step 5", 4))
    return likelihoods


def run():
    likelihoods = steps()
    good_steps = []
    bad_steps = []

    for likelihood in likelihoods:
        if (likelihood[1] >= 50):
            bad_steps.append(likelihood)
        else:
            good_steps.append(likelihood)

    print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))


run()
