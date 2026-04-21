# Time Complexity: O(E * K) - We iterate through all E flight edges exactly K + 1 times.
# Space Complexity: O(V) - We use two arrays of size V (number of cities) to track the minimum prices.
# Approach: Modified Bellman-Ford Algorithm

from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tempPrices = prices[:]                                # Snapshot: explicitly prevents cascading updates in a single layer
            
            for u, v, w in flights:
                if prices[u] == float("inf"):                     # Skip if the departure city is currently unreachable
                    continue
                    
                if prices[u] + w < tempPrices[v]:                 # Read from snapshot (prices), write to active layer (tempPrices)
                    tempPrices[v] = prices[u] + w
                    
            prices = tempPrices                                   # Commit the layer's updates for the next iteration
        
        return prices[dst] if prices[dst] != float("inf") else -1