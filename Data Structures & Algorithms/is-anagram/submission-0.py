from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        for ele in t:
            if ele not in s:
                return False
            s[ele]-=1
        for key in s:
            if s[key]>0:
                return False

        return True
        