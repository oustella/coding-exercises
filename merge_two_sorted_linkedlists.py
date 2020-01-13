# Given two sorted linked lists, combine them in a non-decreasing (<=) order
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# This solution works but ran longer than O(l1.length + l2.length)
# Because the push method traverses from the head every time a new node is added to the end.
# def push(head, value):
#     new = ListNode(value)
#     current = head
#     if head:
#         while current.next:
#             current = current.next
#         current.next = new
#         # head = head.next
#     else:
#         head = new
#     return head
#
#
# def mergeTwoLinkedLists(l1, l2):
#     head = None
#     while l1 and l2:
#         if l1.value <= l2.value:
#             head = push(head, l1.value)
#             l1 = l1.next
#         else:
#             head = push(head, l2.value)
#             l2 = l2.next
#     if l1:
#         while l1:
#             head = push(head, l1.value)
#             l1 = l1.next
#     if l2:
#         while l2:
#             head = push(head, l2.value)
#             l2 = l2.next
#     return head


# Tweaked solution that meets O(l1.length + l2.length)
def push(head, tail, newnode):  # keeps track of both the head and the tail
    if head:
        tail.next = newnode  # new node is pushed to the tailend of the linked list
        tail = tail.next  # the new node becomes the new tail
    else:  # dealing with an empty linked list
        head = newnode
        tail = newnode
    return head, tail


def mergeTwoLinkedLists(l1, l2):
    head = None
    tail = None
    while l1 and l2:
        if l1.value <= l2.value:
            head, tail = push(head, tail, l1)  # pushes the smaller node to the end of the linked list
            l1 = l1.next
        else:
            head, tail = push(head, tail, l2)
            l2 = l2.next
    while l1:  # if l1 is left, that means all of the remaining ones are bigger than the new linkedlist
        head, tail = push(head, tail, l1)
        l1 = l1.next
    while l2:  # same as above
        head, tail = push(head, tail, l2)
        l2 = l2.next
    return head


# Solution by codesignal user flanagan1
def mergeTwoLinkedLists(l1, l2):
    head = ListNode(None)  # initiate a head node
    current = head  # current is a pointer
    while l1 and l2:
        if l1.value <= l2.value:
            current.next = l1  # the first iteration has the first value linked to head
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next  # move the pointer along. The pointer always points to the last node of the linkedlist

    if l1:
        current.next = l1  # the rest of the l1 can just be added by linking to the head of the remaining l1
    elif l2:
        current.next = l2

    return head.next  # since head is an empty node
