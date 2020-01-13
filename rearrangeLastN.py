# Given a singly linked list of integers l and a non-negative integer n,
# move the last n list nodes to the beginning of the linked list.
# Source: https://app.codesignal.com/interview-practice/task/5vcioHMkhGqkaQQYt/description

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l and n>0:
        save_orig_head = l
        # get length of the linked list
        length = 1
        while l.next:
            l = l.next
            length += 1
        save_end = l  # end node will be linked to the orig. head node
        # edge case
        if length == n:
            return save_orig_head
        # when the nth is not the end, find the n-1th node
        else:
            i=1
            l = save_orig_head
            while i < length-n and l:
                i += 1
                l = l.next
            save_new_head = l.next
            l.next = None  # break the link between n-1th and nth nodes
            save_end.next = save_orig_head
            return save_new_head
    # first, think of the cases when the orig. linked list is returned
    # 1. linked list is empty
    # 2. n = 0
    # 3. n = length of the linked list -> have to get the length
    else:
        return l
