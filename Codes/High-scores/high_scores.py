def latest(scores):
	return scores[-1]


def personal_best(scores):
	return max(scores)


def personal_top_three(scores):
	if len(scores) >= 3:
		scores.sort()
		lst = [scores[i] for i in [-1, -2, -3]]
		return lst
	else:
		scores.sort(reverse = True)
		return scores

