from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths are different, they can't be close
        if len(word1) != len(word2):
            return False

        # Count character frequencies
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # Check if both strings have the same set of characters
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        # Check if sorted frequencies are the same
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True
