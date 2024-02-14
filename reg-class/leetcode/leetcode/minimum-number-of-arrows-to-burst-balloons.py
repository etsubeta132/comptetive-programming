class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        r = 1
        ctr = 1
        lap = points[0]
        while r < len(points):
            if lap[1] >= points[r][0]:
                end =min(lap[1],points[r][1])
                lap = [points[r][0],end]
            else:
                ctr+=1
                lap = points[r]
            
            r+=1
        return ctr



