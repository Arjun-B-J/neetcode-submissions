from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = deque()
        maxP = 0
        p = 0
        for price in prices:
            window.append(price)
            if len(window)>1:
                p = window[-1]-window[0]
                print(p)
                maxP = max(p,maxP)
                if p<0:
                    while len(window)!=1:
                        window.popleft()
        return maxP
