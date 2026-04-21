# Time Complexity: O(E log V) - Where E is the number of edges and V is the number of nodes. Pushing/popping from the heap takes log(V) time, and we process each edge at most once.
# Space Complexity: O(E + V) - Space is required for the adjacency list (E), the min-heap (up to E edges), and the visited dictionary (V).
# Approach: Dijkstra's Algorithm using a Min-Heap (Shortest Path on a Weighted Directed Graph)

import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        
        # Build adjacency list: map each node to its outgoing edges as (destination, weight)
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((v, t))

        # Min-heap stores tuples of (accumulated_time, current_node)
        # We start at the source node 'k' with an accumulated time of 0
        heapq.heappush(minHeap, (0, k))
        
        # Acts as our 'visited' set while simultaneously storing the shortest path to each node
        bestTime = {} 
        
        while minHeap:
            # The min-heap guarantees we always expand the node with the shortest known path first
            t1, u = heapq.heappop(minHeap)
            
            # If we've already settled the shortest path for this node, ignore duplicate entries 
            if u in bestTime:
                continue
                
            # The first time we pop a node, it is mathematically guaranteed to be its absolute shortest path
            bestTime[u] = t1

            # Explore all outgoing connections from the current node
            for v, t2 in adj[u]:
                # Optimization: Only push to the heap if we haven't already found the shortest path to 'v'
                if v not in bestTime:
                    heapq.heappush(minHeap, ((t2 + t1), v))
                    
        minTime = -1
        
        # Verify that the signal actually reached every single node
        for i in range(1, n + 1):
            if i not in bestTime:
                return -1 # Graph is disconnected; at least one node is unreachable
            
            # The total network delay is determined by the node that took the LONGEST to receive the signal
            minTime = max(minTime, bestTime[i])
            
        return minTime