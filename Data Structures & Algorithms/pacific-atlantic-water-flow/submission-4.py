# Time Complexity: O(R * C) - In the worst case, each cell is processed once by the Pacific DFS and once by the Atlantic DFS.
# Space Complexity: O(R * C) - Space is used by the visited sets and the recursion stack (if the grid is a single long path).
# Approach: Multi-Source Depth-First Search (Reverse Flow / Flowing Uphill)

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific, atlantic = set(), set()                          # Tracks cells that can flow to respective oceans
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]           # Orthogonal offsets for traversal

        def dfs(r, c, visited_set, prev_height):                  
            # Base case: halt if out of bounds, already visited, or strictly lower than the previous cell
            if r < 0 or r == ROW or c < 0 or c == COL or (r, c) in visited_set or heights[r][c] < prev_height:
                return                                            
            
            visited_set.add((r, c))                               # Mark cell as reachable from the target ocean
            
            for dr, dc in directions:                             # Recursively flow "uphill" to all 4 neighbors
                dfs(r + dr, c + dc, visited_set, heights[r][c])

        for c in range(COL):                                      # Seed DFS from top/bottom horizontal coastlines
            dfs(0, c, pacific, heights[0][c])                     # Top edge flows up from the Pacific
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])        # Bottom edge flows up from the Atlantic

        for r in range(ROW):                                      # Seed DFS from left/right vertical coastlines
            dfs(r, 0, pacific, heights[r][0])                     # Left edge flows up from the Pacific
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])        # Right edge flows up from the Atlantic

        # Return coordinates that exist in BOTH sets, formatted as a list of lists
        return [[r, c] for r, c in pacific.intersection(atlantic)]