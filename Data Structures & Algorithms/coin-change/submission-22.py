class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins) #number of coins that i have 
        dfs = [float('inf')]*(amount+1)

        #base amount must be 0 as we doing perfect conversion
        dfs[amount] = 0
        
        for i in reversed(range(n)):
            for current_sum in reversed(range(amount)):
                #skip i
                skip = dfs[current_sum]
                #include i
                include = float("inf")
                if current_sum+coins[i]<=amount:
                    include = 1 + dfs[current_sum+coins[i]]
                dfs[current_sum] = min(skip,include)

        return dfs[0] if dfs[0]!=float('inf') else -1



        


    






