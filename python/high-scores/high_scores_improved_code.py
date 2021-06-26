def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)
    # or
    # return personal_top_three(scores)[0]


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]