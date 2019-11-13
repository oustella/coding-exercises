# https://www.hackerrank.com/challenges/new-year-chaos/problem


def minimumBribes(q):
    counts = 0
    for current_i, num in enumerate(q):
        orig_i = num - 1
        moves = orig_i - current_i
        if moves > 2:  # for those that have moved more than twice, it violates the rule
            return 'Too chaotic'
        else:
            if current_i > 0:
                for j in range(max(orig_i - 1, 0), current_i):  # orig_i-1 because the front number may have bribed twice
                    if q[j] > num:  # numbers that are bigger than ego means ego has received their bribes
                        counts += 1
    return counts
