class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        for i in range(1,n+1):
            self.parent[i]=i
            self.rank[i] = 1
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,x,y):
        p1,p2 = self.find(x),self.find(y)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2]>self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointSet = UnionFind(len(edges))
        ans = []
        for edge in edges:
            if not disjointSet.union(edge[0],edge[1]):
                ans = edge
        return ans