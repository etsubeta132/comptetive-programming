# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustrl = {i:set() for i in range(1,n+1)}
        trustrl2 = {i:set() for i in range(1,n+1)}
        
        for person in trust:
            trustrl.get(person[1],set()).add(person[0])

        for person in trust:
            trustrl2.get(person[0],set()).add(person[1])
        
        for person in trustrl.keys():
            if len(trustrl[person]) == n-1 and len(trustrl2[person]) == 0:
                return person
        
        return -1