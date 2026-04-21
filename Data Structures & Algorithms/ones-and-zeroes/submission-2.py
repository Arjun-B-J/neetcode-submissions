# Time Complexity: O(L * M * N)
# Space Complexity: O(M * N) - We drop the 'L' dimension entirely, saving massive amounts of memory.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 2D Tabulation)

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[j][k] represents max strings formed with 'j' zeros and 'k' ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # MUST traverse backwards to prevent reusing the same string in the same loop iteration!
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    
                    # dp[j][k] acts as 'skip' (from previous string's loop)
                    # 1 + dp[j-zeros][k-ones] acts as 'include'
                    dp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones])

        return dp[m][n]