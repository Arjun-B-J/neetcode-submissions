# Time Complexity: O(N * C)
# Space Complexity: O(C)
# Approach: Bottom-Up Dynamic Programming (Space Optimized 1D Array - Items Backward)

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        dp = [0] * (capacity + 1)

        for i in range(N - 1, -1, -1):                              # Traverse items backwards
            # MUST traverse Left-to-Right.
            for c in range(weight[i], capacity + 1):
                
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

        return dp[capacity]