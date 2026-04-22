from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque(i for i in range(n) if len(graph[i]) == 1)
        remaining_nodes = n

        while remaining_nodes > 2:
            leaf_count = len(leaves)
            remaining_nodes -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)