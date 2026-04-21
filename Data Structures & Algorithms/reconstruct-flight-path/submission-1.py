# Time Complexity: O(E^d) - Where E is total tickets and d is the max flights from one airport. Backtracking can explore many dead ends in the worst case.
# Space Complexity: O(V + E) - Space for the adjacency list O(E) and the recursion stack tracking the itinerary O(V).
# Approach: Depth-First Search (DFS) with Backtracking

from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()                                      # Sort globally so our adjacency list is naturally in lexical order
        
        for src, dst in tickets:
            adj[src].append(dst)                            # Build directed graph mapping departure -> destinations
        
        res = ["JFK"]                                       # Itinerary must always begin at JFK
        
        def dfs(src):
            if len(res) == len(tickets) + 1:                # Base Case: All tickets used, valid itinerary formed
                return True
            if not adj[src]:                                # Dead end: No outgoing flights left, but tickets remain
                return False
            
            for i in range(len(adj[src])):                  # Iterate by index to allow safe in-place modification
                dst = adj[src].pop(i)                       # "Take" the ticket by removing it from the graph
                res.append(dst)                             # Add the destination to our active route
                
                if dfs(dst):                                # Recursively try to finish the trip from this new airport
                    return True                             # Bubble up success immediately to halt all other branches
                    
                adj[src].insert(i, dst)                     # Backtrack: Route failed, return the ticket to its exact spot
                res.pop()                                   # Backtrack: Remove destination from active route
                
        dfs("JFK")
        return res