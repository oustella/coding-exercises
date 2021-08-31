# https://leetcode.com/problems/palindrome-partitioning/solution/
from typing import List

class Solution:

    def partition(self, s: str) -> List[List[str]]:

        def dfs(start, res, path, level):
            level += "  "  # use level to print debugging series
            if start >= len(s):
                res = min(res, len(path[:]))
                return 

            for end in range(start, len(s)):
                print(level, 'check', start, end)
                if self.isPalindrome(s[start:end+1]):
                    path.append(s[start: end+1])
                    dfs(end+1, res, path, level)
                    path.pop()

        res = float('inf')
        dfs(0, res, [], "")
        return res
            
    
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False

solution = Solution()
solution.isPalindrome('abba')
res = []
solution.partition('abb')
solution.partition('abba')
