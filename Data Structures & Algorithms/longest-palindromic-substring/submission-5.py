class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        mL = -1
        mR = -1
        for i in range(len(s)):
            #do for odd
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxLength:
                    maxLength = r-l+1
                    mL = l
                    mR = r
                l-=1
                r+=1
            #do for even
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxLength:
                    maxLength = r-l+1
                    mL = l
                    mR = r
                l-=1
                r+=1
        return s[mL:mR+1]