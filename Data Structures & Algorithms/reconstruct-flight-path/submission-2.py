# Time Complexity: O(E log(E/V)) - Sorting the destinations takes O(E log E). The traversal processes each edge exactly once in O(E).
# Space Complexity: O(V + E) - Space for the adjacency list O(E) and the recursion stack O(E) in the worst case (a single continuous flight path).
# Approach: Hierholzer's Algorithm (Eulerian Path with Post-Order Traversal)

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # Sort in reverse lexical order so the smallest destination is at the END of the list
        tickets.sort(key=lambda x: x[1], reverse=True)
        
        for src, dst in tickets:
            adj[src].append(dst)                            # Build graph: JFK -> [SFO, ATL] (SFO is first, ATL is last)
            
        res = []
        
        def dfs(src):
            while adj[src]:                                 # While this airport still has outgoing flights available
                next_dest = adj[src].pop()                  # O(1) pop removes the lexically smallest destination
                dfs(next_dest)                              # Immediately fly there
                
            res.append(src)                                 # Post-order: No flights left? Add to route and step back
            
        dfs("JFK")
        
        return res[::-1]                                    # The route was built backwards from the final destination, so reverse it