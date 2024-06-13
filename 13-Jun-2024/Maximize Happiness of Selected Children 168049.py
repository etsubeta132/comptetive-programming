# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        N = len(happiness)
        
        result = 0
        turn = 0

        for  i in range(N - 1, N - k - 1, -1):

            happy_value = happiness[i] - turn 
            if happy_value > 0:
                result += happy_value
                turn += 1
            
            else:
                break
        
        return result


