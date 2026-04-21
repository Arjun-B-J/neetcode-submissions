# Time Complexity: O(N^3)
# Space Complexity: O(N^2) - We store a 2D matrix of size (N+2) x (N+2).
# Approach: Bottom-Up Dynamic Programming (Length-Based Tabulation)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[l][r] represents the max coins collected by bursting balloons in range [l, r]
        dp = [[0] * n for _ in range(n)]
        
        # We must build the table by answering smaller subarray lengths first.
        # length goes from 1 balloon up to the original N balloons.
        for length in range(1, n - 1):
            
            # Slide the window of size 'length' across the array
            for l in range(1, n - length):
                r = l + length - 1
                
                # Try making every balloon 'k' in this window the LAST one to pop
                for k in range(l, r + 1):
                    
                    coins = dp[l][k - 1] + (nums[l - 1] * nums[k] * nums[r + 1]) + dp[k + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
                    
        # The answer is the max coins gained bursting balloons from original index 1 to N
        return dp[1][n - 2]