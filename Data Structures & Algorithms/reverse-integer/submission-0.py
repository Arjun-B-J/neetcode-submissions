import math
class Solution:
    def reverse(self, x: int) -> int:
        intmin, intmax = -2**31, 2**31-1
        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if res>int(intmax/10) or res == int(intmax/10) and digit>intmax%10:
                return 0
            if res<int(intmin/10) or res == int(intmin/10) and digit<intmin%10:
                return 0
            
            res = res*10+digit
        return res

