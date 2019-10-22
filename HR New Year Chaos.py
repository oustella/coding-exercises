# https://www.hackerrank.com/challenges/new-year-chaos/problem


def minimumBribes(q):
    counts = 0
    for current_i, num in enumerate(q):
        orig_i = num - 1
        moves = orig_i - current_i
        if moves > 2:
            return 'Too chaotic'
        else:
            if current_i > 0:
                for j in range(max(orig_i - 1, 0), current_i):
                    if q[j] > num:
                        counts += 1
    return counts
