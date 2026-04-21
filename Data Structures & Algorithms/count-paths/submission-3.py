class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0]*m
        for r in range(n-1,-1,-1):
            curRow = [0]*m
            curRow[m-1] = 1
            for c in range(m-2,-1,-1):
                curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]