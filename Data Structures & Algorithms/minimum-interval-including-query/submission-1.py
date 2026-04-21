# Time Complexity: O(N log N + Q log Q) - Sorting both arrays dictates the runtime.
# Space Complexity: O(N + Q) - For the heap and the result hash map.
# Approach: Offline Queries (Sweep Line) + Min-Heap with Lazy Deletion

import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by start time so we can sweep left-to-right
        intervals.sort()
        
        minHeap = []
        res = {}
        i = 0
        
        # Sort the queries to move our "sweep line" forward chronologically.
        # This is called "Offline Queries" because we don't process them in the order they arrived.
        for q in sorted(queries):
            
            # 1. ADD VALID INTERVALS TO THE POOL
            # If an interval starts BEFORE or EXACTLY ON our query line, it might cover it!
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i][0], intervals[i][1]
                
                # Push a tuple of (size, end_time) to the min-heap
                # We prioritize by smallest size. We store end_time so we know when it expires.
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
                
            # 2. LAZY DELETION (CLEANUP THE TRASH)
            # Some intervals in our heap may have already ended before our current query 'q'.
            # If the SMALLEST interval in our heap is expired, pop it out!
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            # 3. RECORD THE ANSWER
            # The top of the heap is guaranteed to be valid (covers 'q') AND the smallest!
            res[q] = minHeap[0][0] if minHeap else -1
            
        # Because we sorted our queries, we scrambled their original order.
        # We use our hash map to reconstruct the answers in the exact original order.
        return [res[q] for q in queries]