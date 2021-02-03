# Return distinct values from a list including duplicates
# Given {1, 2, 6, 6, 6, 10, 14, 14} ; Return -> {1, 2, 6, 10, 14}

# use hash table
def returnNum(alist):
    # this can be achieved by Counter but we are implementing it from scratch
    myhash = {}
    for n in alist:
        if n not in myhash:
            myhash[n] = 1
        else:
            myhash[n] += 1
    return list(myhash.keys())

# sort and then return numbers that are larger than the one before
# only when it is not required that the original order be kept.
def returnNum2(alist):
    slst = sorted(alist)
    r = [slst[0]]
    for i in range(len(slst)):
        if i<= len(slst)-2 and slst[i+1] > slst[i]:
            r.append(slst[i+1])
    return r



# test
a = {1, 2, 6, 6, 6, 10, 14, 14}
b = {15, 6, 10, 5, 12, 6}
c = {1, 1, 1}

for t in [a,b,c]:
    returnNum(t)
    returnNum2(t)