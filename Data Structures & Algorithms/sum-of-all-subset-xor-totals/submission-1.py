class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        cur=[]
        def dfs(i):
            if i==len(nums):
                subsets.append(cur.copy())
                return
            #pick i
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()

            #dont pick i
            dfs(i+1)

        dfs(0)
        ans = 0
        for subset in subsets:
            temp = 0
            for ele in subset:
                temp = temp^ele
            ans+=temp

        return ans



        