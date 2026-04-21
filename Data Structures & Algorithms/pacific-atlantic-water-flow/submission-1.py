class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        atlantic = set() #who all can reach atlantic
        pacific = set() #who all can reach pacific

        qP = deque()
        qA = deque()
        ROW,COL = len(heights),len(heights[0])
        for i in range(ROW): #adding the pacific and atlantic ocean nearby islands
            pacific.add((i,0))
            qP.append((i,0))

            atlantic.add((i,COL-1))
            qA.append((i,COL-1))
        
        for i in range(COL):
            pacific.add((0,i))
            qP.append((0,i))

            atlantic.add((ROW-1,i))
            qA.append((ROW-1,i))
        
        while qP: #who all can reach pacific
            r,c = qP.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if min(nr,nc)<0 or nr==ROW or nc==COL or (nr,nc) in pacific or heights[nr][nc]<heights[r][c]:
                    continue
                pacific.add((nr,nc))
                qP.append((nr,nc))

        while qA: #who all can reach atlantic
            r,c = qA.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if min(nr,nc)<0 or nr==ROW or nc==COL or (nr,nc) in atlantic or heights[nr][nc]<heights[r][c]:
                    continue
                atlantic.add((nr,nc))
                qA.append((nr,nc))
        
        #find intersection as result
        ans = []
        for i in range(ROW):
            for j in range(COL):
                if (i,j) in atlantic and (i,j) in pacific:
                    ans.append([i,j])

        return ans