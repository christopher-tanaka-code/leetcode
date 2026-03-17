class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # left -> right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # top -> bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix