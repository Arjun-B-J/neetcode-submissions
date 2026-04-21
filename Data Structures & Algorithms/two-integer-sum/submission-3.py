class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for num in nums:
            if num not in present:
                present[num] = 1
            else:
                present[num] += 1
        for i,num in enumerate(nums):
            if target-num in present:
                if target-num == num and present[target-num]>1:
                    return [i,nums.index(target-num,i+1)]
                elif target-num!=num:
                    return [i,nums.index(target-num)]


        