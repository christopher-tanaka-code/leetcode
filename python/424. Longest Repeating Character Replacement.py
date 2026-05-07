class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        answer = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - ord("A")
            count[idx] += 1

            max_freq = max(max_freq, count[idx])

            # Window size minus most frequent character count
            # equals how many characters need replacement.
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer