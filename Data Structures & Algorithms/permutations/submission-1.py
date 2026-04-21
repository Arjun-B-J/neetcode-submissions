class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i,nums):
            if i==len(nums):
                return [[]]
            res = []
            permutations = helper(i+1,nums)
            for p in permutations:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j,nums[i])
                    res.append(pCopy)
            return res
        
        return helper(0,nums)
        