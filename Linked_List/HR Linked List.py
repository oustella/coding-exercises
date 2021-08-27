# https://www.hackerrank.com/challenges/30-linked-list/problem
# solution by HackerRank user kkutt


class Node:  # a linked node has two components
    def __init__(self, data):
        self.data = data  # value
        self.next = None  # pointer to the next value


class Solution:
    def display(self, head):  # to print out the linked list, you just need to know the head
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next  # use the pointer to find the next stored node

    def insert(self, head, data):
        linked_node = Node(data)
        if head:  # if there is a head node
            current = head  # start with the head node
            while current.next:  # traverse through the linked nodes
                current = current.next
            current.next = linked_node  # when reaching the end of the linked list, add the new node
            return head
        else:
            return linked_node  # if currently no head node, return the first node added


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)