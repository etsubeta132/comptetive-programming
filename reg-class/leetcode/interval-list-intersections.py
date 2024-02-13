class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        
        intersection = []
        
        s = 0
        e = 0

        while s < len(firstList) and e < len(secondList):
            first1,first2 = firstList[s]
            second1,second2 = secondList[e]

            start_overlap = max(first1,second1) 
            end_overlap = min(first2,second2)

            if start_overlap <= end_overlap:
                intersection.append([start_overlap,end_overlap])

            if first2 < second2:
                s+=1 
            else:
                e+=1  
                   
        return intersection
            

        
        