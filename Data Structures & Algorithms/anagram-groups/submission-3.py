from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) creates a dictionary where if a key doesn't exist, 
        # it automatically creates an empty list for us to append to.
        # This saves us from having to write: if key not in res: res[key] = []
        res = defaultdict(list)
        
        # Process every string in the input list one by one
        for string in strs:
            # Create a frequency array of 26 zeros, one for each lowercase English letter.
            # This array will act as our unique "signature" for anagrams.
            count = [0] * 26
            
            # Count the occurrences of each character in the current string
            for c in string:
                # ord(c) gets the ASCII value of the character.
                # Subtracting ord('a') maps 'a' to index 0, 'b' to 1, ..., 'z' to 25.
                count[ord(c) - ord('a')] += 1
            
            # Lists are mutable, so they cannot be used as dictionary keys in Python.
            # We must convert 'count' to a tuple (which is immutable) to hash it.
            # Then, we append the original string to the list of its matching signature.
            res[tuple(count)].append(string)
            
        # res.values() gives us all the grouped lists.
        # We wrap it in list() to match the expected return type: List[List[str]]
        return list(res.values())