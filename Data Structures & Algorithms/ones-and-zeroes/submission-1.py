# Time Complexity: O(L * M * N)
# Space Complexity: O(L * M * N) - We store the entire 3D history of states.
# Approach: Bottom-Up Dynamic Programming (3D Tabulation)

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L = len(strs)
        # dp[i][j][k] represents max strings from first 'i' items using exactly 'j' zeros and 'k' ones
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(L + 1)]

        for i in range(L):
            zeros = strs[i].count('0')
            ones = len(strs[i]) - zeros                             # Slightly faster than calling .count() twice
            
            for j in range(m + 1):
                for k in range(n + 1):
                    skip = dp[i][j][k]                              # Inherit max without this string
                    
                    include = 0
                    if j >= zeros and k >= ones:
                        include = 1 + dp[i][j - zeros][k - ones]    # 1 + max from remaining capacity
                        
                    dp[i + 1][j][k] = max(skip, include)

        return dp[L][m][n]