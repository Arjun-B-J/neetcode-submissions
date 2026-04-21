class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # we sort and make it 2 sum
        for i,val in enumerate(nums):
            if i>0 and val==nums[i-1]: #skip the same ele to avoid dups
                continue
            l,r = i+1,len(nums)-1 #2sum begins
            while l<r:
                threshold = val + nums[l]+nums[r]
                if threshold>0:
                    r-=1
                elif threshold<0:
                    l+=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]: # we update only one pointer cause the above logic handles for the right
                        l+=1 # beacuse the array is sorted, moving l will break the threshold everytime, so no valid r dups
        return res