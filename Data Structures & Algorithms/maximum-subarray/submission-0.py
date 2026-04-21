class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        cur = 0
        for num in nums:
            cur = max(cur,0)+num
            maxi = max(cur,maxi)
        return maxi