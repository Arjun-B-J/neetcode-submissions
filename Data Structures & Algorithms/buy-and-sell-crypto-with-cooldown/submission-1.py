# Time Complexity: O(N)
# Space Complexity: O(N) - We store a 2D matrix (or hash map) of size N x 2.
# Approach: Bottom-Up Dynamic Programming (Backwards Tabulation)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices: return 0
        
        # dp map holding (index, can_buy_boolean) -> max_profit
        dp = {}
        
        # Base cases: Any day out of bounds yields 0 profit
        dp[(n, True)] = dp[(n, False)] = 0
        dp[(n + 1, True)] = dp[(n + 1, False)] = 0 
        
        # Build backwards from the last day
        for i in range(n - 1, -1, -1):
            #buy
            buy = dp[(i+1,False)] - prices[i]
            cooldown = dp[(i+1,True)]
            dp[(i,True)] = max(buy,cooldown)

            #sell
            sell = dp[(i+2,True)] + prices[i]
            cooldown = dp[(i+1,False)]
            dp[(i,False)] = max(sell,cooldown)
            
        return dp[(0, True)]