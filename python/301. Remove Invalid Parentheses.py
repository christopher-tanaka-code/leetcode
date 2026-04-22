from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(expr: str) -> bool:
            balance = 0
            for ch in expr:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        result = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            cur = queue.popleft()

            if is_valid(cur):
                result.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue

                nxt = cur[:i] + cur[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result