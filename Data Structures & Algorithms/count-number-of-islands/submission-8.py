class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl,cl = len(grid),len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0
        def dfs(r,c):
            if min(r,c)<0 or r==rl or c==cl or grid[r][c]=="0":
                return
            grid[r][c]="0"
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1
        return islands

