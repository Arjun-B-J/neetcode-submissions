import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        ROW,COL = len(grid)-1,len(grid[0])-1
        heapq.heappush(minHeap,(grid[0][0],0,0))
        visit = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        while minHeap:
            w1,r1,c1 = heapq.heappop(minHeap)
            if (r1,c1) == (ROW,COL):
                return w1
            if (r1,c1) in visit:
                continue
            visit.add((r1,c1))

            for dr,dc in directions:
                rN = r1+dr
                cN = c1+dc
                if min(rN,cN)<0 or rN>ROW or cN>COL or (rN,cN) in visit:
                    continue
                heapq.heappush(minHeap,(max(w1,grid[rN][cN]),rN,cN))