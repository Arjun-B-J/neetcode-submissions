# Time Complexity: O(V + E * alpha(V)) - Initializing takes O(V), processing edges takes amortized O(1) per edge.
# Space Complexity: O(V) - Space used by the parent and rank dictionaries inside the UnionFind class.
# Approach: Union-Find (Cycle Detection & Connectivity)

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False                      # A valid tree MUST have exactly n - 1 edges
        
        class UnionFind:
            def __init__(self, n):
                self.rank = {i: 1 for i in range(n)}              # Tracks the size of the component
                self.parent = {i: i for i in range(n)}            # Each node is its own root initially

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])    # Recursive path compression
                return self.parent[x]                             # Returns the guaranteed absolute root
        
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py: return False                         # Cycle detected: Nodes already connected

                if self.rank[px] > self.rank[py]:                 # Union by size
                    self.rank[px] += self.rank[py]
                    self.parent[py] = px
                else:
                    self.rank[py] += self.rank[px]
                    self.parent[px] = py
                return True

        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x, y):                                # Build the tree edge by edge
                return False                                      # Return early if any cycle is formed

        return True                                               # No cycles + exactly n-1 edges = Valid Tree