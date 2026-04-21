# Time Complexity: O(R * C) - Each cell is processed by the Pacific and Atlantic BFS queues at most once.
# Space Complexity: O(R * C) - The queues and visited sets can scale up to hold all cells in the worst-case scenario.
# Approach: Multi-Source BFS (Reverse Flow / Flowing Uphill from Oceans)

from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        atlantic, pacific = set(), set()                  # Tracks cells that can flow to the respective oceans
        qP, qA = deque(), deque()
        ROW, COL = len(heights), len(heights[0])
        
        for i in range(ROW):                              # Seed the vertical coastlines
            pacific.add((i, 0)); qP.append((i, 0))        # Left edge touches the Pacific
            atlantic.add((i, COL - 1)); qA.append((i, COL - 1)) # Right edge touches the Atlantic
            
        for i in range(COL):                              # Seed the horizontal coastlines
            pacific.add((0, i)); qP.append((0, i))        # Top edge touches the Pacific
            atlantic.add((ROW - 1, i)); qA.append((ROW - 1, i)) # Bottom edge touches the Atlantic
        
        def bfs(queue, visited_set):                      # Helper function to prevent repeating the BFS logic
            while queue: 
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Crucial logic: Since we start at the oceans, we must flow UP to higher or equal elevations
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in visited_set or heights[nr][nc] < heights[r][c]:
                        continue
                        
                    visited_set.add((nr, nc))             # Mark the inland cell as able to reach this specific ocean
                    queue.append((nr, nc))

        bfs(qP, pacific)                                  # Flow uphill from the Pacific coastline
        bfs(qA, atlantic)                                 # Flow uphill from the Atlantic coastline
        
        # Return coordinates that exist in BOTH sets, formatted as a list of lists
        return [[r, c] for r, c in pacific.intersection(atlantic)]