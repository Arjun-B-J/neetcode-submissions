class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0]*m
        for c in range(n-1,-1,-1):
            curRow = [0]*m
            curRow[m-1] = 1
            for r in range(m-2,-1,-1):
                curRow[r] = curRow[r+1] + prevRow[r]
            prevRow = curRow
        return prevRow[0]