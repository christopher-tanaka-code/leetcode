class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []

        for ch in s:
            if ch != '-':
                chars.append(ch.upper())

        first = len(chars) % k
        ans = []

        if first:
            ans.append(''.join(chars[:first]))

        for i in range(first, len(chars), k):
            ans.append(''.join(chars[i:i + k]))

        return '-'.join(ans)