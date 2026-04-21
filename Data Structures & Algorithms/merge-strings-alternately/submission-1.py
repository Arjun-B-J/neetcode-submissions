# Time Complexity: O(M + N) - We visit each character exactly once.
# Space Complexity: O(M + N) - We use an array of size M+N to build the result.
# Approach: Two Pointers (List Append & Join)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # INTERVIEW TIP: Always use an array/list for building strings in Python!
        res = []
        
        i, j = 0, 0
        w1, w2 = len(word1), len(word2)
        
        # We don't need 'k' to track turns! 
        # Just grab one from each string sequentially in the same loop cycle.
        while i < w1 and j < w2:
            res.append(word1[i])
            res.append(word2[j])
            
            i += 1
            j += 1
            
        # The loop breaks when one of the strings runs out.
        # Python slicing safely handles appending the remainder of the longer string.
        # (If i == w1, word1[i:] is safely just an empty string "")
        res.append(word1[i:])
        res.append(word2[j:])
        
        # Join the array into a final string in O(N) time
        return "".join(res)