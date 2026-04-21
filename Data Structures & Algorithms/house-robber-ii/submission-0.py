class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber1(nums):
            rob1,rob2 = 0,0
            for n in nums:
                rob1,rob2 = rob2,max(rob2,rob1+n)
            return rob2  

        return max(nums[0],houseRobber1(nums[1:]),houseRobber1(nums[:-1]))

        