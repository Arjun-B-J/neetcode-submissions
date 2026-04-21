# Time Complexity: O(N^2 log N) - Building the graph takes N^2. The heap processes up to N^2 edges, each taking log(N^2) -> log(N) time.
# Space Complexity: O(N^2) - The adjacency list stores all possible connections for a fully connected graph, taking N^2 space.
# Approach: Prim's Algorithm (Minimum Spanning Tree) using a Min-Heap

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}                   # Map point index to its connections
        
        for i in range(N):                                # Build a fully connected graph
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)        # Calculate Manhattan distance
                adj[i].append([dist, j])                  # Store edges as [cost, neighbor_index]
                adj[j].append([dist, i])

        res = 0                                           # Tracks the total weight of the MST
        visit = set()                                     # Tracks which points are successfully connected
        minH = [[0, 0]]                                   # [cost, point_index], start at point 0 
        
        while len(visit) < N:                             # MST is complete once all N points are connected
            cost, i = heapq.heappop(minH)                 # Always grab the cheapest available connection
            
            if i in visit: continue                       # Skip if this point is already safely in the MST
            
            res += cost                                   # Add the edge cost to our total
            visit.add(i)                                  # Mark this point as officially connected
            
            for neiCost, nei in adj[i]:                   # Look at all possible paths from this new point
                if nei not in visit:                      # Optimization: Ignore edges pointing back into the MST
                    heapq.heappush(minH, [neiCost, nei])  # Add valid outgoing edges to our expanding frontier
                    
        return res