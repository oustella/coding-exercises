# https://www.hackerrank.com/challenges/30-queues-stacks/problem?isFullScreen=false

import sys
import queue


class Solution:

    def __init__(self):  # initialize a queue and a stack using Python queue module
        self.aque = queue.Queue()
        self.astack = queue.LifoQueue()

    def pushCharacter(self, ch):
        self.astack.put(ch)

    def enqueueCharacter(self, ch):
        self.aque.put(ch)

    def popCharacter(self):
        ch = self.astack.get()
        return ch

    def dequeueCharacter(self):
        ch = self.aque.get()
        return ch


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")