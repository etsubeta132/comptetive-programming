# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ans = []
        for word in words:

            char_map = {}
            patt_map = {}
            isMatch = True

            for i in range(len(word)):
                if word[i] in char_map:
                    if char_map[word[i]] != pattern[i]:
                        isMatch = False
                else:
                    char_map[word[i]] = pattern[i]
                
                if pattern[i] in patt_map:
                    if patt_map[pattern[i]] != word[i]:
                        isMatch = False
                else:
                    patt_map[pattern[i]] = word[i]
            
            if isMatch:
                ans.append(word)
            
        return ans
            
            
                    
        