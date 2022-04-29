#%%
def isMatch(s: str, p: str) -> bool:
    dp = [False for _ in range(len(s))]
    if s[0] == p[0] or p[0] == ".":
        dp[0] = True
    j = 1
    while j < len(s):
        for i in range(1, len(p)):
            if s[j] == p[i] or p[i] == ".":
                dp[j] = True
                j += 1
            elif p[i] == "*": 
                for j in range(i, len(s)):
                    if s[j] == s[j-1]:
                        dp[j] = True
                    else:
                        break
                j += 1
            else:
                return False
    return all(dp)
# %%
s = "ab"
p = ".*"
isMatch(s, p)
# %%
