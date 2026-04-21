# Time Complexity: O(N * C)
# Space Complexity: O(N * C)
# Approach: Bottom-Up Dynamic Programming (2D Tabulation - Items Left to Right)

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(N + 1)]           # Padding top row with 0s

        for i in range(N):
            for c in range(capacity + 1):
                skip = dp[i][c]                                     # Value from the row ABOVE
                
                include = 0
                if c >= weight[i]:
                    # Value from the CURRENT row being built
                    include = profit[i] + dp[i + 1][c - weight[i]]  
                    
                dp[i + 1][c] = max(skip, include)

        return dp[N][capacity]