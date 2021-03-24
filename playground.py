# permutations of strings of unique characters
def permute(s, l ,r, results):  # put results (list) as a parameter for recording
    s = list(s)
    if l == r:  # when l=r, the swap is at the end of the string, so it's the end result
        results.append("".join(s))
    for i in range(l,r+1):  # r+1 to make sure the range has one value in it when it is the last character of the string
        s[i], s[l] = s[l], s[i]
        permute(s, l+1, r, results)
        s[i], s[l] = s[l], s[i]
    return results
permute("abc", 0, 2, [])

from collections import defaultdict
test = defaultdict(int)
test[0] = 1
test[0]