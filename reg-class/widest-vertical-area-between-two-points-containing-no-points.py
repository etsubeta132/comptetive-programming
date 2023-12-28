class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        mx_area = 0

        for i in range(1,len(points)):
            area = points[i][0]-points[i-1][0]
            mx_area = max(mx_area,area)

        return mx_area
