class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in count:
            if count[ch] < k:
                answer = 0

                for part in s.split(ch):
                    answer = max(answer, self.longestSubstring(part, k))

                return answer

        return len(s)