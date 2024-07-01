# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        i = 0
        j = 0

        while j < len(s) and i < len(g):

            if s[j] >= g[i]:
                i+=1
                j+=1

            elif g[i] > s[j]:
                j+=1

        return i

