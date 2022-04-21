# all things LinkedList


class ListNode():
    def __init__(self, x):
        self.value = x
        self.next = None

    def getLength(self):
        length = 0
        head = self
        while head:
            head = head.next
            length += 1
        return length
        


# singly linked list
class LinkedList():
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def insert(self, data):  # insert a new head at the beginning of the linked list
        newNode = ListNode(data)
        newNode.next = self.head  # point to the existing head first and inherit all the links
        self.head = newNode  # reassign the head to the new head

    def push(self, data):  # add a new node at the end of the linked list
        newNode = ListNode(data)
        current = self.head
        # if the LinkedList is empty
        if current:
            while current.next:  # you want current to arrive at the last node after the last iteration
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    # This push method is fine in a class, but as an independent function it will lose the head.
    # See 'merge_two_sorted_linkedlist.py' for an alternative push that keeps the head.

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print("")

    def reverse(self):  # see tutorials at https://www.geeksforgeeks.org/reverse-a-linked-list/
        prev = None
        current = self.head
        next = None
        while current:
            next = current.next  # save the next element before redirecting the current pointer. Otherwise you will lose it.
            current.next = prev  # point current to the previous element or None for the first element
            prev = current  # move prev and current one node forward
            current = next
        self.head = prev  # in the end current and next become none and prev arrives at the last element which is the first.

    def removeKFromList(self, k): # remove nodes if value equal to k
        current = self.head
        while current:  # you want to go through the entire linked list so the last element can be examined
            if current.value == k:  # if the head value is k, assign a new head to the next element
                self.head = current.next
                current = current.next  # move along the pointer
            # check the next value, not the current value, so that we don't lose the 'prev' relative to the node to be removed
            elif current.next and current.next.value == k:  
                current.next = current.next.next
                current = current.next
            else:
                current = current.next

    def getMiddle(self):  # return the start of the second half of the linked list.
        m = self.head  # m moves one node at a time
        n = self.head  # n moves two nodes at a time. By the time n reaches the end, m is half way through.
        # since n moves two nodes at a time via .next.next, need to make sure n.next is valid
        while n and n.next:
            m = m.next
            n = n.next.next
        return m.value  # m arrives at N//2 where N is the length of the linked list. Index at N//2 is always the beginning of the second half of an array.


