class Solution:
    def isPalindrome(self, s: str) -> bool:
        L,R = 0,len(s)-1
        s = s.lower()
        while(L<R):
            if not s[L].isalnum():
                L+=1
                continue
            if not s[R].isalnum():
                R-=1
                continue
            if s[L]!=s[R]:
                return False
            L+=1
            R-=1
        return True
        