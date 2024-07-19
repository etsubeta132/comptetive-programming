# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        new_inter = []
        
        l = 0
        r = 0
        while r < len(intervals):
            lower = intervals[l][0]
            upper = intervals[l][1]

            while r < len(intervals) and upper >= intervals[r][0]:
                upper = max(upper, intervals[r][1])
                r += 1
            
           
            new_inter.append([lower, upper])
            l = r

        return new_inter