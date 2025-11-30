from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((v, 0))  # u->v is correct if root-side is u
            adj[v].append((u, 1))  # would need reversal if we want v->u

        parent = [-1] * n
        parent[0] = 0

        # 1) Compute answer[0] by rooting at 0
        ans0 = 0
        stack = [0]
        order = [0]  # nodes in a root-to-leaf traversal order

        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                ans0 += w
                stack.append(v)
                order.append(v)

        # 2) Reroot DP to compute all answers
        ans = [0] * n
        ans[0] = ans0
        stack = [0]

        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                ans[v] = ans[u] + (1 - 2 * w)
                stack.append(v)

        return ans
