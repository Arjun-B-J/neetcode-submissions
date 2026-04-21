class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i==len(s):
                return 1
            if i>len(s):
                return 0
            if s[i]=='0':
                return 0
            if i in cache:
                return cache[i]
            cache[i]=dfs(i+1)
            if i+1<len(s):
                if int(s[i]+s[i+1])<=26:
                    cache[i]+=dfs(i+2)
            return cache[i]
        return dfs(0)  
        