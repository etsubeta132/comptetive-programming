class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoton = {}
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and  stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                monoton[(temp,idx)] = i-idx
            
            stack.append((temperatures[i],i))
        for key,val in monoton.items():
            temp,idx = key
            result[idx] = val
        
        return result 
    