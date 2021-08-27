# A string consisting of only these characters: “(“, “)”, “[“, “]”, “{“, and “}” is considered well formed if the different types of brackets are matched in the correct order. For example, “{)” would not be well formed and “[(){}]” would be considered well formed. Write a program that returns true if a given string is well-formed and false otherwise.

# strategy: utilize hashmap and array
# if a char is the left part of a pair, read it into a list
# if a char is the right part of a pair, match it with the lastet element in the unmatched list.
# If it is a match, then pop off the left part of the pair from the unmatched.
# If it is not a match or there is no left part to be matched with, return false.
# If the last char of the string is a lone left part, the length of the unmatched list will not be 0, therefore also return false.

def is_well_formed(string):
    pairings = {"(": ")", "{": "}", "[": "]"}
    unmatched_brackets = []
    for char in string:
        if char in pairings:
            unmatched_brackets.append(char)
        elif not unmatched_brackets or pairings[unmatched_brackets.pop()] != char:
            return False
    return len(unmatched_brackets) == 0