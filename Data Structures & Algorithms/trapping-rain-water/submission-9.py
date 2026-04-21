class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0,len(height)-1
        maxL,maxR = 0,0
        ans = 0
        while(L<R):
            if height[L]<height[R]:
                ans += max(0,maxL-height[L])
                maxL = max(maxL,height[L])
                L+=1
            else:
                ans += max(0,maxR-height[R])
                maxR = max(maxR,height[R])
                R-=1
        return ans