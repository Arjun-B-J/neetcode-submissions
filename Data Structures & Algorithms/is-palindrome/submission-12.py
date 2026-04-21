class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(s.strip().lower().split())
        L,R = 0,len(s)-1
        while(L<R):
            if not (('a' <= s[L] <= 'z') or ('0' <= s[L] <= '9')):
                L+=1
                continue
            if not (('a' <= s[R] <= 'z') or ('0' <= s[R] <= '9')):
                R-=1
                continue
            if s[L]!=s[R]:
                return False
            L+=1
            R-=1
        return True
        