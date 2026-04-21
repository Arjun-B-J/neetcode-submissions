class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i,profit,weight,capacity):
            if i == len(profit):
                return 0
            #skip i 
            maxProfit = dfs(i+1,profit,weight,capacity)
            #include i
            newCapacity = capacity-weight[i]
            if newCapacity>=0:
                p = profit[i] + dfs(i+1,profit,weight,newCapacity)
                maxProfit = max(p,maxProfit)
            return maxProfit

        return dfs(0,profit,weight,capacity)
