class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneT = sum(stones)
        target = (stoneT//2) #since we cal just above
        dp = {}
        def dfs(i,total):
            if i==len(stones) or total>=target:
                return abs(total - (stoneT-total)) #other half - current half
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = min(dfs(i+1,total),dfs(i+1,total+stones[i]))
            return dp[(i,total)]

        return dfs(0,0)
        