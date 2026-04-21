class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        INF = 2**31-1
        ROW,COL = len(grid),len(grid[0])
        def bfs(i,j): #we do bfs here and fix the grid
            q = deque()
            q.append((i,j))
            visit = set()
            visit.add((i,j))
            distance=0
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if grid[r][c]==0:
                        grid[i][j]=distance
                        return
    
                    for dr,dc in directions:
                        nr,nc= r+dr,c+dc
                        if min(nr,nc)<0 or nr==ROW or nc==COL or (nr,nc) in visit or grid[nr][nc]==-1:
                            continue
                        visit.add((nr,nc))
                        q.append((nr,nc))
                distance+=1
        #call on all places
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==INF:
                    bfs(i,j)
    