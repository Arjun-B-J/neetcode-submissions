# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if pairs is None or len(pairs)==0:
            return pairs
        ans = []
        for i in range(1,len(pairs)):
            j = i-1
            ans.append(pairs.copy())
            while(j>=0 and pairs[j+1].key < pairs[j].key):
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j-=1
        ans.append(pairs.copy())
        return ans

        