class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid[0]), len(obstacleGrid)
        prevRow = [0]*m
        for r in range(n-1,-1,-1):
            curRow = [0]*m
            for c in range(m-1,-1,-1):
                if obstacleGrid[r][c]==1:
                    curRow[c]=0
                else:
                    if r==n-1 and c==m-1:
                        curRow[c]=1
                    else:
                        right = curRow[c+1] if c+1<m else 0
                        down = prevRow[c]
                        curRow[c] = right + down
            prevRow = curRow
        return prevRow[0]