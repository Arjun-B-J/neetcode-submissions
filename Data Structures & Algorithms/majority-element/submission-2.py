# Time Complexity: O(N) - We iterate through the array exactly once.
# Space Complexity: O(1) - We only use two integer variables.
# Approach: Boyer-Moore Majority Vote Algorithm

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for num in nums:
            # If our count hits 0, our current candidate has been completely "canceled out".
            # We must pick the current number as the new candidate.
            if count == 0:
                res = num
                
            # If the current number matches our candidate, it gains strength (+1).
            # If it's an enemy number, it cancels out one of our candidate's votes (-1).
            if num == res:
                count += 1
            else:
                count -= 1
                
        # Because the majority element appears > N/2 times, 
        # it is mathematically guaranteed to survive the cancellations.
        return res