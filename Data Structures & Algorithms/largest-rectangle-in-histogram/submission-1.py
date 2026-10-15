class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                curr_idx,curr_h=stack.pop()
                maxArea=max(maxArea,curr_h*(i-curr_idx))
                start=curr_idx
            stack.append([start,h])
        while stack:
            curr_idx, curr_h=stack.pop()
            maxArea=max(maxArea,curr_h*(len(heights)-curr_idx))

        return maxArea


