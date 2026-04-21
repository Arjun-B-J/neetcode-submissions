class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ele in nums:
            if ele not in count:
                count[ele] = 1
            else:
                return True
        return False
        