class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        maxArea = 0
        rl,cl = len(grid),len(grid[0])
        def dfs(r,c):
            if min(r,c)<0 or r==rl or c==cl or grid[r][c]==0:
                return
            grid[r][c]=0
            curArea.append(1)
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]==1:
                    curArea = []
                    dfs(i,j)
                    maxArea = max(maxArea,len(curArea))
        return maxArea
