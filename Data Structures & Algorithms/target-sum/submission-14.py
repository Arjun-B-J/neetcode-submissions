# Time Complexity: O(N * S) - Where N is len(nums) and S is the sum of all elements. We compute each (index, current_sum) state at most once.
# Space Complexity: O(N * S) - Bounded by the recursion stack depth and the memo dictionary.
# Approach: Top-Down Dynamic Programming (Recursion + Memoization)

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        N = len(nums)

        def dfs(index: int, current_sum: int) -> int:
            if index == N:                                          # Base Case: Out of numbers to pick
                return 1 if current_sum == target else 0            # 1 valid way if we hit the target, 0 otherwise
                
            state = (index, current_sum)
            if state in memo:                                       # Prune tree: Return cached ways for this exact state
                return memo[state]
            
            # Choice 1: Add the current number
            add = dfs(index + 1, current_sum + nums[index])
            
            # Choice 2: Subtract the current number
            subtract = dfs(index + 1, current_sum - nums[index])
            
            memo[state] = add + subtract                            # Cache the total ways from both choices
            return memo[state]
            
        return dfs(0, 0)