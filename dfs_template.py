# iterative approach
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