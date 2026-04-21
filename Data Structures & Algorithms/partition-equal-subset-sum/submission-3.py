class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False
        target/=2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            nextDp = dp.copy()
            for j in dp:
                nextDp.add(j+nums[i])
            dp = nextDp
        return True if target in nextDp else False
        