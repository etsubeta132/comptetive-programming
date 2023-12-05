class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_word = max(words,key=len)
        new_list = []
        for i in range(len(max_word)):
            word=""
            for wd in words:
                if i<len(wd):
                    word+=wd[i]
                else:
                    word+=" "
            word = word.rstrip()
            new_list.append(word)
        return new_list            
                    

        