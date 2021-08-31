def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

isPalindrome('hello')
isPalindrome('racecar')