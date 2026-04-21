class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        prefixSum = {0:1}
        ans = 0
        for ele in nums:
            curSum+=ele
            ans+=prefixSum.get(curSum-k,0)
            prefixSum[curSum] = prefixSum.get(curSum,0) + 1
        return ans