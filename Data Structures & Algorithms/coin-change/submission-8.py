class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        #for each amount what is min number of coins, we solve this subproblem
        for a in range(1,amount+1):
            #check all coins
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        
        return dp[amount] if dp[amount]!= amount+1 else -1