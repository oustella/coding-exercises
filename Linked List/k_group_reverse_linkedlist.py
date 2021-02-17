# Reverse the order of nodes within a group of k, and reconnect them
# Similar to pair_reverse_linkedlist except pair (k=2) becomes group (k=n)
# input 1->2->7->9->3, k = 3
# output 7->2->1->9->3

# Strategy
# Write a helper function to reverse k nodes
# See pair_reverse_linkedlist
# Note how to guarantee the remaining nodes still have k left during traversal

def k_reverse(head, k):
    # if the LL has less than k nodes, then `findKNodes` will return None
    if findKNodes(head, k) is None:
        return head
    
    cur = head
    prev = None
    # nex is the beginning of the next group
    nex = None
    # print(nex.value)

    # the traversal continues if we can find the beginning of a next subgroup (n=k)
    # at the end, cur becomes None 
    while cur:
        nex = findKNodes(cur, k).next
        subhead = helper(cur, k)
        # print(subhead.value)

        # link the new subhead to the previous
        if prev is None:
            head = subhead
        else:
            prev.next = subhead

        # connect the remaining nodes to the end of the reversed
        cur.next = nex
        # memorize cur (end of the reversed) to be previous
        prev, cur = cur, nex
    
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
    # within k nodes there are k links to reverse including the head to prev group
    while count < k:
        nex = cur.next
        cur.next = prev
        prev, cur = cur, nex
        count += 1
    # prev is the end node of the k group, i.e. the new head of the reversed
    return prev


if __name__ == "__main__":
    from myLinkedList import *
    def viewLL(head):
        while head.next:
            print(head.value, "->", end=" ")
            head = head.next
        print(head.value)

    # for k in range(1,8):
    #     print("k=", k)
    #     test = LinkedList()
    #     for i in [1,4,2,7,5,3,6]:
    #         test.push(i)
    #     new_head = k_reverse(test.head, k)
    #     viewLL(new_head)


    test = LinkedList()
    for i in [1,4,2,7,5,3,6]:
        test.push(i)
    viewLL(k_reverse(test.head,7))