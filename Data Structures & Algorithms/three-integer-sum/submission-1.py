class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tuples = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                tuples[(i,j)] = nums[i]+nums[j]
        ans = []
        for i in range(len(nums)):
            for k,v in tuples.items():
                if i==k[0] or i==k[1]:
                    continue
                if nums[i]+v==0:
                    ans.append([nums[i],nums[k[0]],nums[k[1]]])
        return [list(item) for item in {tuple(sorted(row)) for row in ans}]
