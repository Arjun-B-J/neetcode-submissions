class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i,profit,weight,capacity,cache):
            if i == len(profit):
                return 0
            if cache[i][capacity]!=-1:
                return cache[i][capacity]
            
            #skip i 
            cache[i][capacity] = dfs(i+1,profit,weight,capacity,cache)
            #include i
            newCapacity = capacity-weight[i]
            if newCapacity>=0:
                p = profit[i] + dfs(i+1,profit,weight,newCapacity,cache)
                cache[i][capacity] = max(p,cache[i][capacity])
            return cache[i][capacity]
        cache = [[-1]* (capacity + 1) for _ in range(len(profit))]
        return dfs(0,profit,weight,capacity,cache)
