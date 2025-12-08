class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0
        max_count = 0

        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1

            max_count = max(max_count, count)

            # Early stopping: can't do better than k
            if max_count == k:
                return k

        return max_count
