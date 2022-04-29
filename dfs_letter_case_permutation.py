# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(i, temp, res):
            if i == len(s):
                res.append("".join(temp[:]))
                return
            nex = s[i].lower()
            if nex >= "a":
                temp.append(nex.swapcase())
                dfs(i+1, temp, res)
                temp.pop()
            temp.append(nex)
            dfs(i+1, temp, res)
            temp.pop()
                        
        res = []
        dfs(0, [], res)
        return res