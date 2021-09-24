from collections import deque
def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in node.children:
            if OK(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND