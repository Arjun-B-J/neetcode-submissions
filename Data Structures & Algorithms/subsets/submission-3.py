class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [],[]
        n = len(nums)
        def backTrack(i):
            if i == n:
                res.append(cur[:])
                return
            #Dont pick i
            backTrack(i+1)

            #Pick i
            cur.append(nums[i])
            backTrack(i+1)
            cur.pop()
        backTrack(0)
        return res

