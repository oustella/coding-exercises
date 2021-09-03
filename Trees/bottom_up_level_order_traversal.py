# https://leetcode.com/problems/binary-tree-level-order-traversal/
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from collections import deque

def levelOrder(root):
    if not root:
        return []
    queue = deque([[root]])  # root needs to be in a list for nodesInLevel
    res = []
    while len(queue) > 0:
        nodesInLevel = queue.popleft()
        res.append([node.val for node in nodesInLevel])
        nextLevel = []
        for node in nodesInLevel:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        if len(nextLevel) > 0:
            queue.append(nextLevel)
    return res
    # return res[::-1] to return bottom-up level order traversal

# Note deque([root]) is the same as deque(root) 
# It would put root as the first element of the deque.
# ie. the first set of brackets doesn't do anything.

#########################################
# another way to keep track of the levels
#########################################
def levelOrder(root):
    if not root:
        return []
    queue = deque([root])
    res = []
    while len(queue) > 0:
        n = len(queue)
        thisLevel = []
        for _ in range(n):
            node = queue.popleft()
            thisLevel.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        res.append(thisLevel)
    return res
    # return res[::-1] to return bottom-up level order traversal