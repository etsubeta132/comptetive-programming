class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1 = ""
        res2 = ""
        for word in word1:
            res1+=word
            
        for word in word2:
            res2+=word
            
        if res1==res2:
            return True
        else:
            return False