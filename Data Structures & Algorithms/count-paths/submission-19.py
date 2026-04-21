# Time Complexity: O(m * n) - We iterate through every cell in the m x n grid exactly once.
# Space Complexity: O(m * n) - We maintain a full 2D array to store the path counts.
# Approach: Bottom-Up Dynamic Programming (2D Tabulation - Backwards Traversal)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]                        # Pre-fill grid with 1s (handles bottom row & right col bases)
        
        for r in range(m - 2, -1, -1):                          # Start from second-to-last row, moving UP
            for c in range(n - 2, -1, -1):                      # Start from second-to-last column, moving LEFT
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]          # Paths to destination = move DOWN + move RIGHT
                
        return dp[0][0]                                         # The top-left cell now holds the total paths from the start