class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache ={}
        def dfs(i):
            if i>=len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = 0 if i==-1 else cost[i]
            cache[i] += min(dfs(i+1),dfs(i+2))

            return cache[i]
         
        return dfs(-1)