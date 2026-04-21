# Time Complexity: O(M * N)
# Space Complexity: O(N) - We drop the 'M' dimension, only storing an array of size N + 1.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 1D Tabulation)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        
        # We only need a 1D array of size N + 1. 
        # dp[j] currently acts as dp[i+1][j]. When we update it, it becomes dp[i][j].
        dp = [0] * (N + 1)
        dp[N] = 1 # Base case: empty 't' matches 1 time
        
        for i in range(M - 1, -1, -1):
            # MUST traverse backwards (N-1 down to 0) to avoid overwriting values
            # in dp[j+1] that we still need to calculate dp[j] in the current row.
            for j in range(N):
                
                if s[i] == t[j]:
                    dp[j] = dp[j + 1] + dp[j]
                
                # If s[i] != t[j], dp[j] = dp[j], so we literally do nothing!
                
        return dp[0]