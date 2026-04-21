class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins) #number of coins that i have 
        dfs = [[float('inf')]*(amount+1) for _ in range(n+1)]

        #base i,amount must be 0 as we doing perfect conversion
        for i in range(n+1):
            dfs[i][amount]=0
        
        for i in reversed(range(n)):
            for current_sum in reversed(range(amount)):
                #skip i
                skip = dfs[i+1][current_sum]
                #include i
                include = float("inf")
                if current_sum+coins[i]<=amount:
                    include = 1 + dfs[i][current_sum+coins[i]]
                dfs[i][current_sum] = min(skip,include)

        return dfs[0][0] if dfs[0][0]!=float('inf') else -1



        


    






