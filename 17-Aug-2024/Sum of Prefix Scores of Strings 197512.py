# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
                
            cur = cur.children[char]
            cur.count += 1
        

    def score(self, word: str) -> bool:

        result = 0 
        cur = self.root

        for char in word:
            cur = cur.children[char]
            result += cur.count
        
        return result
        

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        T = Trie()

        for word in words:
            T.insert(word)
        
        answer = []
        for word in words:
            answer.append(T.score(word))
        
        return answer
        