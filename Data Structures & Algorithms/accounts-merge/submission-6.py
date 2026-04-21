from collections import defaultdict
class UnionFind:
    def __init__(self,n):
        self.size = {}
        self.parent={}
        for i in range(n):
            self.size[i]=1
            self.parent[i]=i
    def findParent(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,x,y):
        p1,p2 = self.findParent(x),self.findParent(y)
        if p1!=p2:
            if self.size[p1]>self.size[p2]:
                self.size[p1]+=self.size[p2]
                self.parent[p2] = p1
            else:
                self.size[p2]+=self.size[p1]
                self.parent[p1] = p2
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailGroup = defaultdict(list)
        res = []
        emailHash = {}

        #build email hash and DJS for account indexes
        for accountIndex,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailHash:
                    uf.union(accountIndex,emailHash[email])
                else:
                    emailHash[email] = accountIndex
        #Build Email List per account
        for email, accountIndex in emailHash.items():
            parent = uf.findParent(accountIndex)
            emailGroup[parent].append(email)
        #Build Result
        for parent, emailList in emailGroup.items():
            res.append([accounts[parent][0]] + sorted(emailList))
        return res


        