# Time Complexity: O(N) worst case (e.g., [9, 9, 9]), but O(1) best case with the Early Exit!
# Space Complexity: O(1) - Modified in-place.
# Approach: Math (Carry Simulation with Early Exit)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # We start with a carry of 1 because we are "adding one"
        carry = 1
        
        # Traverse from right to left
        for i in reversed(range(len(digits))):
            total = digits[i] + carry
            
            # The current digit is the remainder (e.g., 10 % 10 = 0)
            digits[i] = total % 10
            
            # The new carry is the quotient (e.g., 10 // 10 = 1)
            carry = total // 10
            
            # OPTIMIZATION: Early Exit!
            # If the carry drops to 0, there is no more "ripple effect" to process.
            # We can instantly stop the loop and return our modified array.
            if carry == 0:
                return digits
                
        # If we exhausted the entire loop and STILL have a carry 
        # (e.g., [9, 9] became [0, 0] with carry=1), we insert it at the front.
        if carry:
            digits.insert(0, carry)
            
        return digits