# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            
            if bill == 5:
                change[5] += 1

            elif bill == 10:
                change[10] += 1

                if change[5] >= 1:
                    change[5] -= 1
                else:
                    return False
            else:
                change[20] += 1

                if change[5] >= 1 and change[10] >= 1:
                    change[5] -= 1
                    change[10] -= 1
                
                elif change[5] >= 3:
                    change[5] -= 3
                else: 
                    return False
        
        return True
