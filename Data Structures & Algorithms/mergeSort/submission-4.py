# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self,pairs,s,m,e):
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]

        i= 0
        j= 0
        k = s
        while(i<len(L) and j<len(R)):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i +=1
            else:
                pairs[k] = R[j]
                j+=1
            k+=1
        while(i<len(L)):
            pairs[k] = L[i]
            i+=1
            k+=1
        while(j<len(R)):
            pairs[k]=R[j]
            j+=1
            k+=1

    def mS(self,pairs,s,e):
        if e-s+1 <= 1:
            return pairs
        m = ( s + e ) // 2
        self.mS(pairs,s,m)
        self.mS(pairs,m+1,e)
        self.merge(pairs,s,m,e)
        return pairs


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if pairs is None or len(pairs) == 0:
            return pairs
        return self.mS(pairs,0,len(pairs)-1)

