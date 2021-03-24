# use deque to implement a stack (LIFO) or a queue (FIFO) in Python. 
# compared to list, deque offers O(1) time complexity for append and pop
# list can have O(n) time complexity for append if the list grows out of preallocated memory
from collections import deque

stack = deque()
print(len(stack))

stack.append('a')
stack.append('b')
stack.append('c')
stack.pop()
stack.pop()

# FIFO
stack.appendleft('e')
stack.appendleft('f')
print(stack)
stack.popleft()
stack.popleft()