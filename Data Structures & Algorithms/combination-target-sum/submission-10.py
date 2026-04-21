class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,cur = [],[]
        n = len(nums)
        def backTrack(i,cur,total):
            if total == target:
                res.append(cur[:])
                return
            if i>=n or total > target:
                return
            #pick the i
            cur.append(nums[i])
            backTrack(i,cur,total+nums[i])
            cur.pop()
            #Dont pick the i
            backTrack(i+1,cur,total)
            
        backTrack(0,cur,0)
        return res