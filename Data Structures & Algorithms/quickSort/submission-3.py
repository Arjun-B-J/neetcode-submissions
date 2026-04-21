# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def qS(self,pairs,s,e):
        if e-s+1 <= 1:
            return pairs
        pivot = pairs[e]
        left = s
        for i in range(s,e):
            if(pivot.key > pairs[i].key):
                pairs[left],pairs[i] = pairs[i],pairs[left]
                left+=1
        
        pairs[e],pairs[left] = pairs[left],pivot
        self.qS(pairs,s,left-1)
        self.qS(pairs,left+1,e)
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if pairs is None or len(pairs)==0:
            return pairs
        self.qS(pairs,0,len(pairs)-1)
        return pairs
        