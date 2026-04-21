# Time Complexity: O(N) - Where N is the number of travel days (len(days)). 
#                         There are N unique states. For each state, the while loop advances 'j' 
#                         at most 30 times (the maximum pass duration), which is an O(1) operation.
# Space Complexity: O(N) - Bounded by the recursion stack depth and the memoization dictionary.
# Approach: Top-Down Dynamic Programming (Recursion + Memoization)

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        # 'index' represents the current index in the 'days' array we are evaluating
        def dfs(index: int) -> float:
            if index == len(days):                              # Base case: We have covered all travel days
                return 0
            if index in memo:                                   # Prune tree: Return cached minimum cost for this index
                return memo[index]

            memo[index] = float("inf")                          # Initialize to infinity before finding the minimum
            
            # Zip pairs the pass durations with their respective costs: (1, costs[0]), (7, costs[1]), (30, costs[2])
            for duration, cost in zip([1, 7, 30], costs):
                j = index
                
                # Fast-forward 'j' to find the index of the NEXT travel day that is NOT covered by this pass
                while j < len(days) and days[j] < days[index] + duration:
                    j += 1
                
                # Calculate cost: Price of current pass + optimal cost for the remaining uncovered days
                memo[index] = min(memo[index], cost + dfs(j))

            return memo[index]

        # Start the DFS from the first travel day (index 0)
        return dfs(0)