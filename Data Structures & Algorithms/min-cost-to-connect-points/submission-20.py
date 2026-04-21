# Time Complexity: O(N^2 log N) - Generating N^2 edges and pushing/popping them from the heap takes log(N^2) -> log(N) time.
# Space Complexity: O(N^2) - The min-heap must hold all N^2 possible edges at the start.
# Approach: Kruskal's Algorithm (Minimum Spanning Tree) using Union-Find

import heapq
from typing import List

class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(n)}               # Initially, every node is its own parent (root)
        self.rank = {i: 0 for i in range(n)}              # Tracks tree size/depth to keep the structure flat

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]           # Path compression: point node to its grandparent
            x = self.par[x]
        return x
    
    def union(self, x, y) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2: return False                         # Cycle detected: nodes are already in the same set
        
        if self.rank[p1] > self.rank[p2]:                 # Union by size/rank: merge smaller tree into the larger one
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        minH = []                                         # Will queue all edges from cheapest to most expensive
        
        for i in range(N):                                # Generate a complete graph (all possible connections)
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)        # Edge weight is the Manhattan distance
                heapq.heappush(minH, (dist, i, j))        # Store as (weight, node1, node2)

        mst = []                                          # Tracks the valid edges forming our MST
        cost = 0                                          # Accumulator for the total MST weight
        uf = UnionFind(N)                                 # Disjoint set prevents us from forming closed loops
        
        while minH:
            w, u, v = heapq.heappop(minH)                 # Always grab the absolute cheapest global edge
            
            if not uf.union(u, v): continue               # Skip this edge entirely if it creates a cycle
                
            mst.append((u, v))                            # Edge is safe; officially add it to the MST
            cost += w
            
        if len(mst) != N - 1: return -1                   # Guard clause: a valid MST must have exactly N-1 edges
        
        return cost