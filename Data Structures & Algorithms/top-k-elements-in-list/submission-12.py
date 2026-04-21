class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1
        frequencies = [[] for i in range(len(nums)+1)]
        for num,cnt in count.items():
            frequencies[cnt].append(num)
        res = []
        for ele in reversed(frequencies):
            for num in ele:
                res.append(num)
                if len(res) ==k:
                    return res