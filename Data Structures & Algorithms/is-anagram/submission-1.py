class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit: if lengths don't match, they can't be anagrams.
        # (This is a great optimization to add to any solution!)
        if len(s) != len(t):
            return False
            
        # Create an array of 26 zeros for the 26 alphabet letters
        counts = [0] * 26
        
        # Increment for characters in 's', decrement for characters in 't'
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # If they are anagrams, every index will be back to 0
        for val in counts:
            if val != 0:
                return False
                
        return True