# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        key = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        fin_str = ""
        i = 0
        while i<len(s):
            if i+2<len(s):
                if s[i+2]=="#":
                    num = int(s[i:i+2])
                    fin_str+=key[num-1]
                    i+=3
                else:
                    num = int(s[i])
                    fin_str+=key[num-1]
                    i+=1
            else:
                num = int(s[i])
                fin_str+=key[num-1]
                i+=1
        return fin_str


        