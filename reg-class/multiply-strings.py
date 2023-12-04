class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        exp = num1+"*"+num2
        return str(eval(exp))
        