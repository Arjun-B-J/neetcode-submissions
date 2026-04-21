# Time Complexity: O(N * M)
# Space Complexity: O(M) - We only store a single array of size capacity + 1.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 1D Array)

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        dp = [0] * (capacity + 1)

        for i in range(N):
            # MUST traverse right-to-left to avoid reusing the same item in the same iteration!
            # We stop at weight[i] - 1 because any capacity smaller than the item's weight can't hold it anyway.
            for c in range(capacity, weight[i] - 1, -1):
                
                # dp[c] acts as the 'skip' value (from previous iteration).
                # dp[c - weight[i]] is the value from the previous iteration at the remaining capacity.
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

        return dp[capacity]