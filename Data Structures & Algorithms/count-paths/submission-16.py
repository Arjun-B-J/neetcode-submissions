# Time Complexity: O(m * n) - We still process the equivalent of every cell in the grid.
# Space Complexity: O(n) - We only store a single row, drastically reducing the memory footprint.
# Approach: Bottom-Up Dynamic Programming (Space Optimized 1D Array)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n                                           # Represents the paths for the row currently being processed
        
        for i in range(1, m):                                   # Iterate through the grid row by row
            for j in range(1, n):                               # Leftmost column (j=0) is always 1, so we skip it
                
                # In-place update: 
                # row[j] before the update is the value from ABOVE.
                # row[j-1] is the newly updated value from the LEFT.
                row[j] = row[j] + row[j - 1]                    
                
        return row[-1]                                          # The last element holds the total paths to the destination