from collections import deque, defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph and compute in-degrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # Initialize queue with courses having zero in-degree
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        taken_courses = 0
        
        while queue:
            course = queue.popleft()
            taken_courses += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we were able to take all courses, return True
        return taken_courses == numCourses
