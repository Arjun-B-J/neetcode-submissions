class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        ans = []
        l=0
        window = set()
        for c in s:
            l+=1
            count[c]-=1
            window.add(c)
            if not count[c]:
                window.remove(c)
                if not window:
                    ans.append(l)
                    l=0
        return ans
            