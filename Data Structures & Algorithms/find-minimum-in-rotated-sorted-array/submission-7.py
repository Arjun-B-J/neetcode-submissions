class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        mV = nums[0]
        while l<=r:
            if nums[l]<nums[r]: #if already sorted l and r
                return min(mV,nums[l])
            mid = (l+r)//2
            mV = min(mV,nums[mid])
            if nums[mid]>=nums[l]: #in roated part search right
                l=mid+1
            else:
                r=mid-1 #in sorted part search left
        return mV
            