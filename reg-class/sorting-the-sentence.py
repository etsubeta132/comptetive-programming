class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = {int(word[-1]):word[:-1] for word in s.split()}
       
        rs = []
        for i in range(len(s)):
            rs.append(s[i+1])
        
        return " ".join(rs)
