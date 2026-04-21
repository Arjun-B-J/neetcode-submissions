from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # --- Step 1: Count the frequencies ---
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                
        # --- Step 2: Create the "Buckets" ---
        # We create a list of empty lists where the INDEX represents the frequency.
        # Why len(nums) + 1? The maximum frequency any number can have is the 
        # length of the array itself (e.g., if the array is [2, 2, 2]).
        # The + 1 accounts for 0-indexing.
        frequencies = [[] for i in range(len(nums) + 1)]
        
        # --- Step 3: Populate the Buckets ---
        # Now we map the counts to the indices. 
        # If the number '3' appears '4' times, we append '3' to frequencies[4].
        
        for num, cnt in count.items():
            frequencies[cnt].append(num)
            
        # --- Step 4: Gather the Top K Elements ---
        res = []
        
        # Since the index represents frequency, reading the 'frequencies' array 
        # backwards means we are naturally pulling from highest frequency to lowest.
        for ele in reversed(frequencies):
            # 'ele' is the list of numbers that share this specific frequency.
            for num in ele:
                res.append(num)
                # As soon as we have collected 'k' elements, we are done!
                if len(res) == k:
                    return res