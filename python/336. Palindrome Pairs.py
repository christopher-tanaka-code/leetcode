from typing import List


class TrieNode:
    __slots__ = ("children", "word_index", "palindrome_suffix_words")

    def __init__(self):
        self.children = {}
        self.word_index = -1
        self.palindrome_suffix_words = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        prefix_pal = []
        suffix_pal = []

        for word in words:
            pref, suff = self._palindrome_prefix_suffix(word)
            prefix_pal.append(pref)
            suffix_pal.append(suff)

        # Insert reversed words into trie
        for idx, word in enumerate(words):
            node = root
            n = len(word)

            for pos in range(n - 1, -1, -1):
                # If word[0 : pos + 1] is palindrome,
                # this word can complete another word ending here.
                if prefix_pal[idx][pos + 1]:
                    node.palindrome_suffix_words.append(idx)

                ch = word[pos]
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]

            node.word_index = idx
            node.palindrome_suffix_words.append(idx)

        ans = []

        # Search each word in the reversed-word trie
        for idx, word in enumerate(words):
            node = root
            valid_path = True

            for pos, ch in enumerate(word):
                # If a reversed word ends here, the remaining part of word
                # must be palindrome.
                if (
                    node.word_index != -1
                    and node.word_index != idx
                    and suffix_pal[idx][pos]
                ):
                    ans.append([idx, node.word_index])

                if ch not in node.children:
                    valid_path = False
                    break

                node = node.children[ch]

            if not valid_path:
                continue

            # All remaining words below this node have palindrome leftovers.
            for other_idx in node.palindrome_suffix_words:
                if other_idx != idx:
                    ans.append([idx, other_idx])

        return ans

    def _palindrome_prefix_suffix(self, s: str):
        """
        Returns:
        prefix[i] = True if s[0:i] is palindrome
        suffix[i] = True if s[i:] is palindrome

        Uses Manacher's algorithm, so this is O(len(s)).
        """
        n = len(s)

        if n == 0:
            return [True], [True]

        # Odd length palindrome radius
        odd = [0] * n
        left, right = 0, -1

        for i in range(n):
            k = 1 if i > right else min(odd[left + right - i], right - i + 1)

            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1

            odd[i] = k

            if i + k - 1 > right:
                left = i - k + 1
                right = i + k - 1

        # Even length palindrome radius
        even = [0] * n
        left, right = 0, -1

        for i in range(n):
            k = 0 if i > right else min(even[left + right - i + 1], right - i + 1)

            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1

            even[i] = k

            if i + k - 1 > right:
                left = i - k
                right = i + k - 1

        prefix = [False] * (n + 1)
        suffix = [False] * (n + 1)

        prefix[0] = True
        suffix[n] = True

        # Check every prefix s[0:length]
        for length in range(1, n + 1):
            if length % 2 == 1:
                center = length // 2
                prefix[length] = odd[center] >= center + 1
            else:
                center = length // 2
                prefix[length] = even[center] >= center

        # Check every suffix s[start:n]
        for start in range(n - 1, -1, -1):
            length = n - start

            if length % 2 == 1:
                center = start + length // 2
                suffix[start] = odd[center] >= length // 2 + 1
            else:
                center = start + length // 2
                suffix[start] = even[center] >= length // 2

        return prefix, suffix