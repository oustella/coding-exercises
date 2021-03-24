# https://leetcode.com/problems/permutation-in-string/
# given string s1, return true if s1 or a permutation of s1 is a substring of s2

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutations have to 
        # 1. contain all letters that are together  -> sliding window
        # 3. the order of the letters is not important -> hashmap
        if len(s1) > len(s2):
            return False
        s1map = collections.Counter(s1)
        l = len(s1)  # lenght of sliding window
        for i in range(len(s2)-l+1):
            s2map = collections.Counter(s2[i:i+l])  # note this is not a "real" sliding window [1]
            if s1map == s2map:
                return True
        return False
        
# [1] sliding window is about remove the previous and add the new to calculate sum