# Reverse the order of nodes within a group of k, and reconnect them
# Similar to pair_reverse_linkedlist except pair (k=2) becomes group (k=n)
# input 1->2->7->9->3, k = 3
# output 7->2->1->9->3
# step 1, cur = 1, find subhead = 7, nexseg = 9, and the subseg becomes 7->2->1
# step 2, connects cur to the remaining list, the 7->2->1->9->3
# step 3, advance prev to 1, and cur to 9
# step 4, detects that the remaing elements are fewer than k by nexseg becomes none
# therefore, don't do the reverse and subhead = cur = 9
# step 5, connects prev to subhead
# step 6, cur becomes None, end the while loop

# Strategy
# use pointers to keep track of: 
# 1. reversed new head, 
# 2. old head becomes the new tail, 
# 3. and the head of the next segment

def k_reverse(head, k):
    # if the LL has less than k nodes, then `findKNodes` will return None
    if findKNodes(head, k) is None:
        return head
    
    cur = head
    prev = None

    # the traversal continues if we can find the beginning of a next subgroup (n=k)
    # when remaining segment has fewer than k elements, cur becomes None 
    while cur:
        # print(cur.value)
        # subhead is the new head of the reversed subsegment
        # nexseg is the head of the remaining segment
        subhead, nexseg = helper(cur, k)
        
        # link the new subhead to the previous
        if prev is None:
            head = subhead
        else:
            prev.next = subhead

        # connect the remaining nodes to the end of the reversed
        # here cur is still pointing to the original first element of the subsegment, 
        # which becomes the end of the newly reversed subsegment
        if nexseg:
            cur.next = nexseg
        
        # advance prev to end of the newly reversed subsegment
        # advance cur to the beginning of the new segment
        prev, cur = cur, nexseg
    
    return head

# return the last node within the k group
def findKNodes(head, k):
    cur = head
    # use starting point of count to control whether to return the last node or the beginning of the next group
    count = 1
    # if the remaining nodes are less than k, then cur will stop at the last node
    while cur.next and count<k:
        cur = cur.next
        count += 1
    return cur

# reverse k nodes and return the new head
def helper(head, k):
    cur = head
    nex = None
    prev = None
    count = 0
    nexseg = findKNodes(cur, k).next
    # within k nodes there are k links to reverse including the head to prev group
    if nexseg:
        while count < k:
            nex = cur.next
            cur.next = prev
            prev, cur = cur, nex
            count += 1
        # prev is the end node of the k group, i.e. the new head of the reversed
        return prev, nexseg
    else:
        return cur, nexseg



from myLinkedList import *
def viewLL(head):
    while head.next:
        print(head.value, "->", end=" ")
        head = head.next
    print(head.value)


test = LinkedList()
for i in [1,4,2,7,5,3,6]:
    test.push(i)
viewLL(k_reverse(test.getHead(),3))



