class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1),len(str2)
        def isDivisior(l):
            if l1%l != 0 or l2%l!=0:
                return False
            return str1[:l]*(l1//l) == str1 and str1[:l]*(l2//l) == str2
        for l in range(min(l1,l2),0,-1):
            if isDivisior(l):
                return str1[:l]
        return ""