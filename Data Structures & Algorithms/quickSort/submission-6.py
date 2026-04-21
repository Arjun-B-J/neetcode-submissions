# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def qS(self,pairs,s,e):
        if e-s+1 <=1:
            return pairs
        left = s
        pivot = pairs[e]

        for i in range(s,e):
            if pivot.key > pairs[i].key:
                pairs[i],pairs[left] = pairs[left],pairs[i]
                left+=1
        pairs[e],pairs[left] = pairs[left],pairs[e]
        self.qS(pairs,s,left-1)
        self.qS(pairs,left+1,e)
        return pairs
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if pairs is None or len(pairs)==0:
            return pairs
        self.qS(pairs,0,len(pairs)-1)
        return pairs
        