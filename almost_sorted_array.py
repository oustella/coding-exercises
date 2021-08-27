# Given an almost sorted array, in which each number is less than m spots away from its correctly sorted position, and the value m, write an algorithm that will return an array with the elements properly sorted.

# An example input would be the list [3, 2, 1, 4, 6, 5] and m = 3. In this example, each element in the array is less than 3 spots away from its position in a sorted array.
import heapq
def my_sort(almost_sorted, m):
    min_heap, res = [], []
    for elem in almost_sorted[:m]:
        heapq.heappush(min_heap, elem)
    
    for elem in almost_sorted[m:]:
        heapq.heappush(min_heap, elem)
        res.append(heapq.heappop(min_heap))

    while min_heap:
        res.append(heapq.heappop(min_heap))
    
    return res

test = [1,3,2,5,6,4]
print(test, my_sort(test, 3))