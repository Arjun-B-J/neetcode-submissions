class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        i = abs(n)
        if n<0:
            x=1/x
        while i:
            res*=x
            i-=1
        return res 