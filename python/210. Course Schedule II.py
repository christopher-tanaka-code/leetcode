from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph and compute in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # Step 2: Initialize queue with nodes having zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []
        
        # Step 3: Process nodes
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if topological ordering is possible
        if len(order) == numCourses:
            return order
        else:
            return []  # Cycle detected, cannot finish all courses
