from collections import deque
from typing import List

# Solution 2 for optimal time and space

class Solution:
    # Solution 1
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()
        mins = -1
        queue = deque()
        
        # first get all the rotten oranges at time 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2 and (i,j) not in visited:            
                    queue.append((i,j))
        
        # bfs
        while queue:
            lvl = len(queue)
            mins += 1
            # print(mins, grid)
            for _ in range(lvl):
                i, j = queue.popleft()
                if grid[i][j] == 2 and (i,j) not in visited:
                    visited.add((i,j))
                    if i+1 < nrows and grid[i+1][j]==1:
                        grid[i+1][j] = 2
                        queue.append((i+1,j))
                    if i-1 >=0 and grid[i-1][j]==1:
                        grid[i-1][j] = 2
                        queue.append((i-1,j))
                    if j+1 < ncols and grid[i][j+1]==1:
                        grid[i][j+1] = 2
                        queue.append((i,j+1))
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        queue.append((i,j-1))
        
        # if there are still fresh oranges left return -1
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1:
                    return -1
        
        # if mins did not pass at all return 0 
        return 0 if mins==-1 else mins
                    
# Solution 1a - condensed code
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        nrow = len(grid)
        ncol = len(grid[0])
        count = -1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque([])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 0:
                    visited[i][j] = True
                else:
                    continue
        if all(all(i) for i in visited):
            return 0
        
        while queue:
            count += 1
            for _ in range(len(queue)):    
                rotten = queue.popleft()
                visited[rotten[0]][rotten[1]] = True
                for direction in directions:
                    m = rotten[0] + direction[0]
                    n = rotten[1] + direction[1]
                    if 0 <= m < nrow and 0 <= n < ncol and not visited[m][n] and grid[m][n] == 1:
                        grid[m][n] = 2
                        queue.append([m,n])

        return count if all(all(i) for i in visited) else -1

    # Solution 2 - no extra space required, marking the oranges as rotten already served the purpose of marking visited.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        nrow = len(grid)
        ncol = len(grid[0])
        count = -1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque([])
        # First find all rotten oranges at time 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    queue.append([i,j])

        while queue:
            count += 1  # all pre-existing rotten oranges are counted as time 0
            for _ in range(len(queue)):  # this makes sure all nodes on the same level are used at the same time point
                rotten = queue.popleft()
                for direction in directions:
                    m = rotten[0] + direction[0]
                    n = rotten[1] + direction[1]
                    # if an orange is fresh it means it hasn't been touched before
                    if 0 <= m < nrow and 0 <= n < ncol and grid[m][n] == 1:
                        # mark it as rotten and append to the next time point
                        grid[m][n] = 2
                        queue.append([m,n])

        # if there is a fresh orange left after bfs, returns -1
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    return -1
        # if no fresh oranges left and there are 2 in the grid, it implies all fresh oranges have been rotten
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    return count
        # if the entire grid is filled with 0 after having checked for 1 and 2, it means the grid starts with all 0s
        # meaning no fresh oranges at time 0
        return 0