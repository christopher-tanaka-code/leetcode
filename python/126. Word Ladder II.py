from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while level and not found:
            next_level = set()

            # Remove current level words from wordSet so we don't revisit older levels
            for word in level:
                wordSet.discard(word)

            for word in level:
                word_chars = list(word)
                for i in range(len(word_chars)):
                    original = word_chars[i]
                    for ch in alphabet:
                        if ch == original:
                            continue
                        word_chars[i] = ch
                        new_word = "".join(word_chars)

                        if new_word in wordSet:
                            if new_word == endWord:
                                found = True
                            next_level.add(new_word)
                            parents[new_word].append(word)

                    word_chars[i] = original

            level = next_level

        if not found:
            return []

        res = []
        path = [endWord]

        def dfs(word: str):
            if word == beginWord:
                res.append(path[::-1])
                return
            for prev in parents[word]:
                path.append(prev)
                dfs(prev)
                path.pop()

        dfs(endWord)
        return res