from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        i = 0
        jumps=0
        while i < len(nums) - 1:
            jump_distance = nums[i]
            curCoverage = i + jump_distance
            jumps+=1
            
            # If our current jump can reach or exceed the last index, we win.
            if curCoverage >= len(nums) - 1:
                return jumps
                
            # 'best_next_idx' will store the index that gives us the furthest reach
            best_next_idx = i
            max_future_reach = curCoverage
            
            # Scan all indices we can reach from our current position 'i'
            for j in range(i + 1, curCoverage + 1):
                # If jumping from 'j' gets us further than our current best, update it
                if j + nums[j] > max_future_reach:
                    max_future_reach = j + nums[j]
                    best_next_idx = j
                    
            # If we scanned our whole jump window and couldn't find a way to extend 
            # our reach (i.e., we are stuck on a 0), we fail.
            if best_next_idx == i:
                return -1
                
            # Move to the best index we found
            i = best_next_idx
            
            
        return jumps