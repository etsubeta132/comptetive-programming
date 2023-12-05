class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_order = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        typed_words = []
        
        # iterate through each word
        for word in words:
            low_word = word.lower()
            k_order = ""

            # find the keyboard order that matches the first char of the word
            for ord in keyboard_order:
                if low_word[0] in ord:
                    k_order = ord
                    break
            
            #check if all matches the keyboard order 
            can_typed = True
            for char in low_word:
                if char not in k_order:
                    can_typed = False
                    break
           
            if can_typed:
                typed_words.append(word)

        return typed_words

        