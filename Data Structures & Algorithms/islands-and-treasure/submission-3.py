class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        INF = 2**31-1
        ROW,COL = len(grid),len(grid[0])
        q = deque()
        visit = set()

        #adding to the queue all the treasure chest
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        distance = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc= dr+r,dc+c
                    if min(nr,nc)<0 or nr==ROW or nc==COL or (nr,nc) in visit or grid[nr][nc]==-1:
                        continue
                    grid[nr][nc]=distance
                    q.append((nr,nc))
                    visit.add((nr,nc))
            distance+=1