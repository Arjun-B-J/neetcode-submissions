class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        dp = [1,2]
        i=3
        while i<=n:
            i+=1
            dp[0],dp[1] = dp[1],dp[0]+dp[1]
        return dp[1]