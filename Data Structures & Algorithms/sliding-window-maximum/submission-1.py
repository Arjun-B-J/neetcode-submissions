#monotonically decreasing queue
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l,r = 0,0
        ans = []
        for r in range(len(nums)):
            #if top is less than the ele to be inserted, we remove it cause we dont need it
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)
            #if the l > first ele in q, the window is shifted
            if l>q[0]:
                q.popleft()
            if r+1>=k: # window has reached k
                ans.append(nums[q[0]])
                l+=1 #move l only after window reaches size k
            #r moves everytime
            r+=1

        return ans