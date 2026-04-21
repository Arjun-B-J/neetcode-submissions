class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,cur = [],[]
        candidates.sort() #sort the candidates such that i can skip dups
        def backtrack(i,total):
            if total == target: #should be first cause , if last element is added, then it should check this before next exit
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            #pick
            cur.append(candidates[i])
            backtrack(i+1,candidates[i]+total)
            cur.pop()

            #dont pick
            while i+1<len(candidates) and candidates[i]==candidates[i+1]: #skip dups
                i=i+1
            backtrack(i+1,total)
        
        backtrack(0,0)
        return res