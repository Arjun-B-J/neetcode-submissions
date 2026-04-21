class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins) #number of coins that i have
        cache = {}
        def dfs(i,current_sum):
            #base
            if current_sum == amount: # we reach the success point
                return 0
            if i>=n or current_sum>amount: # cant reach 
                return float("inf")
            if (i,current_sum) in cache:
                return cache[(i,current_sum)]

            #skip i
            skip = dfs(i+1,current_sum)
            #include i
            include = 1 + dfs(i,current_sum+coins[i])

            cache[(i,current_sum)] = min(skip,include)
            return cache[(i,current_sum)]

        ans = dfs(0,0)
        return ans if ans!=float("inf") else -1


    






