class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        nums = [1] + nums + [1]
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            #k is the last ballon we pop,after poping elements left and right to it
            cache[(l,r)] = 0
            for k in range(l,r+1):
                cache[(l,r)] = max(cache[(l,r)],dfs(l,k-1) + nums[k]*nums[l-1]*nums[r+1] + dfs(k+1,r))

            return cache[(l,r)]

        return dfs(1,len(nums)-2)
            