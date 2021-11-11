# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python


#[1] need acts as a sliding window. For a char in target, need[char] == 0 means condition has been met
# For a char not in target, need[char] means it has been excluded from the sliding window
class Solution:

    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)  #[1]
        i = I = J = 0  # i is left pointer, I and J are current best solution for left and right pointer
        for j, c in enumerate(s, 1):  # j is right pointer that starts with 1 so that if there's no solution, J is still 0
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

