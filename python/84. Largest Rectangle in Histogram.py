from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices of increasing heights
        max_area = 0
        heights.append(0)  # sentinel to pop everything at the end

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                mid = stack.pop()
                height = heights[mid]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # restore input (optional)
        return max_area
