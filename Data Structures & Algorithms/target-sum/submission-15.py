# Time Complexity: O(N * S) - Where N is the number of elements and S is the total sum. It dynamically prunes unreachable sums at each step.
# Space Complexity: O(N * S) - We store a dictionary of reachable sums for EVERY index from 0 to N. 
# Approach: Bottom-Up Dynamic Programming (2D Tabulation with Hash Maps)

from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # dp[i] is a dictionary where keys are the achievable sums using the first 'i' items, 
        # and values are the number of ways to achieve that sum.
        dp = [defaultdict(int) for _ in range(n + 1)]
        
        # Base case: 1 way to reach a sum of 0 using 0 items
        dp[0][0] = 1

        for i in range(n):
            # Iterate only through the sums we successfully reached in the previous step
            for current_sum, count in dp[i].items():
                
                # Choice 1: Add the current number
                dp[i + 1][current_sum + nums[i]] += count
                
                # Choice 2: Subtract the current number
                dp[i + 1][current_sum - nums[i]] += count

        # Return the accumulated ways to reach the target sum using all 'n' items.
        # If the target was never reached, defaultdict safely returns 0.
        return dp[n][target]