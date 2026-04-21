class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i,amount):
            if amount==0:
                return 1
            if amount<0 or i==len(coins):
                return 0
            state = (i,amount)
            if state in cache:
                return cache[state]
            cache[state] = dfs(i+1,amount)+dfs(i,amount-coins[i])
            return cache[state]
        return dfs(0,amount)