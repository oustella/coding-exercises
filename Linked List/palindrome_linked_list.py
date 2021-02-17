from myLinkedList import *

def isPalindrome(head: ListNode) -> bool:
# find the middle and reverse the first half
# mid node is (n//2 + 1) th node

    fp = head
    sp = head

    while fp and fp.next:
        fp = fp.next.next
        sp = sp.next
    mid = sp
    print('mid node', mid.value)
    # the head of the reversed left array is the node one before the mid node
    l_head = reverseLL(head, mid)
    print('new left head', l_head.value)

    # for even length ll, the new head of the right ll is the mid node
    # for odd length ll, the new head of the right ll starts one after the mid node
    if fp:  # odd length ll
        print('odd ll')
        r_head = mid.next
    else: # even length ll
        print('even ll')
        r_head = mid
    # print('new right head', r_head.value)  # cannot check r_head value if there is only one element in the linkedlist

    while l_head and r_head:
        if l_head.value != r_head.value:
            return False
        l_head = l_head.next
        r_head = r_head.next
        
    return True

def reverseLL(head, tail):
    # only reverse up to the node before tail
    if head == tail:
        return head
    else:
        prev = None
        cur = head
        next = None
        while cur != tail:
            next = cur.next
            # reverse the link
            cur.next = prev
            prev, cur = cur, next
        return prev


if __name__=="__main__":
    test = LinkedList()
    for i in [1,4,2,4,1]:
        test.push(i)
    test.printLL()
    isPalindrome(test.getHead())

    test = LinkedList()
    for i in [1,1]:
        test.push(i)
    test.printLL()
    isPalindrome(test.getHead())

    test = LinkedList()
    for i in [1,4,2,4]:
        test.push(i)
    test.printLL()
    isPalindrome(test.getHead())

    test = LinkedList()
    for i in [1]:
        test.push(i)
    test.printLL()
    isPalindrome(test.getHead())



