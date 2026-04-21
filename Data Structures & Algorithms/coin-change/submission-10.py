class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize 1D array with Infinity
        dp = [float('inf')] * (amount + 1)
        dp[amount] = 0 # Base case: We are already at the target
        
        for coin in coins:
            # We iterate BACKWARDS because we need the 'larger' sum to be ready
            # to calculate the 'smaller' sum.
            for current_sum in range(amount - 1, -1, -1):
                if current_sum + coin <= amount:
                    dp[current_sum] = min(dp[current_sum], 1 + dp[current_sum + coin])
                    
        return dp[0] if dp[0] != float('inf') else -1