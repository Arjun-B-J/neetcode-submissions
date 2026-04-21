class Solution: #refer video solution for image
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h: #if cur height is smaller, pop and extend backwards
                index, height = stack.pop()
                start = index
                maxArea = max(maxArea,height * (i-index))
            stack.append([start,h])

        for i,h in stack: #now those remain extend till end of heights
            maxArea = max(maxArea,h*(len(heights)-i)) #here we take len of height as it self
        return maxArea