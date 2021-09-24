# You have a graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and a list of edges 
# where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# An undirected graph is tree if it has following properties. 
# 1) There is no cycle. 
# 2) The graph is connected.

from typing import List
from collections import defaultdict

def is_valid_tree(n: int, edges: List[List[int]]) -> bool:
    adj_list = defaultdict(list)
    # we choose to populate only half of the adjacency matrix for efficiency
    for ni, nj in edges:
        adj_list[ni].append(nj)
    # Use dfs
    stack = [0]
    visited = [False for _ in range(n)]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            if node in adj_list:
                for child in adj_list[node]:
                    # a cycle exists if a child has been a parent or another node's child
                    # it would have been visited
                    if visited[child]:
                        return False
                    stack.append(child)
    # last, check for unreachable nodes. All nodes should have been visited in a tree after dfs
    return all(visited)

edges = [[0,1],[0,2],[0,3],[1,4]]
is_valid_tree(5, edges)
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
is_valid_tree(5, edges)