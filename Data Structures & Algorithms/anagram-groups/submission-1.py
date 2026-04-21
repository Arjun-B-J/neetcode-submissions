from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = {}
        for ele in strs:
            c = Counter(ele)
            result = "".join(k+str(v) for k,v in sorted(c.items()))
            if result not in anagramList:
                anagramList[result]=[]
                anagramList[result].append(ele)
            else:
               anagramList[result].append(ele) 
        ans = []
        for k,v in anagramList.items():
            ans.append(v)
        return ans