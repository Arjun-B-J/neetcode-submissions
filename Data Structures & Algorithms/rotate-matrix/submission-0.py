# Time Complexity: O(N^2) - We visit every cell exactly once.
# Space Complexity: O(1) - We only use a 'temp' variable to swap in-place.
# Approach: Layer-by-Layer 4-Way Swap

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Left and right boundaries for our concentric squares
        l, r = 0, len(matrix) - 1
        
        while l < r:
            top, bottom = l, r
            
            # We iterate through the current layer. 
            # Note: We don't do the last element, because it's the start of the next side!
            for i in range(r - l):
                
                # Save the Top-Left value
                temp = matrix[top][l + i]
                
                # Move Bottom-Left into Top-Left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # Move Bottom-Right into Bottom-Left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # Move Top-Right into Bottom-Right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # Move saved Top-Left (temp) into Top-Right
                matrix[top + i][r] = temp
                
            # Move to the inner concentric square
            l += 1
            r -= 1