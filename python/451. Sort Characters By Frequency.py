from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        chars = sorted(count.keys(), key=lambda ch: count[ch], reverse=True)

        result = []

        for ch in chars:
            result.append(ch * count[ch])

        return "".join(result)