class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
                #explore all
            dp[i] = float("inf")
            for cost,duration in zip(costs,[1,7,30]):
                j = i
                while j < len(days) and days[j] < days[i]+duration:
                    j+=1
                dp[i] = min(dp[i],cost+dfs(j))

            return dp[i]
        return dfs(0)