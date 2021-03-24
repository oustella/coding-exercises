import heapq

a = [1,93,5,62,16]
heapq.heapify(a)  # in-place heapify
# the order of a heapified list is not to be trusted by naked eyes
# e.g. the following can correctly return 93 and 62
# but the print shows a list that's not sorted
heapq.nlargest(2, a)
print(a)

