from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg = defaultdict(int)
        outdeg = defaultdict(int)

        # Build graph
        for u, v in pairs:
            adj[u].append(v)
            outdeg[u] += 1
            indeg[v] += 1

        # Choose start node:
        # If an Euler trail exists, start has outdeg = indeg + 1 (if any),
        # otherwise it's an Euler circuit and we can start anywhere with outdeg > 0.
        start = pairs[0][0]
        for node in outdeg:
            if outdeg[node] - indeg[node] == 1:
                start = node
                break

        # To efficiently pop edges, we'll pop from the end of lists
        # (order doesn't matter since any valid arrangement is acceptable).
        # Optionally reverse to keep closer to input order:
        # for node in adj: adj[node].reverse()

        # Hierholzer's algorithm (iterative)
        stack = [start]
        path = []  # will store vertices in reverse order

        while stack:
            u = stack[-1]
            if adj[u]:
                v = adj[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())

        path.reverse()

        # Convert vertex path to edge list
        return [[path[i], path[i + 1]] for i in range(len(path) - 1)]
