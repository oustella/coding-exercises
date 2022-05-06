# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s such that every character in t (including duplicates) 
# is included in the window. If there is no such substring, return the empty string "".
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Strategy: sliding window
# Turn the target string into a Counter object of needed chars and their counts `need`
# Start a missing count with all chars in target string
# Advance a right pointer (j) from the begining. If it read a char in `need`, reduces the missing count by 1
# Record the read char in need. 
# When missing reaches 0, a candidate emerges.
# At this point the sliding window hasn't been shrunk yet.
# So if there is more than one candidate, move the left pointer (i) until the needed chars have a balance of 0
# [1] need acts as a sliding window. For a char in target, need[char] == 0 means condition has been met
# For a char not in target, need[char] means it has been excluded from the sliding window
#%%
import collections

from smart_open import s3_iter_bucket
class Solution:

    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)  #[1]
        i = I = J = 0  # i is left pointer, I and J are current best solution for left and right pointer
        for j, char in enumerate(s, start=1):  # j is right pointer that starts with 1 so that if there's no solution, J is still 0
            print(char, need)
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # each char in t is in the window at least once
                while i < j and need[s[i]] < 0:  # when need[s[i]] < 0 it means a target char is in the window at least one time more than needed
                    need[s[i]] += 1   # shrink the window from the left to exclude s[i]
                    i += 1
                if not J or j - i <= J - I:  # if best right pointer has not been updated and a condition meets (no missing values) or a shorter subsequence is found
                    I, J = i, j
        return s[I:J]

#%%
# Note: if providing an unknown key to a regular dictionary
# It will produce an error.
test = {"a": 1, "b": 2}
try: 
    test["c"]
except:
    print('error!')

# HOWEVER, if it is Counter or default dict
# Then, providing an unknown key return a value 0
s = "abc"
counter = collections.Counter(s)
counter["d"]    

# %%
solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
solution.minWindow(s, t)

# %%
