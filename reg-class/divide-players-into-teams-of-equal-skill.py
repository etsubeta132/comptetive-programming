class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        
        res = skill[0]+skill[len(skill)-1]
        chemistry = skill[0]*skill[len(skill)-1]
        l,r = 1,len(skill)-2

        while l< r:
            if skill[l] + skill[r] != res:
                return -1
            else:
                chemistry += skill[l]*skill[r]
                l+=1
                r-=1
            
        return chemistry





