class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(A)>len(B):
            A,B =B,A #get the smallest array to run binary search on
        total = len(A)+len(B)
        half = total//2 #to get the other half from B
        l,r = 0,len(A)-1

        while True:
            i = (l+r)//2
            j = half-i-2
            # we doing -inf A +inf   and -inf B +inf
            Aleft = A[i] if i>=0 else float("-inf") #it can be negative left side then 
            Aright = A[i+1] if i+1 < len(A) else float("inf") #it will be positive inf
            Bleft = B[j] if j>=0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2==1:#odd
                    return min(Bright,Aright)
                else:
                    return (max(Aleft,Bleft) + min(Bright,Aright))/2
            if Aleft>Bright:
                r=i-1
            else:
                l=i+1
