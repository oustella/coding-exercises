# generate the nth fibnacci number
# dynamic programming, top-down approach 
def getFib(n):
    memo = [None for _ in range(n+1)]
    def dp(n, memo):
        if memo[n]:
            return memo[n]
        if n == 0 or n == 1:
            return n
        memo[n] = dp(n-1, memo) + dp(n-2, memo)
        return memo[n]
    return dp(n, memo)

getFib(4)

# dynamic programming, bottom-up approach
def getFib2(n):
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]

getFib2(4)
