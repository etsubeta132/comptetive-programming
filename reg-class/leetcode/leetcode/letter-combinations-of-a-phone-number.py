class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) <= 0:
            return 
        
        digit_dict = {"1":"", "2":["a","b","c"], "3":["d","e","f"],
                    "4":["g","h","i"], "5":["j","k","l"],"6":["m","n","o"],
                    "7":["p","q","r","s"], "8":["t","u","v"],"9":["w","x","y","z"]}
        digits = [i for i in digits]
        result = []
        sub = []
        def backtrack(idx):
            if idx == len(digits):
                result.append("".join(sub))
                return 
            
            chrs = digit_dict[digits[idx]]
            for j in range(len(chrs)):
                sub.append(chrs[j])
                backtrack(idx+1)
                sub.pop()
            return result
        
        backtrack(0)
        return result
