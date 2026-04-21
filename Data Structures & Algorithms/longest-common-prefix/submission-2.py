# Time Complexity: O(S) - Where S is the sum of all characters in all strings. 
#                  In the worst case, we check every character.
# Space Complexity: O(1) - We only return a slice of the original string.
# Approach: Vertical Scanning (Column by Column)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: Empty array
        if not strs:
            return ""
            
        # We only need to loop through the indices of the very first string.
        # It acts as our "baseline" reference.
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this exact column (i) across all other strings
            for s in strs:
                # BREAK CONDITION 1: The current string 's' is too short! 
                # (e.g., we are checking index 4, but 's' is "flow" which only has indices 0-3)
                # BREAK CONDITION 2: The character doesn't match!
                if i == len(s) or s[i] != char:
                    
                    # We hit a dead end. Return the baseline string exactly up to 'i'.
                    # Python slicing [0:i] naturally excludes the mismatched character at 'i'.
                    return strs[0][:i]
                    
        # If we successfully make it through the entire baseline string without breaking,
        # it means the ENTIRE first string is the common prefix!
        return strs[0]