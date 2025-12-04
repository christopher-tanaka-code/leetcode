# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to keep track of copied nodes: original node -> cloned node
        cloned_nodes = {}
        
        def dfs(n: 'Node') -> 'Node':
            # If node is already cloned, return the clone
            if n in cloned_nodes:
                return cloned_nodes[n]
            
            # Clone the node
            clone = Node(n.val)
            cloned_nodes[n] = clone
            
            # Recursively clone all neighbors
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
