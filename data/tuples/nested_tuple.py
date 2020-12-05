def steps():
    percentages = [50, 38, 27, 99, 4]
    likelihoods = []
    for a in range(len(percentages)):
        step = "step " + str(a + 1)
        step_likelihood = (step, percentages[a])
        likelihoods.append(step_likelihood)
    return likelihoods


def run():
    good_steps = []
    bad_steps = []
    for a in range(len(steps())):
        if steps()[a][-1] >= 50:
            bad_steps.append(steps()[a])
    else:
        good_steps.append(steps()[a])
    print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))


run()
