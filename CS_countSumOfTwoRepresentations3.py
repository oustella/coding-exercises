# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B
# such that l ≤ A ≤ B ≤ r.
# https://app.codesignal.com/challenge/mXCWzh37ibxEY822h


def countSumOfTwoRepresentations3(n, l, r):

    # solution 1 too slow
    # count = 0
    # solutions = []
    # for intA in range(l, r+1):
    #     # print(intA)
    #     if l <= n-intA <= r and n-intA not in solutions:
    #         solutions.append(intA)
    #         count += 1
    # return count

    # solution 2 too slow
    # count = 0
    # for intA in range(l, r+1):
    #     if l <= n-intA <= r:
    #         count += 1
    # return count//2 if count%2 == 0 else count//2+1

    # solution 3 passed
    count = 0
    for intA in range(l, n // 2 + 1):
        if l <= n - intA <= r:
            count += 1
    return count