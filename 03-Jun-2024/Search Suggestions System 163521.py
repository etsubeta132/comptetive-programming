# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.idx = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.result = {}

    def insert(self, word: str) -> None:
        cur = self.root
        
        for idx, char in enumerate(word):
            if char not in cur.children:
                self.result[word[: idx + 1]] = []
                cur.children[char] = TrieNode()
              
            cur = cur.children[char]
            cur.idx = idx
            
        cur.is_end = True
        

    def search(self, product_name, word):
        cur = self.root

        for char in product_name:
            if char in cur.children:
                i = cur.children[char].idx 
                self.result[word[: i + 1]].append(product_name)
                cur = cur.children[char]
            else:
                break
        
        return self.result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = Trie()
        trie.insert(searchWord)
        
        for product in products:
            trie.search(product, searchWord)
        
        result = []
        for key in trie.result.keys():
            val = trie.result[key][:3]
            result.append(val)
        
        return result



        