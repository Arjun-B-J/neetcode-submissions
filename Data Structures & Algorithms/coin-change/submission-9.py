class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # State: (index, current_amount)
        # We don't track 'count' in the key.
        memo = {}

        def dfs(i, current_sum):
            # Base Case 1: Success (0 coins needed to finish)
            if current_sum == amount:
                return 0
            
            # Base Case 2: Failure (Impossible to finish)
            if current_sum > amount or i == len(coins):
                return float('inf')
            
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            
            # OPTION 1: SKIP coin 'i'
            # We don't add 1 because we didn't take a coin
            skip = dfs(i + 1, current_sum)
            
            # OPTION 2: INCLUDE coin 'i'
            # We add 1 to the result because we took one coin
            include = 1 + dfs(i, current_sum + coins[i])
            
            # Store the minimum of the two choices
            memo[(i, current_sum)] = min(skip, include)
            return memo[(i, current_sum)]

        result = dfs(0, 0)
        
        # Convert infinity back to -1 for the final answer
        return result if result != float('inf') else -1