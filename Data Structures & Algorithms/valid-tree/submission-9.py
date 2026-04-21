# Time Complexity: O(V) - With E exactly V-1, time scales linearly. Array lookups remove dictionary hashing overhead.
# Space Complexity: O(V) - Pre-allocated lists of size V for parent and rank tracking.
# Approach: Union-Find (List/Array Optimization)

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False                      # Guard clause ensures E = V - 1
        
        parent = list(range(n))                                   # OPTIMIZATION: Array instead of dictionary
        rank = [1] * n                                            # OPTIMIZATION: Array instead of dictionary

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])                       # Path compression remains identical
            return parent[x]
    
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False                             

            if rank[px] > rank[py]:                               # Union by size remains identical
                rank[px] += rank[py]
                parent[py] = px
            else:
                rank[py] += rank[px]
                parent[px] = py
            return True

        for x, y in edges:
            if not union(x, y):                                   # Because parent/rank are local variables, we drop the 'uf.' prefix
                return False

        return True