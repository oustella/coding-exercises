# OSL 02/12/2021

# implement a stack using linked list
# what is a stack?
# Think of a stack of plates, the first in is the last out.
# Functions:
## Push: to add one more element on top of the stack
## Pop: to remove an element from top of the stack


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class stack():
    def __init__(self) -> None:
        self.head = Node("head")
        self.size = 0

    def printStack(self):
        if self.size == 0:
            print('Empty stack!')
        top = self.head.next
        while top:
            print(top.value)
            top = top.next
    
    def push(self, value):
        '''
        The idea is to insert the new node to the front of the linked list,
        so that the top of the stack is always next to Head.
        '''
        new = Node(value)
        new.next = self.head.next
        self.head.next = new
        self.size += 1

    def pop(self):
        if self.size>=1:
            popped = self.head.next.value
            self.size -= 1
            self.head.next = self.head.next.next
            return popped
        else:
            print('Nothing to pop!')
    
    def getTop(self):
        return self.head.next.value


if __name__ == "__main__":
    mystack = stack()
    for i in range(3):
        mystack.push(i)
    mystack.printStack()
    print("Top of the stack is:", mystack.getTop())


    for _ in range(4):
        print("Popped:", mystack.pop())

    mystack.printStack()

