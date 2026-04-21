# Time Complexity: O(R * C) - Each cell in the grid is processed and added to the queue at most once.
# Space Complexity: O(R * C) - The queue can scale up to hold all cells in the worst-case scenario.
# Approach: Multi-Source Breadth-First Search (BFS)

from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]         # Orthogonal offsets for neighbor traversal
        INF = 2**31 - 1                                         # Standard representation of unvisited empty rooms
        ROW, COL = len(grid), len(grid[0])
        q = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:                             # Identify all treasure chests (BFS sources)
                    q.append((i, j))                            # Enqueue sources for simultaneous level-order expansion
        
        distance = 1                                            # Tracks radius radiating outward from all treasures
        while q:
            for _ in range(len(q)):                             # Process the entire current BFS level snapshot
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or grid[nr][nc] != INF:
                        continue                                # Prune out-of-bounds, obstacles, or already visited rooms
                    
                    grid[nr][nc] = distance                     # Mutate grid in-place with the shortest distance found
                    q.append((nr, nc))                          # Queue valid neighbor for the next depth level
                    
            distance += 1                                       # Increment radius after the current level is exhausted