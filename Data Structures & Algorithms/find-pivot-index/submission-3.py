class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=0
        prefix=[]
        postfix=[]
        for ele in nums:
            total+=ele
            prefix.append(total)
        total=0
        for ele in reversed(nums):
            total+=ele
            postfix.append(total)
        postfix=postfix[::-1]
        for i,ele in enumerate(nums):
            left = 0 if i<1 else prefix[i-1]
            right = 0 if i>=len(nums)-1 else postfix[i+1]
            if left==right:
                return i
        return -1  
        