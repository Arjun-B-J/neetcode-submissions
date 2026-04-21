class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:return 1
        l,r = 0,x//2
        while l<=r:
            mid = (l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                r=mid-1
            else:
                l=mid+1
        return r