# Time Complexity: O(N log N) - We iterate through the array once O(N), and for each element, we perform a Binary Search O(log N).
# Space Complexity: O(N) - For the 'tails' array.
# Approach: Binary Search / Patience Sorting

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] stores the smallest tail of all increasing subsequences of length i+1.
        tails = []
        
        for num in nums:
            # bisect_left finds the index where 'num' should be inserted to maintain sorted order
            idx = bisect.bisect_left(tails, num)
            
            # If the index is equal to the length of 'tails', it means 'num' is larger 
            # than all current tails. We can extend our longest subsequence!
            if idx == len(tails):
                tails.append(num)
                
            # Otherwise, 'num' is smaller than or equal to an existing tail. 
            # We replace that tail with 'num'. This doesn't change the max length, 
            # but it lowers the barrier for future numbers to extend the sequence.
            else:
                tails[idx] = num
                
        return len(tails)