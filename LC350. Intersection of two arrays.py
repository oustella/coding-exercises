
# this approach is O(N*N)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 <= len2:
            for i in nums1:
                if i in nums2:
                    output.append(i)
                    nums2.remove(i)  # O(N)

        else:
            for j in nums2:
                if j in nums1:
                    output.append(j)
                    nums1.remove(j)

        return output


# sorted approach
def intersect(nums1, nums2):
    i = 0
    j = 0
    sorted1 = sorted(nums1)
    sorted2 = sorted(nums2)
    output = []
    while i < len(nums1) and j < len(nums2):
        if sorted1[i] == sorted2[j]:
            output.append(sorted1[i])
            i += 1
            j += 1
        elif sorted1[i] < sorted2[j]:
            i += 1
        else:
            j += 1
    return output


# Use a hashmap
from collections import Counter
def intersect(nums1, nums2):
    output = []
    if len(nums1) <= len(nums2):
        nums_short = nums1
        nums_long = nums2
    else:
        nums_short = nums2
        nums_long = nums1

    num_counts = Counter(nums_short)
    for i in nums_long:
        if i in num_counts:
            if num_counts[i] > 0:
                output.append(i)
                num_counts[i] -= 1
    return output


