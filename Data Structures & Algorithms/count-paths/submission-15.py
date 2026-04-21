# Time Complexity: O(m * n) - We iterate through every cell in the m x n grid exactly once.
# Space Complexity: O(m * n) - We maintain a full 2D array to store the path counts for every cell.
# Approach: Bottom-Up Dynamic Programming (2D Tabulation)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]                        # Pre-fill grid with 1s (handles the top row & left col bases)
        
        for r in range(1, m):                                   # Start from row 1, col 1 since borders are pre-filled
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]          # Paths to current cell = Paths from ABOVE + Paths from LEFT
                
        return dp[m - 1][n - 1]                                 # The bottom-right cell holds the accumulated total paths