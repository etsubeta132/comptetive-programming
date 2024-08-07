# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution(object):
    def kClosest(self, points, k):
        result = sorted(points, key= lambda x: (x[0] ** 2 + x[1] ** 2))
        result  = result[:k]
        return result
