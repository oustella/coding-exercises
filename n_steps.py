# a child can hop 1,2,3 steps. How many ways to get to n steps?
def countWays2(n):
    if n < 0:
        return 0
    memo = [float("inf")] * (n+1)
    memo[0] = 1
    if memo[n]!= float("inf"):
        return memo[n]
    memo[n] = countWays2(n-1) + countWays2(n-2) + countWays2(n-3)
    return memo[n]


# coin change
# extension: given an array [1,5,4,2,6] with each element representing the number of max allowed steps
# 1. what's the minimum number of jumps to reach the end of the array
#  https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# Note jumps are different then steps. One jump can go over multiple steps.
# Otherwise to go from arr[0] to arr[n-1] always requires n steps
def minJumps(arr, n):
    # jumps records the min steps to arrive at arr[i] from arr[0]
    jumps = [float("inf")] * n  #[1]
    if n==0 or arr[0] == 0:  # arr[0]=0 suggests the steps cannot progress
        return -1
    jumps[0] = 0  # 0 steps from arr[0] to arr[0]

    for i in range(1,n):  # start checking from arr[1] to the last element arr[n-1]
        for j in range(i): # examien all elements prior to the ith step
            if arr[j]>= i-j and jumps[j]!= float("inf"):  #[2]
                jumps[i] = min(jumps[i], jumps[j]+1)  #[3]

    return jumps[n-1]


# [2] i is always behind j in the array. 
# i-j: the distance between two elements. Can arr[j] cover the distance between i and j
# jump[j] != inf makes sure there is a way to get to j.
# because j is always before i, j will already have been tested 
# [3] compare the current min steps to i and the new option from j to i.

# 2. how many different ways to jump out of the array
def jumpWays(arr, n):
    # jumps records the min steps to arrive at arr[i] from arr[0]
    ways = [float("inf")] * n  #[1]
    if n==0 or arr[0] == 0:  # arr[0]=0 suggests the step cannot progress
        return -1
    ways[0] = 1  # 1 way to get to arr[0]
    paths = []
    for i in range(1,n):  # start checking from arr[1] to the last element arr[n-1]
        path = []
        path.append(arr[i])
        for j in range(i): # examien all elements prior to the ith step
            if arr[j]>= i-j and ways[j]!= float("inf"):  #[2]
                ways[i] = ways[j]+1  #[3]
                path.append((arr[j],arr[i]))
        paths.append(path)

    return ways[n-1],paths

if __name__ == "__main__":
    countWays(4)
    countWays2(7)
    minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11)
    minJumps([1, 1, 1], 3)
    jumpWays([1,2,3],3)