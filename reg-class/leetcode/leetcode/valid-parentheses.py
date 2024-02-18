class Solution:
    def isValid(self, s: str) -> bool:

        open = {"(":')',"[":"]","{":"}"}
        s=[i for i in s]
        stack = []
        for i in s:
            if i in open.keys():
                stack.append(i)
            else:
                if len(stack) != 0:
                    if open[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
                

            





        