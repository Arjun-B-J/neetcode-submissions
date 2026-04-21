# Time Complexity: O(log_26(N)) - We divide the number by 26 in each iteration.
# Space Complexity: O(log_26(N)) - For storing the resulting characters.
# Approach: Base-26 Conversion with 1-Index Offset

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 0:
            # INTERVIEW TRICK: The "- 1" is the secret to this problem!
            # Since Excel is 1-indexed (A=1, Z=26), taking a direct modulo 26 
            # would map Z (26 % 26) to 0, which breaks the logic.
            # Subtracting 1 maps A to 0 and Z to 25, allowing standard base-26 math.
            columnNumber -= 1
            
            # Extract the rightmost base-26 "digit" (0 to 25)
            remainder = columnNumber % 26
            
            # Convert that digit to an ASCII character ('A' is 65 in ASCII)
            # 0 -> 'A', 1 -> 'B', ..., 25 -> 'Z'
            char = chr(remainder + ord('A'))
            res.append(char)
            
            # Integer divide by 26 to process the next "digit"
            columnNumber //= 26
            
        # Because we extracted digits from right to left, the list is backwards.
        # We must reverse the list and join it into a string.
        return "".join(res[::-1])