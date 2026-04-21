class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        rollingSum = 0
        threshold*=k
        ans=0

        L = 0
        for R in range(len(arr)):
            if R-L+1>k:
                rollingSum-=arr[L]
                L+=1
            rollingSum+=arr[R]
            if R-L+1 == k and rollingSum>=threshold:
                ans+=1
        return ans
            
        