# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        matrix = []
        l = 0 
        r = n - 1
        while r < len(original):
            matrix.append(original[l : r + 1])
            l = r + 1
            r += n
        
        return matrix
        