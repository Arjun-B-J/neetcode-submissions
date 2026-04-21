# Time Complexity: O(N) - Single pass through the string.
# Space Complexity: O(1) - Only tracking two integer variables.
# Approach: Greedy Range Tracking

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else: # c == '*'
                leftMin -= 1 # Try treating '*' as ')'
                leftMax += 1 # Try treating '*' as '('
                
            # If our absolute MAXIMUM possible open parentheses dips below 0,
            # it means we have way too many ')' and not enough '(' or '*' to save us.
            if leftMax < 0:
                return False
                
            # If our MINIMUM drops below 0, it just means treating a past '*' as a ')' 
            # was a bad choice. We can just treat it as an empty string instead, 
            # effectively resetting our minimum required open parentheses to 0.
            if leftMin < 0:
                leftMin = 0
                
        # If it's possible to end up with exactly 0 open parentheses, the string is valid. else there are some (( left
        return leftMin == 0