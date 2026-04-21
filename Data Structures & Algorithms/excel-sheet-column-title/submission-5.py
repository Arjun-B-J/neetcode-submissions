class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            columnNumber -=1
            res= res + chr(ord('A')+columnNumber%26)
          
            columnNumber//=26
        return res[::-1]