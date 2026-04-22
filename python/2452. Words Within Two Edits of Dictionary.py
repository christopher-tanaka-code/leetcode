from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def within_two_edits(a: str, b: str) -> bool:
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        result = []

        for query in queries:
            for word in dictionary:
                if within_two_edits(query, word):
                    result.append(query)
                    break

        return result