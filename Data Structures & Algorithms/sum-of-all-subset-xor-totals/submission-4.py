# ==========================================
# Approach 1: Optimized DFS (On-the-fly XOR)
# Time Complexity: O(2^N) - We branch 2 ways for each of the N elements.
# Space Complexity: O(N) - We only use memory for the recursion call stack (depth of N). No arrays are stored!
# ==========================================
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # INTERVIEW FLEX: There is a mathematical property for this specific problem.
        # The sum of all XOR totals of subsets is exactly equal to:
        # (The Bitwise OR of all elements) multiplied by 2^(N-1).
        
        bitwise_or = 0
        for num in nums:
            bitwise_or |= num
            
        return bitwise_or * (1 << (len(nums) - 1))