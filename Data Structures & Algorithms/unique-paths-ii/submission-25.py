# Time Complexity: O(m * n) - Processing all rows and columns.
# Space Complexity: O(n) - We only hold two arrays (current and previous row) of size n.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 2-Row Array)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * n
        prev_row[0] = 1                                                 # Virtual seed for the start
        
        for r in range(m):
            curr_row = [0] * n
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0                                     # Obstacle blocks the path
                else:
                    if c > 0: 
                        curr_row[c] = curr_row[c - 1] + prev_row[c]     # LEFT + ABOVE
                    else: 
                        curr_row[c] = prev_row[c]                       # Leftmost boundary only inherits from ABOVE
            prev_row = curr_row                                         # Shift window down
            
        return prev_row[-1]