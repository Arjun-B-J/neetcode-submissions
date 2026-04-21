from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1 # l = buy day, r = sell day

        
        while r < len(prices):
            # If selling today is profitable, check if it's our new max profit
            if prices[r] > prices[l]:
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            # If today's price is lower than our buy price, 
            # we found a better (cheaper) day to buy. Jump 'l' to 'r'.
            else:
                l = r
                
            r += 1 # Always move the sell day forward to check the next day
            
        return maxP