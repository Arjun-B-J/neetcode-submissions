class DisjointSet:
    def __init__(self,n):
        self.size = {}
        self.parent = {}
        self.connectedComponents = 0
        for i in range(n):
            self.parent[i]=i
            self.size[i] = 1
            self.connectedComponents+=1

    def findParent(self,node):
        while self.parent[node]!=node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self,edge):
        a,b = edge
        p1,p2 = self.findParent(a),self.findParent(b)
        if p1!=p2:
            if self.size[p1] < self.size[p2]:
                self.parent[p1] = p2
            elif self.size[p2] < self.size[p1]:
                self.parent[p2] = p1
            else:
                self.parent[p2]=p1
                self.size[p1]+=self.size[p2]
            self.connectedComponents-=1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = DisjointSet(n)
        for edge in edges:
            disjointSet.union(edge)
        return disjointSet.connectedComponents

        