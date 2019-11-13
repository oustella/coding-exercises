# Refer to https://leetcode.com/problems/merge-sorted-array/ for input variable definitions

def merge(self, nums1, m, nums2, n):
    """
    This method is by Leetcode user cffls.
    It adds the larger number of the two arrays to the end of nums1.
    It then compares the second largest of one array to the largest of the other array.
    The array that has more larger numbers are "used up" more quickly.
    If nums1 reached to the front first, all numbers left in nums2 are smallers and can be added to the beginning of nums1.
    If nums2 reached to the front first, all numbers left at the beginning of nums1 need not change.
    """
    while m > 0 and n > 0:  # go from the end of the arrays
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:  # if when in nums1 all numbers are used up (larger) and still a few left in nums2, put them in front.
        nums1[:n] = nums2[:n]