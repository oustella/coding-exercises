# partition is the process of slicing a string to different substrings
# e.g. "abc" can be partitioned into [["a", "b", "c"], ["a", "bc"], ["ab", "c"], ["abc"]]
def partition(s):
    ans = []
    def dfs(start, path):
        if start == len(s):
            ans.append(path[:])
            return

        for i in range(start+1, len(s)+1):
            prefix = s[start: i]
            path.append(prefix)
            dfs(i, path)
            path.pop()

    dfs(0, [])
    return ans

# simplified backtracking code
def partition(s):
    ans = []
    def dfs(start, path):
        if start == len(s):
            ans.append(path[:])
            return

        for i in range(start+1, len(s)+1):
            prefix = s[start: i]
            dfs(i, path + [prefix])  # [1]

    dfs(0, [])
    return ans
# [1] This part makes sure path is not permanently modified
# i.e. always return to the previous state when the call stack goes back

partition("abc")

# partition() is concerned with finding all possible partitions
# when the substring can only be in a given list, the code be further simplied.

def partition2(s, allowed):
    ans = []
    def dfs(i, path):
        if i == len(s):
            ans.append(path[:])
            return 
        for candidate in allowed:
            if s[i:].startswith(candidate):
                dfs(i+len(candidate), path + [candidate])
    dfs(0, [])
    return ans

partition2("helloworld", ["hello", "world", "he", "llo", "w"])