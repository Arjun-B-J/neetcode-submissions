class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 1
        L=0
        visit = set()
        if len(s)<=1:
            return len(s)
        visit.add(s[0])
        for R in range(1,len(s)):
            if s[R] not in visit:
                visit.add(s[R])
                ans = max(ans,R-L+1)
            else:
                while s[R] in visit:
                    visit.remove(s[L])
                    L+=1
                visit.add(s[R])
        return ans
        