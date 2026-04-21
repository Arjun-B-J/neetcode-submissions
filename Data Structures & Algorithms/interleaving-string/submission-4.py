class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        n, m = len(s1), len(s2)
        
        # 'next_row' represents row i+1. Initially it's the last row (n).
        # In the last row (i=n), we can only use s2.
        next_row = [False] * (m + 1)
        next_row[m] = True # Base case (n, m)
        
        # Fill the initial 'next_row' (base case row where i=n)
        for j in range(m - 1, -1, -1):
            if s2[j] == s3[n + j] and next_row[j + 1]:
                next_row[j] = True
        
        # Iterate s1 backwards
        for i in range(n - 1, -1, -1):
            curr_row = [False] * (m + 1)
            
            # Iterate s2 backwards
            for j in range(m, -1, -1):
                # Check s1 (Down -> next_row[j])
                if s1[i] == s3[i + j] and next_row[j]:
                    curr_row[j] = True
                
                # Check s2 (Right -> curr_row[j+1])
                # Only if not already true
                if not curr_row[j] and j < m and s2[j] == s3[i + j] and curr_row[j + 1]:
                    curr_row[j] = True
            
            next_row = curr_row
            
        return next_row[0]