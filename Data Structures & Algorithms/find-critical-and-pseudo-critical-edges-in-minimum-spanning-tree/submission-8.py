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
    
    def union(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True
    
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        mstWeight = 0
        uf = UnionFind(n)
        # to keep the original index for accumulating results
        for i,edge in enumerate(edges):
            edge.append(i) #[u v weight i]

        edges.sort(key = lambda e:e[2])

        for u,v,w,i in edges:
            if uf.union(u,v):
                mstWeight+=w
        critical,pseudo = [],[]

        for u,v,w,i in edges:
            weight = 0
            uf = UnionFind(n)
            for x,y,w2,j in edges:
                if i!=j and uf.union(x,y):
                    weight+=w2
            #since given a connceted Graph, it will be n if mst is formed
            #since dict is used , need to do max of .values()
            if weight>mstWeight or max(uf.rank.values())!=n:
                critical.append(i)
                continue
            #Check if pseudo critical
            uf = UnionFind(n)
            weight = w #initialze with this edge and see if mst
            uf.union(u,v)
            #add this and check if mst is formed, if so then pseudo
            
            for x,y,w2,j in edges:
                if uf.union(x,y):
                    weight+=w2
            #since connected , it will always be an mst since no to other restriction apart from adding an initial edge
            if weight==mstWeight:
                pseudo.append(i)

        return [critical,pseudo]















