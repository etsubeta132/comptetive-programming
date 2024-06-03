# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = []
    
    def insert(self, path):
        cur = self.root
        
        for char in path:
            if cur.is_end:
                break
            
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        
        cur.is_end = True
    
    def search(self, root, res):
        if root.is_end:
            self.result.append("".join(res))
            return
        
        
        for node in root.children:
            res.append(f"/{node}")
            temp = root
            root = root.children[node]
            
            self.search(root, res)
            root = temp
            res.pop()
    
        return self.result
    
            

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for path in folder:
            path_l = path.split("/")[1:]
            trie.insert(path_l)
        
        root = trie.root
        
        return trie.search(root, [])
