class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expressions = []
        operators = {"+","-","/","*"}
        for operand in tokens:
            if operand in operators:
                opp1 = expressions.pop()
                opp2 = expressions.pop()
                res = int(eval(opp2 + operand + opp1))
                expressions.append(str(res))
            else:
                expressions.append(operand)
        
        return int(expressions[-1])