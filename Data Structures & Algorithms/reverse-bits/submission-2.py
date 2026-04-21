class Solution:
    def reverseBits(self, n: int) -> int:
        rN =0
        power = 31
        while n>0:
            bit = n&1
            rN += 2**power * bit
            power-=1
            n = n>>1

        return rN

        