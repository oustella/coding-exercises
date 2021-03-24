# Give a rope of length int(n), you can cut it into m segments of your choosing.
# Each subsegment is also an integer. 
# m >= 1 and n >= 2 (at least one cut is required.) 
# What's the maximum product of the lengths of the subsegments.
# Input: n = 12
# Output: 81 (3*3*3*3)

# strategy:
# n = k + (n-k)
# the subproblem is to find max(k*(n-k)), which becomes
# max(k)*max(n-k)
# let k be i, and n-k be j, 1 <= j < i < n

def maxProduct(n):
    dp = [0] * (n+1)  # for i = 0 to n, there are n+1 numbers
    # dp[1] = 1
    # the overall length of the remaining rope
    for i in range(2, n+1):  # starting from 2, because we already have taken care of dp[1]
        # j is the segment to be cut from i that is shorter
        for j in range(1, i):  
            temp = max(i-j, dp[i-j]) * max(j, dp[j])  # [1]
            dp[i] = max(temp, dp[i])
    return dp[n]


# [1] find max for each of the two segments j and i-j
# i-j is the remaining length if cut j from i
# dp[i-j] is if keeping (not cutting) the current segment 
# j is if not cutting 


if __name__ == "__main__":
    maxProduct(12)
    maxProduct(2)
