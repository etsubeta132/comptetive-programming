class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for p in s:
            if p == "(":
                if len(stack)==0:
                    stack.append(p)
                else:
                    if stack[-1] == "(":
                        stack.append(p)
                    else:
                        stack.append("+")
                        stack.append(p)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("1")
                else:
                    exp = ''
                    while stack[-1] !="(":
                        exp += str(stack.pop())
                    exp = str(eval(exp)*2)
                    stack.pop()
                    stack.append(exp)
            
        return eval("".join(stack))
