# Time Complexity: O(N * C) - Where N is len(profit) and C is capacity.
# Space Complexity: O(N * C) - Bounded by the recursion stack and memo dictionary.
# Approach: Top-Down Dynamic Programming (Recursion + Memoization)

from typing import List

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        N = len(profit)

        def dfs(i, c):
            if i == N or c == 0:                                    # Base case: out of items or out of capacity
                return 0
            if (i, c) in memo:                                      # Prune tree: return cached result
                return memo[(i, c)]

            skip = dfs(i + 1, c)                                    # Move to the next item
            
            include = 0
            if c >= weight[i]:
                # We stay on item 'i' to allow infinite reuses
                include = profit[i] + dfs(i, c - weight[i])         

            memo[(i, c)] = max(skip, include)
            return memo[(i, c)]

        return dfs(0, capacity)