from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Sort in reverse lexical order so we can pop the smallest destination
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        route = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            route.append(airport)

        dfs("JFK")

        return route[::-1]