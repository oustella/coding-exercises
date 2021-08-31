# https://leetcode.com/problems/the-skyline-problem/
# Solution source: CodePath.org

# [1] only add to the skyline, if the height has not been seen before. Addressing the 'note' scenario in the question
# [2] put all contending positions in a sorted, unique set. Both the left and right edges of a building are qualified.
# Sorting makes sure we look at the positions from left to right. Otherwise, the below logic doesn't stand.
# Think of the algorithm to draw a vertical line across the landscape at each contending position
# and scan from left to right
# [3] add buildings whose left edge is to the left or on the contending position to a max heap
# use -height to convert the default minHeap to a maxHeap
# [4] remove buildings whose right edge is to the left or on the contending position from the heap
# note the order of removal is from the tallest
# [5] height at the current contending position is the highest seen so far
# Works in tandem with addSky() which further filters repeating highest positions
# If nothing standing in the horizon then the height is 0

import heapq
from types import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = [[-1,0]]
        def addSky(pos, height):
            if ans[-1][1] != height:  #[1]
                ans.append([pos, height])
                
        edges = sorted(set([b[0] for b in buildings] + [b[1] for b in buildings]))  #[2]
        b = 0
        live = []
        for edge in edges:
            while b < len(buildings) and buildings[b][0] <= edge:  #[3]
                heapq.heappush(live, [-buildings[b][2], buildings[b][1]])
                b += 1
            while live and live[0][1] <= edge:  #[4]
                heapq.heappop(live)
            # print(edge, live)     
                        
            height = -live[0][0] if live else 0  #[5]
            addSky(edge, height)
            
        return ans[1:]