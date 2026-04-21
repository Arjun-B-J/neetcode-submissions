class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,cur = 0 ,0
        for num in nums:
            temp = max(prev+num,cur)
            prev,cur = cur,temp 
        return cur