class TrieNode:
    def __init__(self):
        self.children = {}  # map from char to TrieNode
        self.is_end = False  # indicates end of a word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        # DFS helper function
        def dfs(j, node):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    # try all possible children
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end
        
        return dfs(0, self.root)
