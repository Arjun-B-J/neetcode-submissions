class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax,curMin,globalMax,globalMin = 0,0,nums[0],nums[0]
        total =0
        for num in nums:
            total+=num
            curMax = max(curMax,0)+num
            curMin = min(curMin,0)+num
            globalMax = max(globalMax,curMax)
            globalMin = min(globalMin,curMin)
        return max(globalMax,total-globalMin) if globalMax>0 else globalMax