# Document Python syntax idiosyncracies

from collections import deque
# the common approach to initiate a queue
queue = deque(["a"])
# but if you don't put the element in a bracket
# it will be automatically put in a bracket for you
queue = deque("a")
print(queue)
# appending subsequent element the first set of [] works as part of the new element to be appended
queue.append(["b"])
print(queue)