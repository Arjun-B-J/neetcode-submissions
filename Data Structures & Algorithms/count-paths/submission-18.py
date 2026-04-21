# Time Complexity: O(m * n) - We iterate through m rows and n columns.
# Space Complexity: O(n) - We maintain exactly two arrays of size n. Dropping constants yields O(n).
# Approach: Bottom-Up Dynamic Programming (Space Optimized 2-Row Array)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [1] * n                                      # Represents the row directly above the current one
        
        for _ in range(1, m):                                   # Iterate through the remaining m - 1 rows
            curr_row = [1] * n                                  # Initialize current row (leftmost col is always 1)
            
            for c in range(1, n):                               # Fill the current row from left to right
                curr_row[c] = curr_row[c - 1] + prev_row[c]     # Current cell = Paths from LEFT + Paths from ABOVE
                
            prev_row = curr_row                                 # Shift the window down: current row becomes the previous
            
        return prev_row[-1]                                     # The last element holds the total paths to the destination