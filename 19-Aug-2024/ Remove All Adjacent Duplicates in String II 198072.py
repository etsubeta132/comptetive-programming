# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        stack = []
        idx = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                idx.append(0)
            else:
                start = idx[-1]
                if stack[start] != s[i]:
                    idx.append(len(stack))
                    stack.append(s[i])
                else:
                    if len(stack) + 1 - start == k:
                        idx.pop()
                        stack = stack[:start]
                    else:
                        stack.append(s[i])
                
            
        return "".join(stack)
                    
                
                    





        