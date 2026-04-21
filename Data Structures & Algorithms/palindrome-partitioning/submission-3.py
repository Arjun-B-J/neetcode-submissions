class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True                        # every single char is a palindrome
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        def backtrack(i):
            # Base case: consumed the whole string → valid partition found
            if i == len(s):
                res.append(part.copy())
                return

            # Try every substring starting at i
            for j in range(i, len(s)):
                # Only recurse if s[i..j] is a palindrome
                if dp[i][j]:
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