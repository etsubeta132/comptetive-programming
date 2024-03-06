class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            row = matrix[r]
            left,right = 0,len(row)-1
            if target > row[right]:
                continue
            
            while left <= right:
                mid = (left+right)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right  = mid - 1
                else:
                    left = mid + 1
            return False
            
