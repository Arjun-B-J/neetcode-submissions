class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0]*26
        for c in s1:
            count[ord(c)-ord('a')]+=1
        tupleC = tuple(count)
        l,r = 0,len(s1)-1
        permCount = [0]*26
        if len(s2)<len(s1):
            return False
        for c in s2[l:r+1]:
            permCount[ord(c)-ord('a')]+=1
        while r<len(s2):
            if tuple(permCount)==tupleC:
                return True
            permCount[ord(s2[l])-ord('a')]-=1
            l+=1
            r+=1
            if r < len(s2):
                permCount[ord(s2[r])-ord('a')]+=1
        return False