class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        
        size = len(heights)

        for i in range(size):

            p = i
            min_num = heights[i]

            for j in range(i+1,size):
                if min_num > heights[j]:
                    min_num = heights[j]
                    p = j
                    
            heights[i],heights[p] = heights[p],heights[i]
            names[i],names[p] = names[p],names[i]

        return names[::-1] 

        



