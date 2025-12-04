from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value      # A / B = value
            graph[B][A] = 1 / value  # B / A = 1 / value
        
        # Step 2: Define DFS function to find path product
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue
                product = dfs(neighbor, end, visited)
                if product != -1.0:
                    return val * product
            
            return -1.0
        
        # Step 3: Evaluate each query
        result = []
        for C, D in queries:
            result.append(dfs(C, D, set()))
        
        return result
