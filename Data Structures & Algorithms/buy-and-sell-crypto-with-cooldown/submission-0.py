class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp= {}
        def dfs(i,buyState):
            if i >= len(prices):
                return 0
            state = (i,buyState)
            if state in dp:
                return dp[state]
            
            #deal with buying
            if buyState:
                buy = dfs(i+1,False) - prices[i]
                cooldown = dfs(i+1,True)
                dp[state] = max(buy,cooldown)
            #deal with selling
            else:
                sell = dfs(i+2,True) + prices[i]
                cooldown = dfs(i+1,False)
                dp[state] = max(sell,cooldown)
            return dp[state]
        return dfs(0,True)
