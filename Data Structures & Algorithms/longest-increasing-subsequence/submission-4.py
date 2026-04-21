import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def get_insertion_index(arr,target):
            l,r = 0, len(arr)
            while l<r:
                mid = (l+r)//2
                if target > arr[mid]:
                    l=mid+1
                else:
                    r=mid
            return l
        tails= []
        for n in nums:
            idx = get_insertion_index(tails,n)
            if idx==len(tails):
                tails.append(n)
            else:
                tails[idx]=n
        return len(tails)