# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0,0,0]
        for bill in bills:
            if bill == 10:
                if changes[0] >= 1:
                    changes[0] -=1
                    changes[1] +=1
                else:
                    return False
            elif bill == 20:
                if changes[1] >= 1 and changes[0]>=1:
                    changes[1] -=1
                    changes[0] -=1 
                elif changes[0]>=3:
                    changes[0] -=3
                else:
                    return False
                changes[2]+=1
            else:
                changes[0]+=1
        return True
           








                 
