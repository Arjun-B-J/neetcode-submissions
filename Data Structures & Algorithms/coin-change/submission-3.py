class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i,cash,c):
            #base
            if cash==amount:
                return c
            if cash>amount or i==len(coins):
                return -1
            #cache
            if (i,cash,c) in cache:
                return cache[(i,cash,c)]

            skip = dfs(i+1,cash,c)
            include = dfs(i,cash+coins[i],c+1)
            if skip!=-1 and include!=-1:
                cache[(i,cash,c)] = min(skip,include)
            elif skip==-1 and include!=-1:
                cache[(i,cash,c)] = include
            elif include==-1 and skip!=-1:
                cache[(i,cash,c)] = skip
            else:
                cache[(i,cash,c)] = -1
            return cache[(i,cash,c)]

        return dfs(0,0,0)