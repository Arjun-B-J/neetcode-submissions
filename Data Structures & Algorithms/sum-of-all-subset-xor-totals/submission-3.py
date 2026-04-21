# ==========================================
# Approach 1: Optimized DFS (On-the-fly XOR)
# Time Complexity: O(2^N) - We branch 2 ways for each of the N elements.
# Space Complexity: O(N) - We only use memory for the recursion call stack (depth of N). No arrays are stored!
# ==========================================
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, current_xor):
            # Base Case: We've made a decision for every element.
            # Return the XOR total of this specific subset path.
            if i == len(nums):
                return current_xor
            
            # Branch 1: Pick the current element (XOR it with our running total)
            include = dfs(i + 1, current_xor ^ nums[i])
            
            # Branch 2: Don't pick the current element (keep running total as is)
            exclude = dfs(i + 1, current_xor)
            
            # The total for this subtree is the sum of both branching paths
            return include + exclude

        # Start at index 0, with an initial XOR sum of 0
        return dfs(0, 0)