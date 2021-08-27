from myLinkedList import *

############################################
# Reverse nodes in a linked list in pairs.
# e.g. 1->2->7->9->3 becomes 2->1->9->7->3
############################################

# strategies: 
# 1. Traverse down the list two steps at a time
# 2. have a helper function that reverses pairs inside the loop
# 3. Link the tail of the reversed pair to the original head of the new pair
# 3a. Remember the tail of the reversed pair before progressing it to the head of the next pair
# 4. Need to make sure the single dangling node at the end is included for edd LL
# 5. Edge cases: empty LL, or one-node LL

def solution(head):
    # edge cases
    if head.next is None or head is None:
        return head

    prev = None
    left = head
    while left and left.next:
        nex = left.next.next
        # print('nex is', nex.value)
        subhead = reverseAPair(left)
        # print(subhead.value, "->", subhead.next.value)
        # the first prev is the new head
        if prev is None:
            head = subhead
        # link prev to the subhead of the reversed pair
        else:
            prev.next = subhead

        # connect the tail of the reversed pair to the remaining ll
        # although it seems unecessary, it actually does the job of connecting it to the daggling single node at the end
        left.next = nex
        # memorize the tail of the reversed pair to be 'prev' and then progress it to the next pair
        prev, left = left, nex

        # print('left is', left.value)
    return head


def reverseAPair(head):
    left = head
    right = head.next
    right.next = left
    left.next = None
    return right


def viewLL(head):
    while head.next:
        print(head.value, "->", end=" ")
        head = head.next
    print(head.value)


if __name__ == "__main__":
    test = LinkedList()
    for i in [1,4,2,7,5,3,6]:
        test.push(i)
    test.printLL()
    new_head = solution(test.head)
    viewLL(new_head)

