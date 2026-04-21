#monotonically decreasing stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]: #if the top is small, pop till its equal or smaller than cur ele
                prevIndex, prevTemp = stack.pop() 
                ans[prevIndex] = i-prevIndex
            stack.append([i,t])
        return ans