class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class UnionFind:
            def __init__(self,n):
                self.rank = {}
                self.parent = {}
                for i in range(n):
                    self.rank[i]=1
                    self.parent[i]=i

            def find(self,x):
                if x!=self.parent[x]:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
        
            def union(self,x,y):
                px,py = self.find(x),self.find(y)
                
                if px==py:
                    return False
                if self.rank[px]>self.rank[py]:
                    self.rank[px] +=self.rank[py]
                    self.parent[py]=px
                else:
                    self.rank[py] +=self.rank[px]
                    self.parent[px]=py
                print(px,py,self.rank[px],self.rank[py])
                return True

        uf = UnionFind(n)
        for x,y in edges:
            if not uf.union(x,y):
                return False

        return True if max(uf.rank.values())==n else False