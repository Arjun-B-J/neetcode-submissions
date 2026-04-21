# Time Complexity: O(N * C)
# Space Complexity: O(C) - We only store a single array of size capacity + 1.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 1D Array - Items Forward)

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        dp = [0] * (capacity + 1)

        for i in range(N):
            # MUST traverse Left-to-Right.
            # When we evaluate dp[c], dp[c - weight[i]] has ALREADY been updated for the current item, allowing reuse.
            for c in range(weight[i], capacity + 1):
                
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

        return dp[capacity]