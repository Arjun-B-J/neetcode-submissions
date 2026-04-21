class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid,r,c,visit):
            rows,cols = len(grid),len(grid[0])
            if min(r,c)<0 or r==rows or c==cols or (r,c) in visit or grid[r][c]==1:
                return 0
            if r==rows-1 and c==cols-1:
                return 1
            
            counts=0
            visit.add((r,c))
            counts+=dfs(grid,r+1,c,visit)
            counts+=dfs(grid,r,c+1,visit)
            counts+=dfs(grid,r-1,c,visit)
            counts+=dfs(grid,r,c-1,visit)

            visit.remove((r,c))
            return counts
        return dfs(grid,0,0,set())    
        