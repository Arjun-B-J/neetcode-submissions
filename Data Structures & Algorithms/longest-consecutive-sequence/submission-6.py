class DisjointSet:
    def __init__(self,nums):
        self.size = {}
        self.parent = {}
        self.maxL = 1
        for ele in nums:
            self.parent[ele]=ele
            self.size[ele] = 1

    def findParent(self,node):
        while self.parent[node]!=node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self,a,b):
        p1,p2 = self.findParent(a),self.findParent(b)
        if p1!=p2:
            if self.size[p1] < self.size[p2]:
                self.parent[p1] = p2
                self.size[p2]+=self.size[p1]
                self.maxL = max(self.size[p2],self.maxL)
            else:
                self.parent[p2] = p1
                self.size[p1]+=self.size[p2]
                self.maxL = max(self.size[p1],self.maxL)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uf = DisjointSet(nums)
        hashMap = {}
        for ele in nums:
            if ele not in hashMap:
                hashMap[ele]=1
            if ele-1 in hashMap:
                uf.union(ele-1,ele)
            if ele+1 in hashMap:
                uf.union(ele+1,ele)
        return uf.maxL







        