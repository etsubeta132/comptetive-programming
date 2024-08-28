# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        arrays.sort()
        mn_mx = []
        for i in range(len(arrays)):
            mn_mx.append((arrays[i][0], arrays[i][-1]))
        
        val = 0
        for i in range(len(mn_mx)):
            for j in range(len(mn_mx)):
                if i != j:
                    val = max(val,mn_mx[j][1] - mn_mx[i][0])
                    val = max(val,mn_mx[i][1] - mn_mx[j][0])
            
            return val



        