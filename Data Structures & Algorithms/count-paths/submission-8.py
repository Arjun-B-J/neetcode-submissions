class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0]*m
        for r in range(n-1,-1,-1):
            curRow = [0]*m
            for c in range(m-1,-1,-1):
                if r==n-1 and c==m-1:
                    curRow[c]=1
                else:
                    right = curRow[c+1] if c+1<m else 0
                    curRow[c] = right + prevRow[c]
            prevRow = curRow
        return prevRow[0]