# Time Complexity: O(N^2) - The outer loop runs N times, and the inner loop runs up to N times.
# Space Complexity: O(N) - We store a 1D array of size N.
# Approach: Bottom-Up Dynamic Programming (1D Tabulation)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] represents the length of the longest increasing subsequence starting at index i.
        # Base case: Every element is a valid subsequence of length 1 (just the element itself).
        LIS = [1] * len(nums)
        
        # Build the DP array backwards. 
        # To calculate the LIS starting at 'i', we must already know the LIS for all elements after it.
        for i in range(len(nums) - 1, -1, -1):
            
            # For the current element at 'i', look ahead at all future elements 'j'
            for j in range(i + 1, len(nums)):
                
                # If the future element is strictly larger, we can append it to our sequence
                if nums[j] > nums[i]:
                    # We take the max of what we currently have, OR 
                    # 1 (for the current element) PLUS the pre-calculated LIS starting at 'j'.
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        # The longest increasing subsequence could have started at ANY index, 
        # not just index 0, so we return the maximum value found in the entire array.
        return max(LIS)