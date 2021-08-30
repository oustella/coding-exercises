from myLinkedList import *

# class ListNode():
#     def __init__(self, x=""):
#         self.value = x
#         self.next = None

#     def get_value(self):
#         return self.value

#     def print(self):
#         temp = self
#         while temp and temp.next:  # don't print the last element to avoid the extra end "->"
#             print(temp.value, end="->")
#             temp = temp.next
#         print(temp.value)  # print the last element

#     # push a node to the end of the linked list
#     def push(self, val):
#         newnode = ListNode(val)
#         head = self
#         if not head:
#             head.next(newnode)
#         while head and head.next:
#             head = head.next
#         head.next(newnode)


def get_last(head):
    if not head or not head.next:
        return head
    return get_last(head.next)

# recursively reverse a list
def reverse(head):
    if not head or not head.next:
        return head
    r = reverse(head.next)
    l = get_last(r)
    head.next = None
    l.next = head
    return r


# assign kth element to be the new head and connect the left to the end
# e.g. input 1->2->3->4->5, k = 3, output 3->4->5->1->2
# strategy: have a fast pointer first go out by k steps
# and then the slow and fast pointer move together until the fast reaches the last element
# they will be k elements apart
def make_kth_head(head, k):
    if not head:
        return head
    
    fast = head
    slow = head
    i = 0
    while i < k:
        fast = fast.next
        # for when k is greater than the length of the linked list
        if not fast:
            return head
        i += 1
    # fast will be at 4

    while fast.next:
        slow = slow.next
        fast = fast.next
    # fast will be at 5, slow will be at 2

    temp = ListNode("d")  # just an anchor for where the new head is
    temp.next = slow.next
    slow.next = None
    fast.next = head
    return temp.next


ll = LinkedList()
for i in range(1,6):
    ll.push(i)
head = ll.getHead()    
head.print()

make_kth_head(head, 3).print()

# node1 = ListNode(1)
# node1.next = ListNode(2)
# node1.next.next = ListNode(3)
# node1.print()
# newhead = reverse(node1)
# newhead.print()
# make_kth_head(newhead, 2).print()
# time complexity O(N^2), because for each node, get_last goes to the end of the linked list
# space complexity O(N^2), because for each node, n calls of get_last() happpens