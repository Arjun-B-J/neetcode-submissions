from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # --- Step 1: Create a Hash Set ---
        # Converting the list to a set gives us O(1) constant time lookups.
        # This is crucial because we will be checking if specific numbers exist 
        # over and over again.
        numSet = set(nums)
        ans = 0

        # --- Step 2: Iterate through the unique numbers ---
        for num in numSet:
            # --- Step 3: Find the START of a sequence ---
            # This is the most important line in the algorithm.
            # If (num - 1) is NOT in the set, it means 'num' has no left neighbor.
            # Therefore, 'num' MUST be the beginning of a new sequence.
            # If (num - 1) IS in the set, we skip it entirely because we only 
            # want to build sequences from their absolute starting point.
            if (num - 1) not in numSet:
                
                # 'l' will keep track of the length of the current sequence.
                # It starts at 1 because the current 'num' itself counts as 1.
                l = 1
                
                # --- Step 4: Count the sequence length ---
                # As long as the next consecutive number (num + l) exists in our set,
                # we increment our length counter.
                while (num + l) in numSet:
                    l += 1
                
                # --- Step 5: Update the maximum length ---
                # Compare the length of the sequence we just found against our 
                # running maximum, and keep the larger value.
                ans = max(l, ans)
                
        return ans