# Time Complexity: O(N) - In the worst case, we scan the string at most twice.
# Space Complexity: O(1) - Strictly constant space (no recursion call stack or string slicing).
# Approach: Iterative Two-Pointer with Branching

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Helper function to do a standard, strict palindrome check
        def check_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Main logic
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # MISMATCH FOUND! This is where your 'flag' logic kicks in.
                # We have exactly one chance to delete a character.
                # Branch 1: What if we delete the character at 'l'? (Skip left)
                # Branch 2: What if we delete the character at 'r'? (Skip right)
                
                # If EITHER of these remaining inner strings is a perfect palindrome, we return True!
                return check_palindrome(l + 1, r) or check_palindrome(l, r - 1)
                
        return True