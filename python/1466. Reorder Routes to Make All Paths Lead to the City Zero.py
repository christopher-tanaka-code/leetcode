from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Build a graph with direction info
        # If we can go from u -> v in original, store v in graph[u] with a flag 1
        # If we can go from v -> u in original, store u in graph[v] with a flag 0 (no change needed)
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # original direction u -> v
            graph[v].append((u, 0))  # reverse direction v -> u (no change needed)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            changes = 0
            for nei, cost in graph[node]:
                if not visited[nei]:
                    changes += cost  # cost=1 means we need to reverse this edge
                    changes += dfs(nei)
            return changes

        return dfs(0)
