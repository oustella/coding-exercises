# Given an unsorted array, return the length of the longest subsequence of ascending order
# a subsequence is a subset of numbers from the original array maintaining the same order
# but the numbers don't have to be next to each other. i.e. skipping elements is allowed.

def longest_subseq_len(nums):
    # dp[i] is the longest sub seq ending at nums[i]
    dp = [1 for _ in range(len(nums))]
    ans = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])
    return ans

longest_subseq_len([10, 9, 2, 5, 3, 7, 101, 18])

            