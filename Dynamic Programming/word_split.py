# Under-construction as of 3/25/2021

# Given a string and a vocab dictionary, output all posssible combinations of substrings from the dictionary
# input: s = "abcde", vocab = ["ab", "cd", "e", "cde"]
# output: [["ab", "cd", "e"], ["ab", "cde"]]

# strategy:
# move a pointer from left to right, see if the substring s[:i]is in the vocab
# if it is, append it to a result, and keep moving from s[i:]
# if it is not, then 
# if it reaches the end when s becomes empty, then it is an accpetable combination.


def wordSplit(s, vocab):
    results = []
    results.append(back_track(s, vocab))
    return results

# current_solution = []
def back_track(s, vocab):
    current_solution = []
    if not s: 
        return current_solution
    for i in range(1, len(s)+1):
        if s[:i] in vocab:
            current_solution.append(s[:i])
            current_solution.extend(back_track(s[i:], vocab))
    return current_solution
back_track(s,vocab)


current_solution
wordSplit(s, vocab)
if __name__=="__main__":
    s = "abcde"
    vocab = ["ab", "cd", "e", "cde"]
    wordSplit(s, vocab)