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


# ooo programming
# 1. recursive + memoization
class FibTopDown(object):
    
    def __init__(self):
        self.cache = {}
        
    def calculate(self, n):
        if n in self.cache:
            return self.cache[n]
        if n < 2:
            return n
        self.cache[n] = self.calculate(n-1) + self.calculate(n-2)
        return self.cache[n]
# 2. iterative / bottom up
class FibBottomUp(object):
    
    def __init__(self):
        self.cache = {}
    
    def calculate(self, n):
        c = self.cache
        c[0] = 0
        c[1] = 1
        if n < 2:
            return c[n]
        for i in range(2,n+1):
            c[i] = c[i-1] + c[i-2]
        return c[n]
    
# 2a. optimized space bottom up
# Because we are working from left to right, small to big numbers
# We only need two previous numbers to calculate the current position
class FibBottomUpOptimized(object):
    
    def calculate(self, n):
        pp = 0
        p = 1
        for _ in range(2, n+1):
            cur = pp + p
            pp, p = p, cur
        return cur
        
if __name__ == "__main__":
    print(FibTopDown().calculate(6))
    print(FibBottomUp().calculate(6))
    print(FibBottomUpOptimized().calculate(6))