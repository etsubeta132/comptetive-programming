# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, binary):
        cur = self.root

        for char in binary:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
    
    
    def find_xor(self, binary):
        cur = self.root
        ans = 0
        for idx, bit in enumerate(binary):
            bit1 = "0" if bit == "1" else "1"
            if bit1 not in cur.children:
                if bit in cur.children:
                    cur = cur.children[bit]
            else:
                cur = cur.children[bit1]
                ans = ans + (1 << (32 - idx - 1))

        return ans
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()

        for num in nums:
            binary = bin(num)[2:]
            binary = "".join(["0"] * (32 - len(binary)))  + str(binary)
            trie.insert(binary)
        
        res = 0
        for num in nums:
            binary = bin(num)[2:]
            binary = "".join(["0"] * (32 - len(binary)))  + str(binary)
            res = max(res, trie.find_xor(binary))


        return res

            

        