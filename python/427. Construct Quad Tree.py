# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def build(x0, y0, length):
            # Check if all values in the subgrid are the same
            val = grid[x0][y0]
            isLeaf = True
            for i in range(x0, x0 + length):
                for j in range(y0, y0 + length):
                    if grid[i][j] != val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break
            
            if isLeaf:
                # Leaf node
                return Node(val == 1, True)
            
            # Internal node: divide into four quadrants
            half = length // 2
            topLeft = build(x0, y0, half)
            topRight = build(x0, y0 + half, half)
            bottomLeft = build(x0 + half, y0, half)
            bottomRight = build(x0 + half, y0 + half, half)
            
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)
        return build(0, 0, n)
