class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(i):
            # Base case: consumed the whole string → valid partition found
            if i == len(s):
                res.append(part.copy())
                return

            # Try every substring starting at i
            for j in range(i, len(s)):
                # Only recurse if s[i..j] is a palindrome
                if isPalin(s, i, j):
                    part.append(s[i:j+1])   # choose this slice
                    backtrack(j + 1)         # recurse on the remainder
                    part.pop()               # undo (backtrack)

        def isPalin(s, l, r):
            # Two-pointer palindrome check — O(n) but called many times
            # Can be optimised to O(1) with DP pre-computation (see below)
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        backtrack(0)
        return res