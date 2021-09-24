# You have a graph of n nodes labeled from 0 to n - 1.
# You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that 
# there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.

from collections import deque
from collections import defaultdict
from typing import List
def num_connected_components(n: int, graph: List[List[int]]) -> int:
    count = 0
    if not graph:
        return count
    # convert graph to adjancy list
    # because we are interested in all connected nodes,
    # we can assume the edges are directed so the same node doesn't need to be visited twice
    adj = defaultdict(list)
    for ni, nj in graph:
        adj[ni].append(nj)
    # use dfs to visit all connected nodes while ticking off the visited ones
    def dfs(node, visited):
        visited[node] = True
        if node in adj:
            for child in adj[node]:
                dfs(child, visited)
    # begin with all nodes being unvisited
    visited = [False for _ in range(n)]
    for node in range(n):
        # this is the key to the solution
        # recognizing that the condition to increase count is when a new dfs is needed
        # ie who hasn't been visited after a round of dfs
        if not visited[node]:
            count += 1
            dfs(node, visited)
    return count

edges = [[0,1],[0,2],[1,2],[3,4]]
num_connected_components(5, edges)

edges = [[0,1],[1,2],[2,3],[3,4]]
num_connected_components(5, edges)