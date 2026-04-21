class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets,cur = [],[]
        

        def helperWithoutDuplicates(i,subsets,cur,nums):
            if i>=len(nums):
                subsets.append(cur.copy())
                return
            
            cur.append(nums[i])
            helperWithoutDuplicates(i+1,subsets,cur,nums)
            cur.pop()

            helperWithoutDuplicates(i+1,subsets,cur,nums)
            
        helperWithoutDuplicates(0,subsets,cur,nums)
        return subsets
            
        