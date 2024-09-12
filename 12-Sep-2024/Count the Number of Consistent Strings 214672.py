# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed1 = {i:1 for i in allowed}
        
        def isAllowed(word):
            return len(set(word) -  set(allowed)) == 0
        
        ctr = 0
        for word in words:
            if isAllowed(word):
                ctr += 1
        

        return ctr
