class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helperWithDuplicates(i,subsets,cur,nums):
            if i>=len(nums):
                subsets.append(cur.copy())
                return 
            cur.append(nums[i])
            helperWithDuplicates(i+1,subsets,cur,nums)
            cur.pop()

            #dont include now, and skip to a non duplicate val
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helperWithDuplicates(i+1,subsets,cur,nums)


        subsets,cur = [],[]
        nums.sort() # here we sort so that duplicates are adjacent to each other
        helperWithDuplicates(0,subsets,cur,nums) 
        return subsets
