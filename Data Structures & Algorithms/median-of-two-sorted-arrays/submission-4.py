from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        # We always want to run binary search on the smaller array.
        # This keeps our time complexity strictly at O(log(min(n, m))).
        if len(A) > len(B):
            A, B = B, A 
            
        total = len(A) + len(B)
        
        # 'half' represents exactly how many elements should be in the left 
        # partition of our combined imaginary array.
        half = total // 2 
        
        # Set up the binary search pointers for array A
        l, r = 0, len(A) - 1

        while True:
            # 'i' is the rightmost index of the left partition in array A
            i = (l + r) // 2
            
            # 'j' is the rightmost index of the left partition in array B
            # Why (half - i - 2)? 
            # Because the number of elements we take from A is (i + 1)
            # and the number from B is (j + 1). 
            # (i + 1) + (j + 1) = half  =>  j = half - i - 2
            j = half - i - 2
            
            # --- Gather the four values bordering our partition line ---
            # If our partition completely excludes one side of an array, 
            # we use -infinity or +infinity so the comparisons below don't break.
            Aleft = A[i] if i >= 0 else float("-inf") 
            Aright = A[i+1] if (i + 1) < len(A) else float("inf") 
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j + 1) < len(B) else float("inf")

            # --- Check if we found the correct partition ---
            # For the partition to be correct, EVERY element on the left must be 
            # <= EVERY element on the right. We check the diagonals:
            # (Note: I corrected Bleft <= Bright to Bleft <= Aright here)
            if Aleft <= Bright and Bleft <= Aright:
                
                # If the total number of elements is odd, the median sits alone 
                # in the right partition. We take the smallest value on the right.
                if total % 2 == 1:
                    return min(Bright, Aright)
                
                # If the total is even, the median is the average of the largest 
                # value on the left and the smallest value on the right.
                else:
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            
            # --- Adjust the binary search range ---
            # If A's left side is strictly greater than B's right side, 
            # our partition in A is too far to the right. Move left.
            elif Aleft > Bright:
                r = i - 1
                
            # Otherwise, B's left side is greater than A's right side, meaning 
            # our partition in A is too far to the left. Move right.
            else:
                l = i + 1