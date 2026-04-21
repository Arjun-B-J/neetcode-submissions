class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curComb,res = [],[]

        def helper(i,nums,target,curComb,res):
            if 0==target:
                res.append(curComb.copy())
                return
            if 0>target:
                return
    
            #Do Combinations for i, in accending Order, 1,2 if counted need not be counted as 2,1 so skip i-1.. val for i
            for j in range(i,len(nums)):
                curComb.append(nums[j])
                helper(j,nums,target-nums[j],curComb,res)
                curComb.pop()


        helper(0,nums,target,curComb,res)
        return res