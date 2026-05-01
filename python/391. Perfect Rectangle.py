from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")

        total_area = 0
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            total_area += (x2 - x1) * (y2 - y1)

            rect_corners = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]

            for corner in rect_corners:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        expected_area = (max_x - min_x) * (max_y - min_y)

        if total_area != expected_area:
            return False

        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        return corners == expected_corners