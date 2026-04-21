class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        # --- Step 1: Target frequencies ---
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)    

        # --- Step 2: Setup Window Variables ---
        window = {}
        res, resLength = [-1, -1], float("inf")
        l = 0
        
        # 'need' is the number of UNIQUE characters we must match.
        # 'have' tracks how many unique characters currently meet the target frequency.
        have, need = 0, len(countT) 

        
        
        # --- Step 3: Expand the window (move 'r' right) ---
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            
            # If we just hit the exact required count for a character, increment 'have'
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # --- Step 4: Shrink the window (move 'l' right) ---
            # While the window is valid, try to make it smaller to find the minimum
            while have == need: 
                # Update our result if we found a smaller valid window
                if (r - l + 1) < resLength:
                    resLength = r - l + 1
                    res = [l, r]
                    
                # Pop the leftmost character out of the window
                left_char = s[l]
                window[left_char] -= 1
                
                # If removing this char drops us below the required count, the window becomes invalid
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                    
                l += 1 # Actually shrink the window

        # --- Step 5: Return result ---
        return s[res[0]:res[1]+1] if resLength != float("inf") else ""