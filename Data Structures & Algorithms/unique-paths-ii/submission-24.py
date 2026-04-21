# Time Complexity: O(m * n) - Iterating through every cell exactly once.
# Space Complexity: O(m * n) - Maintaining the full 2D grid of path counts.
# Approach: Bottom-Up Dynamic Programming (2D Tabulation)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]                                # Initialize grid with 0s
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0                                        # Obstacle wipes out paths here
                elif r == 0 and c == 0:
                    dp[r][c] = 1                                        # Seed the starting position
                else:
                    if r > 0: dp[r][c] += dp[r - 1][c]                  # Add paths coming from ABOVE
                    if c > 0: dp[r][c] += dp[r][c - 1]                  # Add paths coming from LEFT
                    
        return dp[m - 1][n - 1]