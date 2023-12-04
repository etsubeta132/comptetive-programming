class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tot_sec = 0
        def num_steps(p1,p2):
            s1 = abs(p1[0]-p2[0])
            s2 = abs(p1[1]-p2[1])
            min_s = min(s1,s2)
            seconds = abs(s1-s2)+min_s
            return seconds
        for i in range(1,len(points)):
            second = num_steps(points[i-1],points[i])
            tot_sec+=second
        return tot_sec


        