# Given a linked list l, reverse its nodes k at a time and return the modified list.
# k is a positive integer that is less than or equal to the length of l.
# If the number of nodes in the linked list is not a multiple of k,
# then the nodes that are left out at the end should remain as-is.
# You may not alter the values in the nodes - only the nodes themselves can be changed.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None


# a helper reverse function that reverse k nodes at a time
def reverseK(current, k):
    prev = None
    new_tail = current  # the starting point becomes the new tail that needs to be memorized
    count = 0
    while count < k and current:  # loop stops when count hits k times, or when there are no more nodes to reverse
        nextn = current.next
        current.next = prev
        prev = current
        current = nextn
        count += 1
    new_head = prev

    return new_head, new_tail, current, count  # current is the starting point of the next reversal


def reverseNodesInKGroups(l, k):
    # do the reversal once to find out the first new head
    current = l
    new_head, new_tail, current, count = reverseK(current, k)
    first_head = new_head  # memorizes the first head

    while current:
        prev_tail = new_tail  # memorizes the previous tail that will link to the new head from the next reversal
        new_head, new_tail, current, count = reverseK(current, k)
        if count < k:  # True would mean that the remaining nodes are fewer than k
            new_head, new_tail, current, count = reverseK(new_head, k)  # reverse them back
            prev_tail.next = new_head
        else:
            prev_tail.next = new_head

    return first_head







