# return the index of a character starting from the rightmost character
# note it still returns the index according to the left-to-right order
astring = 'abcdcdba'
astring.index('b')
astring.rindex('b')


# range(0) returns an empty list
list(range(0))  # returns an empty list
list(range(1, 2))  # returns 1
list(range(1))  # returns 0
list(range(4, 2))  # put a number in front of a smaller number returns an empty range


# this construct traverse through the lower left diagonal half of a square without touching the diagonal line
def updateHalf(arr, n):
    for i in range(len(arr)):
        for j in range(i):
            arr[i, j] = n


import numpy as np
test_arr = np.identity(5)
updateHalf(test_arr, 3)
print(test_arr)


# this expression traverse from the end to front
test_list = [1, 2, 3, 4]
test_list[::-1]
list(reversed(test_list))  # same effect

testArr = [[1,2,3], [4,5,6], [7,8,9]]  # works only on the out most layer
testArr[::-1]


# create a square of size n out of an array for a starting point (i,j)
def get_square(i, j, n):
    square = ([x[j:j+n] for x in testArr[i:i+n]])
    return square


testArr = [[1,0,1],[1,1,1],[1,1,1]]
square = get_square(0,0,2)
print(square)

for row in square:
    for i in range(len(row)):
        if row[i] == 1:
            continue
        else:
            break

# `all()` and `any()` only works with one level of list
test = [1,0,1]
all(x==1 for x in test)  # returns False

all(x[:]==1 for x in testArr)
# this effectively evaluates `all([False, False, False])`
# because the inner iterable is the results of you are comparing x[:] which is a list to the value 1.


testArr = [[1,1,1],[1,1,1],[1,1,1]]
all(y==1 for x in testArr for y in x)  # returns True. Pay attention to the syntax for the nested list comprehension.

testArr = [[1,0,1],[1,1,1],[1,1,1]]
all(y==1 for x in testArr for y in x)  # returns False.


# develop a function that checks if all values equal to 1
def check_all(arr):
    for row in arr:
        if all(x==1 for x in row):
            continue  # continue is to go to the next iteration of the loop
            # break terminates the nearest enclosing loop, skipping else
            # pass does nothing
        else:
            return False
    return True


testArr = [[1,1,1],[1,1,1],[1,1,1]]
[x for x in row for row in testArr]
check_all(testArr)

testArr = [[1,1,1],[1,0,1],[1,1,1]]
check_all(testArr)


# integer division operator // in Python3 uses floor division where the result is rounded down
-3//2  # gives -2
3//2  # gives 1


# Single * operator means any number of positional arguments
# double ** operator means keyword arguments. Using the keyword as keys of a dictionary
def foo(**kwargs):
    for key in kwargs:
        print(kwargs[key])


foo(arg1=1, arg2=3)

myDict = {'a':1, 'b':2}
foo(**myDict)  # ** helps unpack a dictionary


def bar(*args):
    for a in args:
        print(a)


testArr = [[1,2,3], [4,5,6], [7,8,9]]
bar(*testArr)  # * helps unpack a list/tuple


# This will create unintended behavior: if you change [i][j], the value on the other rows will change too.
n = 5
new_arr = [[0] * n] * n
new_arr
new_arr[2][3] = 1
print(new_arr)

# better to use list comprehension
new_arr = [[0 for x in range(n)] for x in range(n)]
new_arr
new_arr[2][3] = 1
print(new_arr)


# access individual digits from right to left of an integer
def getDigits(n):
    while n:  # until the division leaves nother n = 0 
        digit = n % 10  # integers are base-10
        n = n // 10
        print(digit, n)