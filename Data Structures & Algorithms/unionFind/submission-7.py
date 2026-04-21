class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        for i in range(0,n):
            self.parent[i]=i
            self.rank[i]=0

    def find(self, x: int) -> int:
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1==p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2]+=1
        return True

    def getNumComponents(self) -> int:
        ans=0
        for key in self.parent:
            if self.parent[key] == key:
                ans+=1
        return ans












