# Time Complexity: O(V + E) - We build the adjacency list and visit every node and edge at most once.
# Space Complexity: O(V + E) - Space is used by the adjacency list and the worst-case recursion stack.
# Approach: Depth-First Search (Cycle Detection & Connectivity in Undirected Graph)

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False                      # Guard clause: A valid tree MUST have exactly n-1 edges
        
        adj = {i: [] for i in range(n)}                           # Initialize adjacency list
        for u, v in edges:
            adj[u].append(v)                                      # Undirected graph requires 2-way connections
            adj[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit: return False                        # Cycle detected: We hit a node we've already seen
            
            visit.add(node)                                       # Mark as safely visited
            
            for nei in adj[node]:
                if nei == prev: continue                          # Skip the trivial cycle (going right back to the parent)
                
                if not dfs(nei, node): return False               # Pass current node as 'prev', bubble up any failures
                    
            return True
            
        # A valid tree must have no cycles (dfs returns True) AND be fully connected (we visited all 'n' nodes)
        return dfs(0, -1) and len(visit) == n