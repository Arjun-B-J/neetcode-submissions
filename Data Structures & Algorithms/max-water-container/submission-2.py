class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0, len(heights)-1
        ans =0
        while L<R:
            ans = max(ans,(R-L) * min(heights[L],heights[R]))
            if heights[L]<heights[R]:
                L+=1
            else:
                R-=1
        return ans

        