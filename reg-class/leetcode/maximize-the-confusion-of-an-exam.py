class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def flip(char,k):
            l = r = mx_ln  = 0
            while r < len(answerKey):
                if answerKey[r]!= char:
                    k-=1

                while k < 0:
                    if answerKey[l]!= char:
                        k+=1
                    l+=1
                mx_ln = max(mx_ln, r-l+1)
                r+=1
                
            return mx_ln
        
        win = max(flip('T',k),flip('F',k))
        
        return win
            
                    