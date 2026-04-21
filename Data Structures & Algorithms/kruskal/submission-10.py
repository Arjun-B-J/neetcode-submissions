class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i]=i
            self.rank[i]=1

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
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minH = []
        edges.sort(key = lambda x:x[2])
        print(edges)
        uf= UnionFind(n)
        cost  = 0
        mst = []
        for u,v,w in edges:
            if uf.union(u,v):
                mst.append((u,v))
                cost+=w
        if len(mst) != n-1:
            return -1
        return cost














