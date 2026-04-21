class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions,maxArea,rl,cl = [(0,1),(1,0),(0,-1),(-1,0)],0,len(grid),len(grid[0])
        def dfs(r,c):
            if min(r,c)<0 or r==rl or c==cl or grid[r][c]==0:
                return 0
            grid[r][c],curArea=0,1
            for dr,dc in directions:
                curArea+=dfs(r+dr,c+dc)
            return curArea
        for i in range(rl):
            for j in range(cl):
                if grid[i][j]==1:
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea
