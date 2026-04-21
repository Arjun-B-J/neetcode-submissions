class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*(m+1)
        dp[m-1]=1
        for r in reversed(range(n)):
            for c in reversed(range(m)):
                dp[c]+=dp[c+1]
        return dp[0]
