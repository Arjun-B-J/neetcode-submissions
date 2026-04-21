class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Track frequencies of chars in s1 and the current window in s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # 'matches' tracks how many letters (out of 26) have identical frequencies
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        
        l = 0
        # Slide the window across s2
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # --- Add new character from the right ---
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before we added 1, we just broke a match
            elif s1Count[index] + 1 == s2Count[index]: 
                matches -= 1

            # --- Remove old character from the left ---
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If it was equal before we subtracted 1, we just broke a match
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
                
            l += 1
            
        # Final check for the last window position
        return matches == 26