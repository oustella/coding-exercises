# dfs with state
# backtracking

def permutation(s):
    def dfs(path, visited, res):
        if len(path) == len(s):
            res.append(path[:])
            return
        for i, element in enumerate(s):
            if visited[i] == True:
                continue
            else:
                path.append(element)
                visited[i] = True
            dfs(path, visited, res)
            path.pop()
            visited[i] = False
    res = []
    dfs([], [False for _ in range(len(s))], res)
    return res

test = "abc"
print(permutation(test))