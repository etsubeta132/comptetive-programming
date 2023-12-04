class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        idx = 0 
        step = 0
        cap = capacity
        while idx < len(plants):
            if cap < plants[idx]:
                step = step + idx
                step = step + idx+1
                cap = capacity-plants[idx]
            else:
                cap-= plants[idx]
                step +=1   
            idx+=1
        return step
        
        