import heapq

a = [1,93,5,62,16]
heapq.heapify(a)  # in-place heapify
# the order of a heapified list is the pre-order view of the binary tree
print(a)

# e.g. the following can correctly return 93 and 62
heapq.nlargest(2, a)

# when the smallest item is popped, the binary tree reorganizes
# and the first element of the heap is always the smallest item
heapq.heappop(a)
print(a)

b = []
for element in a:
    heapq.heappush(b, element)
print(b)
