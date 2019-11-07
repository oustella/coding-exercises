# all things LinkedList


class ListNode():
    def __init__(self, x):
        self.value = x
        self.next = None


# singly linked list
class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):  # insert a new head at the beginning of the linked list
        newNode = ListNode(data)
        newNode.next = self.head  # point to the existing head first and inherit all the links
        self.head = newNode  # reassign the head to the new head

    def push(self, data):  # add a new node at the end of the linked list
        newNode = ListNode(data)
        current = self.head
        while current.next:  # you want current to arrive at the last node after the last iteration
            current = current.next
        current.next = newNode

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print("")

    def reverse(self):  # see tutorials at https://www.geeksforgeeks.org/reverse-a-linked-list/
        prev = None
        current = self.head
        while current:
            next = current.next  # save the next element before redirecting the current pointer. Otherwise you will lose it.
            current.next = prev  # point current to the previous element or None for the first element
            prev = current  # move prev and current one node forward
            current = next
        self.head = prev  # in the end current and next become none and prev arrives at the last element which is the first.

    def removeKFromList(self, k): # remove nodes if value equal to k
        current = self.head
        while current:  # you want to go through the entire linked list so the last element needs to be examined
            if current.value == k:  # if the head value is k, assign a new head to the next element
                self.head = current.next
                current = current.next  # move along the pointer
            elif current.next and current.next.value == k:  # if the next value is k, skip that node
                current.next = current.next.next
                current = current.next
            else:
                current = current.next

    def getMiddle(self):  # return the start of the second half of the linked list.
        m = self.head  # m moves one node at a time
        n = self.head  # n moves two nodes at a time. By the time n reaches the end, m is half way through.
        while n and n.next:
            m = m.next
            n = n.next.next
        return m.value  # m arrives at N//2 where N is the length of the linked list. m has moved N//2 times from first position.


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.printLL()

ll.push(2)
ll.push(3)
ll.printLL()

ll.reverse()
ll.push(3)
ll.printLL()


ll.removeKFromList(3)
ll.printLL()

test = [3, 1, 2, 3, 4, 5]
def getLL(test):
    ll2 = LinkedList()
    for i in test:
        ll2.insert(i)
    return ll2

ll2.removeKFromList(3)
ll2.printLL()

test = [3, 1, 2, 3, 4, 5]
ll_test = getLL(test)
ll_test.printLL()

ll_test.getMiddle()

ll_test.reverse()
ll_test.printLL()

test = [3, 1, 3, 4, 5]
ll_test = getLL(test)
ll_test.printLL()
ll_test.getMiddle()
#
# # set i to point to middle of list using runner j
# l = node1
# i = j = l
#
# while j.next != None:
#     j = j.next.next
#     if j == None:
#         break
#     i = i.next
#
# print(i.value)
# print(j.value)
