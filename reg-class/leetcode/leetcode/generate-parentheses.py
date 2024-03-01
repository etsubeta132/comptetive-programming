class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub  = []
        result = []
        def parSub(idx,open,close): 
            if len(sub) >= 2*n:
                if len(sub) == 2*n and open==close:
                    return result.append("".join(sub))
                return

            if close > open:
                return 

            sub.append("(")
            open+=1
            parSub(idx+1,open,close)
            sub.pop()
            open-=1

            sub.append(")")
            close+=1
            parSub(idx+1,open,close)
            sub.pop()
            close-=1
                
        
        parSub(0,0,0)

        return list(result)
            

