# all things LinkedList


class ListNode():
    def __init__(self, x):
        self.value = x
        self.next = None


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

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert(1)
    # ll.insert(2)
    # ll.printLL()

    ll.push(2)
    ll.push(3)
    ll.printLL()
#
# ll.reverse()
# ll.push(3)
# ll.printLL()
#
#
# ll.removeKFromList(3)
# ll.printLL()
#
# test = [3, 1, 2, 3, 4, 5]
# def getLL(test):
#     ll2 = LinkedList()
#     for i in test:
#         ll2.insert(i)
#     return ll2
#
# ll2.removeKFromList(3)
# ll2.printLL()
#
# test = [3, 1, 2, 3, 4, 5]
# ll_test = getLL(test)
# ll_test.printLL()
#
# ll_test.getMiddle()
#
# ll_test.reverse()
# ll_test.printLL()
#
# test = [3, 1, 3, 4, 5]
# ll_test = getLL(test)
# ll_test.printLL()
# ll_test.getMiddle()
# #
# # # set i to point to middle of list using runner j
# # l = node1
# # i = j = l
# #
# # while j.next != None:
# #     j = j.next.next
# #     if j == None:
# #         break
# #     i = i.next
# #
# # print(i.value)
# # print(j.value)
48*47*46*45/(52*51*50*49)


import math

48*47*46*45/(math.factorial(52)/math.factorial(13)/math.factorial(39))*3


4*3*2/(52*51*50*49

import numpy as np
arr = [[3,1],[2,2]]
np.linalg.matrix_power(arr, 5)


arr = [[3**0.5, 1], [-1, 3**0.5]]
temp = np.linalg.matrix_power(arr,6)
np.matrix.trace(temp)

from scipy.integrate import quad
def integrand(x):
    return 1/(1+x**6)

ans, err = quad(integrand, -np.inf,np.inf)
ans/np.pi


(0.1**2 + 0.6**2 + 0.3**2)

11/48*(11/35)*(11/22)*4*3*2/2


(1/4+3/1+1/2)


(math.factorial(48)/math.factorial(35))/(math.factorial(52)/math.factorial(39))

((math.factorial(48)/math.factorial(12)/math.factorial(36))/(math.factorial(52)/math.factorial(39)/math.factorial(13)))*4


from scipy.special import comb
def prob(N, m, n, k):
    return comb(m, k)*comb((N-m),(n-k))/comb(N,n)

prob(52, 4, 13, 1)*prob(39,3,13,1)*prob(26,2,13,1)*prob(13,1,13,1)

prob(52,4, 13,0)**4

comb(4,0)