# https://app.codesignal.com/challenge/J785w3Xu4BFzqnREg

import numpy as np

def numbersGrouping(a):
    # solution 1 did not pass time limit
    # headings = []
    # num_count = 0
    # for i in a:
    #     group_num =  math.ceil(i / math.pow(10, 4))
    #     if group_num not in headings:
    #         headings.append(group_num)
    #     num_count += 1
    # return num_count + len(headings)

    # solution 2 using vectorized calculation
    real_arr = np.asarray(a)
    groups = np.ceil(real_arr / math.pow(10, 4))
    return len(a) + len(np.unique(groups))

    # solution by user synth
    # dir()[0] is the name of the first of the local variables
    # and eval(dir()[0]) evaluates the variable name, i.e. returns the first local variable's value.
    # you don't really need this line. See https://stackoverflow.com/questions/52046446/what-does-evaldir0-do-in-python
    a, = eval(dir()[0])
    # get the length of two concatenated list
    # *args unpacks the variables in the container
    # {a,b,c} is a value-less dictionary, essentially a set
    # probably better using [*set(-i //1e4 for i in [3,450000,7])]
    # negate the floor division is smart because the heading buckets are [0,1), [1,2], ...
    # floor division is the same as math.floor(a/b)
    return len(a + [*{-i // 1e4 for i in a}])



