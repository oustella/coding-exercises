# OSL 02/12/2021

# Delete duplicative elements from a Linked List
# e.g., [1,2,2,4] -> [1,2,4]
# It's possible that the linked list elements are not sorted


class node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class linkedlist():
    def __init__(self) -> None:
        self.head = node("head")

    def add(self, node):
        """
        add a node to the end of the linked list
        """
        cur = self.head.next
        if not cur:
            self.head.next = node
        else:
            while cur.next:  # make sure the pointer stops at the last node
                cur = cur.next
            cur.next = node

    def print(self):
        cur = self.head.next
        if not cur:
            return 'Empty linked list!'
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

# S1 O(n) space complexity
# memorize what's already read
def removeDupes(ll):
    head = ll.head
    prev = head
    cur = head.next
    mem = []  
    while cur:
        if cur.value not in mem:
            mem.append(cur.value)
            prev, cur = cur, cur.next
        else:
            prev.next = cur.next
            cur = cur.next

# S2 O(1) space complexity
# Iterate through the ll
## for each node, check all the nodes down the line and remove those with the same value as the current node
def removeDupes2(ll):
    head = ll.head
    cur = head.next
    while cur:
        helper(cur, cur.next, cur.value)
        cur = cur.next

def helper(anchor, cur, val):
    while cur:
        if cur.value == val:
            anchor.next = cur.next
        anchor, cur = cur, cur.next




if __name__=="__main__":
    ll = linkedlist()
    for i in [2,3,5,7,4,5]:
        ll.add(node(i))
    removeDupes(ll)
    ll.print()

    # test out single element linked list
    ll = linkedlist()
    for i in [2]:
        ll.add(node(i))
    removeDupes(ll)
    ll.print()

    print('Sort and then dedup')
    ll = linkedlist()
    for i in [2,3,5,7,4,5]:
        ll.add(node(i))
    removeDupes2(ll)
    ll.print()

    ll = linkedlist()
    for i in [2]:
        ll.add(node(i))
    removeDupes2(ll)
    ll.print()