# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_col.add(j)
                    zero_row.add(i)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
        

        