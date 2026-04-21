class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        dp = [[0]* (M+1) for _ in range(N+1)]

        # Do DP , Find the best for each cell, if included , current c - weight check in row - 1 to see the best possible with that included, and row-1 skip , take max of that , we get max for each cell
        for i in reversed(range(N)):
            for j in range(M+1):
                # Skip 
                skip = dp[i+1][j]

                #include
                include = 0
                if j - weight[i]>=0:
                    include = profit[i] + dp[i+1][j-weight[i]]
                dp[i][j] = max(skip,include)
        return dp[0][M]