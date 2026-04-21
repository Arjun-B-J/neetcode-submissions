class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # Fix 3: Base case implies 1 way to make 0 amount

        for i in reversed(range(len(coins))):
            cur = [0] * (amount + 1)
            cur[0] = 1  # Base case for the current row
            for a in range(1, amount + 1):
                skip = dp[a]
                include = 0
                if a - coins[i] >= 0:
                    # Fix 1: Don't add 1. Just inherit the number of ways.
                    include = cur[a - coins[i]] 
                
                # Fix 2: Use index 'a' (amount), not 'i' (coin index)
                cur[a] = skip + include 
            dp = cur
            
        return dp[amount]