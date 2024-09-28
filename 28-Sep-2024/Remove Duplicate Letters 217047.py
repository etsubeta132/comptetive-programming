# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {s[i]:i for i in range(len(s))}
        stack = []
        visited = {}
        for idx,char in enumerate(s):
            if char  in visited:
                continue

            while stack and stack[-1] >= char and last_idx[stack[-1]] > idx:
                del visited[stack.pop()]
                    
            stack.append(char)
            visited[char] = idx
                        
        
        return "".join(stack)
           