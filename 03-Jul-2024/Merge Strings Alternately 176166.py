# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        t = min(len(word1),len(word2))
        l = 0
        while l<t:
            n_str = word1[l]+word2[l]
            new_word+=n_str
            l+=1
        if l <len(word1):
            new_word+=word1[l:]
        elif l <len(word2):
            new_word+=word2[l:]
        return new_word


        