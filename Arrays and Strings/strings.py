# strings common strategies:
# 1. hash and store
# 2. two pointer
# 3. sort

##############################
# Q1 convert string representation of integers into integers
# e.g. "123" -> 123
# e.g. "-123" -> -123

# "123" becomes 1*100 + 2*10 + 3*1
# 1*10^2 + 2*10^1 + 3*10^0
# 10 exponent = len(s)-i-1

def string2int(s):
    r = 0
    # index in the string from left to right
    i = 0
    # handle negative numbers
    negative = False
    N = len(s)  # length of the string
    if s[0] == "-":
        negative = True
        N -= 1
    # traverse down the string
    for l in s:
        # if the first letter is a sign then do nothing, but index should still be 0
        if l != "-":
            r += (ord(l)-ord("0")) * 10**(N-i-1)
            i += 1
    return -1*r if negative else r

# or 123 can be calcluate in three iterations
# 1. 0*10 + 1 = 1
# 2. 1*10 + 2 = 12
# 3. 12*10 + 3 = 123
def string2int2(s):
    r = 0
    # handle negative numbers
    sign = 1
    # traverse down the string
    for l in s:
        # if the first letter is a sign
        if l == "-":
            sign = -1
        else:
            r = r*10 + (ord(l)-ord("0"))
    return sign*r

string2int(str(-2**31))
string2int2(str(-2**31))

##############################
# Note to convert a single digit 0-9 in char to int use `ord(char)-ord("0")`
# `ord` returns the unicode of a character
# calculate the distances between two unicodes
ord("9")-ord("0")  # "9"->9
# 'chr' returns the character based on a unicode
# the unicode of "0" plus 9 positions becomes the unicode of "9"
chr(9+ord("0")) # 9-> "9"
##############################


##############################
# Q2. Convert int to string
# e.g. 123 to "123"

# 1 = 123//100
# 2 = 23//10
# 3 = 3
# conccat them in order

# or,
# 3 = 123 % 10
# 2 = 12 % 10
# 1 = 1 % 10
# then need to concat them in reverse order because you get 3 first 

# Note string is immutable
# Also note string concatenation in Python has O(n^2) time complexity
# So it's better to use list and then join
def int2str(a):
    # make sure edge case 0 is accounted for
    if a == 0:
        return "0"
    r = []
    # this logic only works when the number is positive
    # because -123//10 = -13, not -12
    negative = a<0
    a = abs(a)
    while a != 0:
        d = a % 10
        r.append(chr(d+ord("0")))
        a = a // 10
    # inplace reverse
    r.reverse()
    return "-"+"".join(r) if negative else "".join(r)
int2str(-199)


##############################
# Q3. Reverse a sentence
# e.g. "What a wonderful world" -> "World Wonderful a What"
def reverseASent(input):
    # the `split()` method doesn't return space
    # by default separator is any number of white spaces
    words = [i for i in input.split()]
    words.reverse()
    return " ".join([i for i in words])

input = "What  a wonderful world"
reverseASent(input)

##############################
# Interconvert strings and integers
# input "abcdef"
# output "badcfe"

def interconvert(s, k):
    i = 0
    r = ""
    while i < len(s):
        print(i)
        r += s[:i][::-1]
        i += k

    if i < len(s)-1:
        r += s[i:]
    return r

a = "abcdef"
interconvert(a, 3)


################################
# generate all permutations of a string
# n*(n-1) = n! 
# e.g. abc; [abc, acb, bac, bca, cab, cba]

def permute(a):
    if len(a)==1:
        return a
    if a is None:
        return None
    r = []
    for i in range(len(a)):
        cur = a[i]
        print("cur", cur)
        remaining = a[:i]+a[i+1:]
        for p in permute(remaining):
            r.append(cur+p)
        print()
    return r

permute("abd")


# compare to subarray/substrings 
# n*(n+1)/2
# e.g. [1,2,3]; [1],[1,2],[1,2,3],[2],[2,3],[3]

# compare to subsequences
# 2^n-1
# e.g. [1,2,3]; [1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]


test = {}
test[1] = 1
print(test)