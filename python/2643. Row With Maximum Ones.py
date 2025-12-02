from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        best_row = 0
        best_count = -1

        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > best_count:          # strictly greater keeps smallest index on ties
                best_count = cnt
                best_row = i

        return [best_row, best_count]
