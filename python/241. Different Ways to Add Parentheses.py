from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def solve(expr: str) -> List[int]:
            results = []

            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i + 1:])

                    for a in left_results:
                        for b in right_results:
                            if ch == "+":
                                results.append(a + b)
                            elif ch == "-":
                                results.append(a - b)
                            else:  # ch == "*"
                                results.append(a * b)

            if not results:
                results.append(int(expr))

            return results

        return solve(expression)