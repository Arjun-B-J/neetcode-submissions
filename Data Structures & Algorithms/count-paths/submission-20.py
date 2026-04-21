# Time Complexity: O(m * n) - We iterate through m rows and n columns.
# Space Complexity: O(n) - We maintain exactly two arrays of size n.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 2-Row Array - Backwards Traversal)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        next_row = [1] * n                                      # Represents the row directly BELOW the current one
        
        for _ in range(m - 1):                                  # Iterate through the remaining m - 1 rows moving UP
            curr_row = [1] * n                                  # Initialize current row (rightmost col is always 1)
            
            for c in range(n - 2, -1, -1):                      # Fill the current row from RIGHT to LEFT
                curr_row[c] = curr_row[c + 1] + next_row[c]     # Current cell = move RIGHT + move DOWN
                
            next_row = curr_row                                 # Shift window UP: current row becomes the row below the next iteration
            
        return next_row[0]                                      # The first element holds the total paths from (0,0)