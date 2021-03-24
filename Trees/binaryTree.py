class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# depth first traversal: in-order, pre-order, post-order.
# Time complexity is linear O(n), where n is number of nodes.
# in-order: left, root, right. Left->right
# good for flattening trees or printing
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)

# pre-order: root, left, right. Pre means the previous level, the root first.
# good for copying trees
def printPreOrder(root):
    if root:
        print(root.val, end=" ")
        printPreOrder(root.left)
        printPreOrder(root.right)

# post-order: left, right, root. Post means the next level, the children first. 
# good for deletion from root (exploring children node before root)
def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val, end=" ")

# Breath first traversal: level-order
# Level-order: traverse in layers from left to right
# good for visiting roots first
from collections import deque
def printLevelOrder(root):
    if root is None:
        return
    queue = deque([root])
    while len(queue) > 0:
        # pop the first element from the queue
        root = queue.popleft()
        print(root.val, end=" ")
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
 

    

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left= Node(4)
    root.left.right = Node(5)

    print("in-order")
    printInOrder(root)
    print()
    print("pre-order") 
    printPreOrder(root)
    print()
    print("post-order")
    printPostOrder(root)
    print()
    print("level-order")
    printLevelOrder(root)
    print()
