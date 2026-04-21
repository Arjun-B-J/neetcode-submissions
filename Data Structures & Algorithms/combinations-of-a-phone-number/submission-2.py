class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        charToStr = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []
        l = len(digits)
        def helper(i,curStr):
            if len(curStr)==l:
                res.append(curStr)
                return
            
            for c in charToStr[digits[i]]:
                helper(i+1,curStr+c)
        
        if digits:
            helper(0,"")

        return res

        