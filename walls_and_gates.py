from collections import deque
from typing import List

# You are given an m x n grid rooms initialized with these three possible values.
# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF. 

# Strategy: use BFS to ensure minimum distance. Start with the gate to improve efficiency.
# Increase the distance by 1 from current room to next room only if current room has a smaller distance
# This is to make sure min distance is kept if a room is reachable from multiple gates

# Recall: BFS = use deque and popleft
# Recall: BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1

def min_distance_to_gate(rooms: List[List[int]]) -> None:
    if not rooms or len(rooms) == 0:
        return rooms
    directions = {"up": (-1,0), "down": (1,0), "left": (0,-1), "right": (0,1)}
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:  # start with a gate
                queue = deque([(i,j)])
                while queue:
                    i, j = queue.popleft()
                    for _, step in directions.items():
                        m = i + step[0]
                        n = j + step[1]
                        # only search the eligible rooms
                        if 0 <= m < len(rooms) and 0 <= n < len(rooms[0]) and rooms[m][n] != -1 and rooms[i][j] < rooms[m][n]:
                            queue.append((m,n))
                            rooms[m][n] = rooms[i][j] + 1

test = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
(min_distance_to_gate(test))
print(test)  # [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


test1 = [[0,-1],[2147483647,2147483647]]
min_distance_to_gate(test1)
print(test1)  # [[0,-1],[1,2]]