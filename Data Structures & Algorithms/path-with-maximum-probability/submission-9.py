# Time Complexity: O(E log V) - Heap operations take log(V), processing edges takes E.
# Space Complexity: O(E + V) - Space for the adjacency list (E), max-heap (E), and visited dict (V).
# Approach: Modified Dijkstra's Algorithm (Max-Heap with multiplicative path weights)

import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}                           # Map each node to its connected neighbors
        for i in range(len(edges)):                               # Build undirected graph
            adj[edges[i][0]].append((edges[i][1], succProb[i]))   # Store as (neighbor, probability)
            adj[edges[i][1]].append((edges[i][0], succProb[i]))   
      
        maxHeap = []
        distance = {}                                             # Tracks settled max probability to each node
        heapq.heappush(maxHeap, (-1, start_node))                 # Push -1 (100% prob) to simulate max-heap

        while maxHeap:
            w1, u = heapq.heappop(maxHeap)                        # Expand the highest probability path first
            w1 = abs(w1)                                          # Convert negative back to positive probability
            
            if u == end_node: return w1                           # First arrival guarantees max probability
            if u in distance: continue                            # Ignore lower-probability duplicate paths
            distance[u] = w1                                      # Lock in the max probability for this node

            for v, w2 in adj[u]:                                  # Explore outgoing connections
                if v not in distance:                             # Optimization: only push if not settled
                    heapq.heappush(maxHeap, (-w1 * w2, v))        # Multiply probabilities, push as negative
            
        return 0.0                                                # Return 0 if the end node is unreachable