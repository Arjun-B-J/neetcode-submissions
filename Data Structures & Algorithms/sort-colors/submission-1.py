from collections import  Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i]=n
                i+=1
        return nums
        