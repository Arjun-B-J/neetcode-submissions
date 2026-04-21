# Time Complexity: O(A * C) - We iterate through every amount from 1 to A, and for each amount, we check all C coins.
# Space Complexity: O(A) - We only store a single 1D array of size A + 1.
# Approach: Bottom-Up Dynamic Programming (1D Tabulation)

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount + 1 acts as a localized "infinity". The absolute worst-case scenario 
        # is using entirely '1' value coins, which would take exactly 'amount' coins.
        dp = [amount + 1] * (amount + 1)
        
        dp[0] = 0                                               # Base case: 0 coins are needed to make an amount of 0

        for a in range(1, amount + 1):                          # Build the optimal solution for every amount up to the target
            for c in coins:
                if a - c >= 0:                                  # If we have enough amount to use this coin
                    # Choice: Keep current optimal, OR use 1 of this coin + optimal coins for the remaining amount
                    # Because we iterate left-to-right, dp[a - c] is guaranteed to be fully updated
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # If dp[amount] was never updated from our initial "infinity", the amount is unreachable
        return dp[amount] if dp[amount] != amount + 1 else -1