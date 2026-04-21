from collections import Counter
class Solution:
    def checkCounts(self,c1,c2):
        for ele,val in c1.items():
            if ele not in c2:
                return False
            if c2[ele]!=val:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l,r = 0,len(s1)
        while r<=len(s2):
            if self.checkCounts(c1,Counter(s2[l:r])):
                return True
            r+=1
            l+=1
        return False