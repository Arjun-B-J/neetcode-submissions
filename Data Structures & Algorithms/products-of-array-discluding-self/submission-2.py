class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixP = []
        cur = 1
        for ele in nums:
            cur*=ele
            prefixP.append(cur)
        postfixP = []
        cur = 1
        for ele in reversed(nums):
            cur*=ele
            postfixP.append(cur)
        postfixP = postfixP[::-1]
        ans = []
        for i in range(len(nums)):
            left = 1 if i<1 else prefixP[i-1]
            right = 1 if i>=len(nums)-1 else postfixP[i+1]
            ans.append(left*right)
        return ans     