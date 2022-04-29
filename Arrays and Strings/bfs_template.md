from collections import deque
# bfs for tree
def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in node.children:
            if OK(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND

# bfs for graph. Just need to keep track of the visited nodes.
def bfs(node):
    queue = deque([node])
    visited = set()
    level = 0
    while queue:
        n = len(queue)
        # use this for loop to keep track of levels
        for _ in range(n):
            cur = queue.popleft()
            if OK(cur):
                return FOUND(cur)
            if hasNeighbors(cur):
                for neighbor in getNeighbors(cur):
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        level += 1

## When to use BFS? 
- Get shortest distance
- When total number of nodes is unknown/infinite.

# DFS iterative approach.
The main difference is that DFS pops the newly added nodes first (stack) and BFS pops all existing nodes from a level before doing the next level (queue)

def dfs(graph: dict, startnode):
    if not graph:
        return
    stack, visited = [startnode], []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node in graph:
            children = graph[node]
            for child in children:
                if child not in visited:
                    stack.append(child)

## When to use DFS?
- Finding an exit in a maze. The answer node is far away from beginning.