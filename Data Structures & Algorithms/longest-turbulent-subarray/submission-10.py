class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r = 0,1
        res,prev = 1,""

        while r < len(arr):
            if arr[r]> arr[r-1] and prev!=">":
                prev = ">"
                res = max(res,r-l+1)
                r+=1
            elif arr[r]< arr[r-1] and prev!="<":
                prev = "<"
                res = max(res,r-l+1)
                r+=1
            else:
                r = r+1 if arr[r]==arr[r-1] else r
                l=r-1
                prev=""
        return res
        