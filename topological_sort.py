# A topological sort is an ordering of nodes for a directed acyclic graph (DAG) 
# such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

from collections import deque
from typing import List

def top_sort(n: int, graph: dict) -> List:
    sorted_nodes, visited = deque(), [False for _ in range(n)]
    for node in graph:
        if not visited[node]:
            dfs(node, sorted_nodes, visited, graph)
    return list(sorted_nodes)

def dfs(node, sorted_nodes, visited, graph):
    visited[node] = True
    if node in graph:
        for child in graph[node]:
            if not visited[child]:
                dfs(child, sorted_nodes, visited, graph)
    # if the node doesn't have any children, append to the beginning of the queue
    sorted_nodes.appendleft(node)

test = {0:[1,2], 1:[2,5], 2: [3], 5: [3,4], 6: [1,5]}
n = 7
print(top_sort(n, test))
                    