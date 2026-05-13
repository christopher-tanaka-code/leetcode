from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        ans = []

        for word in words:
            lower = set(word.lower())

            for row in rows:
                if lower <= row:
                    ans.append(word)
                    break

        return ans