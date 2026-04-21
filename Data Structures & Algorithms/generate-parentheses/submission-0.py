class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,stack = [],[]
        def backtrack(openN,closeN):
            #base is when open and close is equals to n
            if openN==closeN==n:
                res.append("".join(stack))
            #we can only add an open if its less than n
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closeN)
                stack.pop()
            #we can only add an close if its less than open
            if closeN<openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()

        backtrack(0,0)
        return res