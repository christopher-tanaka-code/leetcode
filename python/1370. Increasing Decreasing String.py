class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        res = []
        remaining = len(s)

        while remaining > 0:
            # increasing pass
            for i in range(26):
                if freq[i] > 0:
                    res.append(chr(i + 97))
                    freq[i] -= 1
                    remaining -= 1

            # decreasing pass
            for i in range(25, -1, -1):
                if freq[i] > 0:
                    res.append(chr(i + 97))
                    freq[i] -= 1
                    remaining -= 1

        return "".join(res)
