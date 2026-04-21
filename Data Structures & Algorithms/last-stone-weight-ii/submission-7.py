# Time Complexity: O(N * S) - Where N is the number of stones and S is sum(stones) // 2. Each unique state (i, total) is computed at most once.
# Space Complexity: O(N * S) - Bounded by the recursion stack depth (N) and the memoization dictionary storing up to N * S states.
# Approach: Top-Down Dynamic Programming (0/1 Knapsack)

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneT = sum(stones)
        # We want to find a subset of stones that sums as close to stoneT // 2 as possible.
        # This minimizes the difference when the two subsets are "smashed" together.
        target = stoneT // 2 
        dp = {}
        
        def dfs(i, total):
            # Base Case 1: We have considered all stones.
            # Base Case 2: We reached or exceeded our ideal half-weight (target). 
            # Adding more weight will only pull us further from the optimal balance.
            if i == len(stones) or total >= target:
                # The weight of the other pile is (stoneT - total).
                # The smashed result is the absolute difference between the two piles.
                return abs(total - (stoneT - total)) 
                
            # Prune tree: If we have already calculated the min difference for this state, return it.
            if (i, total) in dp:
                return dp[(i, total)]
                
            # Recursive Step: We have two choices for the current stone:
            # Choice 1: Skip it (total remains the same)
            # Choice 2: Include it in our current subset (total + stones[i])
            # We want the choice that yields the minimum final difference.
            dp[(i, total)] = min(
                dfs(i + 1, total), 
                dfs(i + 1, total + stones[i])
            )
            
            return dp[(i, total)]

        # Start the DFS from the first stone (index 0) with an initial subset sum of 0
        return dfs(0, 0)