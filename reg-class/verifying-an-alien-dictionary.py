class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {char:idx for idx, char in enumerate(order)}
    
        def is_ordered(word1, word2):
            N1, N2 = len(word1), len(word2)

            for i in range(min(N1, N2)):
                if index[word2[i]] > index[word1[i]]:
                    return True
                elif index[word2[i]] == index[word1[i]]:
                    continue

                return False

            return len(word1) <= len(word2)

        for i in range(1, len(words)):
            if not is_ordered(words[i - 1], words[i]):
                return False

        return True
        

            


        
        
    

        