class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0

        for _ in range(k+1):
            tempPrices = prices.copy() #for the k stop thing
            for u,v,w in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u]+w < tempPrices[v]:
                    tempPrices[v] = prices[u]+w
            prices = tempPrices
        
        return prices[dst] if prices[dst]!=float("inf") else -1
