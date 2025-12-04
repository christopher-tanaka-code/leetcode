from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # To allow O(1) lookups
        if endWord not in wordSet:
            return 0
        
        # Initialize BFS
        queue = deque([(beginWord, 1)])  # (current_word, current_level)
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
            
            # Try changing each character
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != current_word[i]:
                        next_word = current_word[:i] + c + current_word[i+1:]
                        if next_word in wordSet:
                            queue.append((next_word, level + 1))
                            wordSet.remove(next_word)  # Mark as visited
        
        return 0
