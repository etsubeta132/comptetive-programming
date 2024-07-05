# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map={}
        t_map={}
        for i in range(0,len(s)):
            s_char=s[i]
            t_char=t[i]
            if (s_char in s_map and s_map[s_char] != t_char) or ( t_char in t_map and t_map[t_char] != s_char):
                return False
            s_map[s_char]=t_char
            t_map[t_char]=s_char
        return True