# return the maximum length of the subarray of a string that is a palindrome.
# input: "aabccb"
# output: 4
# also print the longest palindrome subarray

# This method doesn't work for "cbbd"
#%%
def maxP(s):
    n = len(s)
    # initiate an array with len(s) row and len(s) column
    # dp[i][j] is the whether str[i:j+1] is a palindrome. Boolean values.
    dp =[[False for i in range(n)] for j in range(n)]
    # starting point for longest palindrome is 1
    maxL = 1
    # record the starting index of the longest palindrome subarray
    start = None
    # all single letters are palindrome 
    for i in range(n):
        dp[i][i] = True
    # two pointers 
    # check all the letters up to r - the rightmost letter
    i = 0
    for r in range(n):
        for l in range(r):
            i+=1
            # test two adjacent letters
            if s[l] == s[l+1]:
                dp[l][l+1] = True
            # test palindroms longer than 2
            # if dp[l+1][r-1] the inner segment is already a palindrome
            # then expands outwards two letters
            if dp[l+1][r-1] and s[l] == s[r]:
                dp[l][r] = True
                # print(l, r, "yay")
                if r - l + 1 > maxL:
                    maxL = r - l + 1
                    start = l
    # print("Longest palindrome subarray is", s[start:start+maxL])
    print(i)
    return maxL

#%%
print("max length", maxP("aabccb"))

#%%
print(maxP("abbabbabba"))
print(maxP("aba"))

# %%
print(maxP("cbbd"))
# %%
