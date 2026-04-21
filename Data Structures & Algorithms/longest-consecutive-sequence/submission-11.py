class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0

        for num in nums:
            if num-1 not in numSet:
                l = 0
                while num+l in numSet:
                    l+=1
                ans = max(l,ans)
        return ans
        