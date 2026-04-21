class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i,j):
            if i>=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            
            match = i<len(s) and s[i]==p[j] or p[j]=='.'
            if i<=len(s) and j+1<len(p) and p[j+1]=='*': #deal with *
                cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j)) #dont use or use
                return cache[(i,j)]
            if match:
                cache[(i,j)]= dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)]= False
            return cache[(i,j)]
        return dfs(0,0)
                