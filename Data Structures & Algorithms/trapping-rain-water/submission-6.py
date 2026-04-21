class Solution:
    def trap(self, height: List[int]) -> int:
        maxLA = []
        maxRA = []
        maxL,maxR = 0,0
        for ele in height:
            maxLA.append(maxL)
            maxL=max(maxL,ele)
        for ele in reversed(height):
            maxRA.append(maxR)
            maxR=max(maxR,ele)
        maxRA = maxRA[::-1]
        ans = 0
        for i,ele in enumerate(height):
            ans+= max(0,min(maxLA[i],maxRA[i])-ele)
        return ans
