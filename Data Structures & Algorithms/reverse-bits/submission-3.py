# Time Complexity: O(1) - We always loop exactly 32 times, regardless of the input size.
# Space Complexity: O(1) - Only a few integer variables are stored.
# Approach: Pure Bit Manipulation (Shift and OR)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # We must process exactly 32 bits as per the problem description
        for _ in range(32):
            # Step 1: Extract the rightmost bit of 'n'
            # (n & 1) isolates the least significant bit (0 or 1)
            bit = n & 1
            
            # Step 2: Shift our running result to the left by 1 space.
            # This makes room for the new bit we are about to insert.
            res = res << 1
            
            # Step 3: Insert the extracted bit into the newly opened space.
            # The bitwise OR (|) safely places the 1 or 0 into the last position.
            res = res | bit
            
            # Step 4: Shift 'n' to the right by 1 space to queue up the next bit.
            n = n >> 1
            
        return res