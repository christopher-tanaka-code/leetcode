class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D mid back into 2D indices
            r = mid // n
            c = mid % n
            value = matrix[r][c]
            
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
