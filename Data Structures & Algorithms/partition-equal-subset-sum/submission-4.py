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
                if j+nums[i]==target:
                    return True
                nextDp.add(j+nums[i])
            dp = nextDp
        return False
        