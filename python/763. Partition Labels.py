from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last occurrence of each character
        last = {ch: i for i, ch in enumerate(s)}

        res: List[int] = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res
