# Time Complexity: O(N * S) - Where N is len(stones) and S is sum(stones)/2.
# Space Complexity: O(S) - The set holds at most S distinct sums.
# Approach: Bottom-Up Dynamic Programming (Space Optimized via Set)

from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        possible_sums = {0}                                     # Initialize with 0 (empty subset)
        
        for stone in stones:
            next_sums = possible_sums.copy()                    # Snapshot to avoid modifying set while iterating
            
            for current_sum in possible_sums:
                new_sum = current_sum + stone
                
                if new_sum <= target:                           # We only care about sums up to the halfway point
                    next_sums.add(new_sum)
                    
            possible_sums = next_sums
            
        # The closest we can get to the perfect half is the largest sum in our set
        max_achieved_sum = max(possible_sums)
        
        # The remaining weight is (total - subset1) - subset1
        return total_sum - (2 * max_achieved_sum)