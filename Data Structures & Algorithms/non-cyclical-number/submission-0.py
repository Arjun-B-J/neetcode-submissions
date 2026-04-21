class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        def getSquare(n):
            l = list(map(int, str(n)))
            ans =0
            for ele in l:
                ans+=ele**2
            return ans
        while True:
            square = getSquare(n)
            print(square)
            if square==1:
                return True
            if square in seen:
                return False
            seen[square]=True
            n=square
        