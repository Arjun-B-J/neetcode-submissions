class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,partition = [],[]

        def backtrack(i):
            if i==len(s): #if it reaches end, then it has a valid palidrome
                res.append(partition.copy())
            
            #iterate through every piece and check if palidrome , then recurse
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    partition.append(s[i:j+1])
                    backtrack(j+1)
                    partition.pop()
        backtrack(0)
        return res
    def isPalindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r = l+1,r-1
        return True