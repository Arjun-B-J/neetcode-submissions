class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb = []
        res = []

        def helper(i,k,curComb,res):
            if len(curComb)==k:
                res.append(curComb.copy())
                return
            
            if i>n:
                return
            
            #Pick i
            curComb.append(i)
            helper(i+1,k,curComb,res)
            curComb.pop()

            #Dont Pick i
            helper(i+1,k,curComb,res)
        
        helper(1,k,curComb,res)
        return res