# Time Complexity: O(L * M * N) - Where L is len(strs). We evaluate each (index, zeros_left, ones_left) state at most once.
# Space Complexity: O(L * M * N) - Bounded by the recursion stack and the memoization dictionary.
# Approach: Top-Down Dynamic Programming (Recursion + Memoization)

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        # Pre-calculate counts: [(zeros, ones), (zeros, ones), ...]
        counts = [(s.count('0'), s.count('1')) for s in strs]

        def dfs(i, zeros_left, ones_left):
            if i == len(strs):                                  # Base case: No more strings to process
                return 0
            if (i, zeros_left, ones_left) in memo:              # Prune tree: Return cached result
                return memo[(i, zeros_left, ones_left)]

            # Choice 1: Skip the current string
            res = dfs(i + 1, zeros_left, ones_left)

            # Choice 2: Include the current string (if we have enough capacity)
            zeros, ones = counts[i]
            if zeros_left >= zeros and ones_left >= ones:
                res = max(res, 1 + dfs(i + 1, zeros_left - zeros, ones_left - ones))

            memo[(i, zeros_left, ones_left)] = res              # Cache the max strings we can form from this state
            return res

        return dfs(0, m, n)