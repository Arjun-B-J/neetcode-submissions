class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1(num):
            count=0
            while num>0:
                if num&1:
                    count+=1
                num=num>>1
            return count
        ans = []
        for i in range(n+1):
            ans.append(count1(i))
        return ans


        