from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram for current row
            for c in range(cols):
                if row[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Compute largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices
        max_area = 0
        extended = heights + [0]  # sentinel to flush stack at the end

        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]
                left_boundary = stack[-1] if stack else -1
                width = i - left_boundary - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area