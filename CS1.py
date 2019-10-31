# Given an array a that contains only numbers in the range from 1 to a.length,
# find the first duplicate number for which the second occurrence has the minimal index.

from collections import Counter

# this method is correct but took too long
def firstDuplicate(a):
    counts = Counter(a)
    dups = [k for k, v in counts.items() if v > 1]

    if len(dups) == 0:
        return -1
    else:
        count_occurences = Counter()
        for num in a:
            if num in dups:
                count_occurences[num] += 1
                if count_occurences[num] == 2:
                    return num


# this method was accepted
def firstDuplicate(a):
    counts = Counter(a)  # use Counter to effectively count frequencies

    # the first time a number's occurrences ticks 2, that's the minimal index
    # because we traverse the list in order
    occurrences = Counter()  # keep track of how many times a num has been read in array
    for num in a:
        if counts[num] > 1:
            occurrences[num] += 1
        if occurrences[num] == 2:
            return num
    if not occurrences:
        return -1
