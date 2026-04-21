import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails= []
        for n in nums:
            idx = bisect.bisect_left(tails,n)
            if idx==len(tails):
                tails.append(n)
            else:
                tails[idx]=n
        return len(tails)