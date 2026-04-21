class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            
            #left half is sorted
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]: #if target falls in the left range
                    r=mid-1 #discard right half
                else:
                    l=mid+1
            #right half is sorted
            else:
                if nums[mid]<target<=nums[r]: #if target falls in the right range
                    l=mid+1 #discard left half
                else:
                    r=mid-1
        return -1
