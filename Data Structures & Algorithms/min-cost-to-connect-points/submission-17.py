import heapq
class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i]=i
            self.rank[i]=0

    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self,x,y) -> bool:
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p1]+=self.rank[p2]
        return True



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        minH = []
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minH,(dist,i,j))

        mst = []
        cost = 0
        uf = UnionFind(N)
        while minH:
            w,u,v = heapq.heappop(minH)
            if not uf.union(u,v):
                continue
            mst.append((u,v))
            cost+=w
        if len(mst) != N-1:
            return -1
        return cost

