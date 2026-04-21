class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curComb,res = [],[]

        def helper(i,k,curComb,res):
            
            if len(curComb)==k:
                res.append(curComb.copy())
                return
            if i>n:
                return
            #Do Combinations for i, in accending Order, 1,2 if counted need not be counted as 2,1 so skip i-1.. val for i
            for j in range(i,n+1):
                curComb.append(j)
                helper(j+1,k,curComb,res)
                curComb.pop()


        helper(1,k,curComb,res)
        return res