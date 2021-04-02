# Under-construction as of 3/25/2021

# Given a string and a vocab dictionary, output all posssible combinations of substrings from the dictionary
# input: s = "abcde", vocab = ["ab", "cd", "e", "cde"]
# output: [["ab", "cd", "e"], ["ab", "cde"]]

# strategy:
# move a pointer from left to right, see if the substring s[:i]is in the vocab
# if it is, append it to a result, and keep moving from s[i:]
# if it is not, then 
# if it reaches the end when s becomes empty, then it is an accpetable combination.


# def wordSplit(s, vocab):
#     results = []
#     results.append(back_track(s, vocab))
#     return results

# current_solution = []
def wordSplit(s, vocab):
    def dfs(s, path, res):
        if not s: 
            res.append(path[:])
            return 
        for i in range(1, len(s)+1):
            if s[:i] in vocab:
                path.append(s[:i])
                dfs(s[i:], path, res)
                path.pop()
    res = []
    dfs(s, [], res)
    return res

if __name__=="__main__":
    s = "abcde"
    vocab = ["a","ab", "cd", "e", "cde"]
    wordSplit(s, vocab)