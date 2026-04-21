class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = 0
        for i in range(0,n):
            self.parent[i]=i
            self.rank[i]=0
            self.num_components +=1

    def find(self, x: int) -> int:
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x)==self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1==p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2]+=self.rank[p1]
        self.num_components -=1
        return True

    def getNumComponents(self) -> int:
        return self.num_components












