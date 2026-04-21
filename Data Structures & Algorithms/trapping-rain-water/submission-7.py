class Solution:
    def trap(self, height: List[int]) -> int:
        
        L,R =0,len(height)-1
        maxL,maxR = 0,0
        ans = 0
        while(L<R):
            if height[L]<height[R]:
                ans+=max(maxL-height[L],0)
                maxL = max(height[L],maxL)
                L+=1
            else:
                ans+=max(0,maxR-height[R])
                maxR = max(height[R],maxR)
                R-=1
        return ans
        