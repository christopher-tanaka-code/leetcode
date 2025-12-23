from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        need = [0] * 26
        win = [0] * 26

        for ch in p:
            need[ord(ch) - 97] += 1

        # initialize first window
        for i in range(m):
            win[ord(s[i]) - 97] += 1

        matches = 0
        for i in range(26):
            if win[i] == need[i]:
                matches += 1

        res = []
        if matches == 26:
            res.append(0)

        for r in range(m, n):
            add = ord(s[r]) - 97
            rem = ord(s[r - m]) - 97

            # add new char
            if win[add] == need[add]:
                matches -= 1
            win[add] += 1
            if win[add] == need[add]:
                matches += 1

            # remove old char
            if win[rem] == need[rem]:
                matches -= 1
            win[rem] -= 1
            if win[rem] == need[rem]:
                matches += 1

            if matches == 26:
                res.append(r - m + 1)

        return res
