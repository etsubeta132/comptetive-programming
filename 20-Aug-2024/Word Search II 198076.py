# Problem: Word Search II - https://leetcode.com/problems/word-search-ii/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.isend = True
    
    def search(self, root, char):
        if char in root.children:
            return True
        else:
            return False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        board_words = set()
        def dfs(root, row, col, word, visited):
            if not trie.search(root, board[row][col]):
                return []
            else:
                char = board[row][col]
                root = root.children[char]
                word.append(char)
                if root.isend:
                    board_words.add("".join(word))
                dir = [(1, 0), (0, -1), (0, 1), (-1, 0)]
                for r, c in dir:
                    if (row + r, col + c) not in visited and 0 <= row + r < len(board) and 0 <= col + c < len(board[0]):
                        visited.add((row, col))
                        dfs(root, row + r, col + c, word, visited)
                        visited.remove((row, col))
                word.pop()
        
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j, [], set())
        
        return list(board_words)
                       