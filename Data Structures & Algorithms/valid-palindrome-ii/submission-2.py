class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(i,j,flag):
            print(i,j,flag)
            if i>=j:
                return True
            if s[i]==s[j]:
                return dfs(i+1,j-1,flag)
            else:
                if not flag:
                    return False
                return dfs(i+1,j,False) or dfs(i,j-1,False)

        return dfs(0,len(s)-1,True)
