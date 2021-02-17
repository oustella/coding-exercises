from myLinkedList import *

# Reverse nodes in a linked list in pairs.
# e.g. 1->2->7->9->3 becomes 2->1->9->7->3

# strategies: 
# 1. Traverse down the list two steps at a time
# 2. have a helper function that reverses pairs inside the loop
# 3. Memorizes the next pair to be connected
# 4. Need to make sure the single dangling node at the end is included for edd LL
# 5. Edge cases: empty LL, or one-node LL

def solution(head):
    # memorizes the new head to return
    if head.next is None or head is None:
        return head
    new_head = head.next
    left = head
    while left and left.next:
        nex = left.next.next
        reverseAPair(left)
        left.next = nex
        left = left.next


def reverseAPair(head):
    left = head
    right = head.next
    right.next = left
    # return right
