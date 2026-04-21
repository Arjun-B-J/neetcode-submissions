# Time Complexity: 
#   - add(): O(1)
#   - count(): O(N) where N is the number of unique points added so far.
# Space Complexity: O(N) - Storing the points in a hash map.
# Approach: Hash Map & Diagonal Identification

from collections import defaultdict
from typing import List

class CountSquares:
    def __init__(self):
        # Maps (x, y) coordinates to their frequency count
        self.pts_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # Tuples are hashable, lists are not, so we convert it
        self.pts_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        
        # Iterate through every unique point we've seen so far
        for (x, y), n in self.pts_count.items():
            
            # 1. Is this a valid diagonal point?
            # It forms a square if the x-distance equals the y-distance.
            # We also ensure x != qx and y != qy so we don't count a line/point (area must be > 0).
            if abs(qx - x) == abs(qy - y) and qx != x and qy != y:
                
                # 2. Do the other two corners exist?
                # If we have the diagonal, the other corners MUST be at (x, qy) and (qx, y)
                if (x, qy) in self.pts_count and (qx, y) in self.pts_count:
                    
                    # 3. Calculate the total ways to form this square.
                    # Multiply the frequencies of all three points!
                    res += n * self.pts_count[(x, qy)] * self.pts_count[(qx, y)]
                    
        return res