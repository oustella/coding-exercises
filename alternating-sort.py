# take the first element from an array, then the last, then the second, then the last but one in an alternating way.
# return Boolean whether the elements are sorted


def alternatingSort(a):
    n = len(a)
    i = 0  # front pointer from the beginning of the array
    j = -1  # end pointer from the end
    if n == 1:
        return True
    elif n % 2 == 0:  # an even length array will have complete pairs for comparison
        print('Even array')  # debugging
        while i < n // 2:  # last pair for comparison is in the middle. don't need to condition on j because i, j always move together
            if a[i] > a[j]:  # if front pointer is greater than end pointer
                return False
            else:
                i += 1
                j -= 1
        return True
    else:  # an odd length array has one additional front pointer
        print('Odd array')
        while i < n // 2:  # note // gets you the integer in a division. don't confuse with %
            print(i, j)  # debugging
            if a[i] > a[j]:
                return False
            else:
                i += 1
                j -= 1
        print("one last comparison")
        print(i, i+1)
        if a[i] > a[i+1]:  # no need to involve j, just the addition front pointer and the element on the right
            return True
        else:
            return False


test1 = [-52, 2, 31, 56, 47, 29, -35]
test2 = [1, 2, 3, 4, 5]
test3 = [1, 3, 4, 5]

alternatingSort(test1)

alternatingSort(test2)

alternatingSort(test3)

