# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# Approach: Bottom-Up Dynamic Programming (2D Tabulation - Items Left to Right)

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(N + 1)]       # Padding top row with 0s for base case

        for i in range(1,N+1):                                      # i maps to the current item -1 index
            for c in range(capacity + 1):                       # c maps to the current capacity column
                
                skip = dp[i-1][c]                                 # Value from the row ABOVE (not including item i)
                
                include = 0
                if c >= weight[i-1]:
                    include = profit[i-1] + dp[i-1][c - weight[i-1]]  # Profit + best value from ABOVE at remaining capacity
                
                dp[i][c] = max(skip, include)               # Store in current row

        return dp[N][capacity]