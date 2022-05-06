# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

# strategy: two pointers / sliding window

# %%
# Use a hashmap to record the indices of the chars that are read
def lengthOfLongestSubstring(s: str) -> int:
    curMax = 0
    lp = 0
    window = {}
    for rp in range(len(s)):
        curChar = s[rp]
        if curChar in window and lp <= window[curChar]:  # [1]
            lp = window[curChar] + 1
        # update the char with the new index in the window    
        window[curChar] = rp
        curMax = max(curMax, rp-lp+1)
    return curMax

s = "abba"
print(lengthOfLongestSubstring(s))

# [1] `lp <= window[curChar]` is crucial if a char existed in the past
# but the left pointer has already moved passed it. This negates the need to
# remove a key from a dictionary which is O(n)
    
# Strategy 2 uses a deque to record characters in the sliding window
from collections import deque
def lengthOfLongestSubstring(self, s: str) -> int:
    path = deque([])
    lp = 0
    currMax = 0
    rp = 0
    while rp < len(s):
        if s[rp] in path:
            path.popleft()
            lp += 1
        else:
            path.append(s[rp])
            rp += 1
        currMax = max(currMax, rp-lp)
    return currMax
