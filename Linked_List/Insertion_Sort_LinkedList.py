from myLinkedList import *

def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode("d")  # p points to where last moved element is, dummy points to head
        cur = dummy.next = head 
        
        while cur and cur.next:  # stop cur point at the last element
            target = cur.next
            target_val = target.value  # save next_val to compare with p
            if cur.value <= target_val: 
                cur = cur.next
                continue  # use continue to advance to next element if cur val is smaller than next val
            
            if p.next.value > target_val:  # if the last moved element is bigger than the next val
                p = dummy  # start the comparison from the beginning
                
            while p.next.value <= target_val:  # move p to point to where next_val should be inserted after
                p = p.next
                
            cur.next = target.next  # point cur to skip the element to be moved
            target.next = p.next  # the moved element points is inserted in front of where it needs to be
            p.next = target  # connects the prev node to the inserted node. [1]
        
        return dummy.next # dummy is always at the beginning

# [1] This has the added benefit of p now pointing to the moved element 
# so if the next element is greater than p.next
# no need to search from the beginning