import math
class Solution:
    def calculateTime(self,mid,piles):
        t = 0
        for ele in piles:
            t+= math.ceil(ele/mid)
        return t
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        H = max(piles)
        while(L<=H):
            mid = (L+H)//2
            if self.calculateTime(mid,piles) > h:
                L = mid+1
            else:
                H = mid-1
        return L
        