# crypt contains three words, solution contains key to each letter
# check whether the first two words add up to the third word.
# numbers like 064 with a leading zero in front is not valid.

crypt_test = ["SEND",
 "MORE",
 "MONEY"]

solution_test = [["O","0"],
 ["M","1"],
 ["Y","2"],
 ["E","5"],
 ["N","6"],
 ["D","7"],
 ["R","8"],
 ["S","9"]]


def getKeyDict(solution):  # convert solution list to a dictionary for easy access
    sol = {}
    for pair in solution:
        sol[pair[0]] = pair[1]
    return sol


def convertWord(word, solution):  # replace each char with a numb
    word_key = []
    for i, char in enumerate(word):
        key = getKeyDict(solution)[char]
        word_key.append(key)
    if len(word_key) > 1 and word_key[0] == "0":  # invalid if a number starts with 0 but not 0
        return False
    else:
        return int("".join(word_key))


def isCryptSolution(crypt, solution):
    if type(convertWord(crypt[0], solution)) == int and type(convertWord(crypt[1], solution)) == int and type(
            convertWord(crypt[2], solution)) == int:
        if convertWord(crypt[0], solution) + convertWord(crypt[1], solution) == convertWord(crypt[2], solution):
            return True
        else:
            return False
    else:
        return False


# critique1: getKeyDict() can be written in one line:
# {pair[0]: pair[1] for pair in solution}
# or even better:
# dict(solution)

# critique2: convertWord() can be replaced by str.translate() in tandem with str.maketrans()
# or use str.replace()

# Solution by CS user jlhamilton
def isCryptSolution(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)  # any() returns True if any element of the iterable is true
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])  # use and to implicitly test two conditions simultaneously
