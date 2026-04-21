# Time Complexity: O(n) - We iterate from step 3 to n exactly once.
# Space Complexity: O(1) - We only maintain a 2-element array, which scales independently of n.
# Approach: Bottom-Up Dynamic Programming (Space Optimized Fibonacci)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n                                      # Base cases: 1 way for 1 step, 2 ways for 2 steps
            
        dp = [1, 2]                                       # dp[0] represents (n-2) ways, dp[1] represents (n-1) ways
        
        for _ in range(3, n + 1):                         # Build the sequence iteratively
            dp[0], dp[1] = dp[1], dp[0] + dp[1]           # Shift window: n-2 becomes n-1, and the new n is their sum
            
        return dp[1]                                      # dp[1] holds the final accumulated ways for step n