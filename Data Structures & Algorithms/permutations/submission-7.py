class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        hashMap = Counter(nums)
        res= []
        cur = []
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())

            for n in hashMap:
                if hashMap[n]>0:
                    hashMap[n]-=1
                    cur.append(n)
                    
                    dfs()
                    
                    hashMap[n]+=1
                    cur.pop()
        dfs()
        return res 