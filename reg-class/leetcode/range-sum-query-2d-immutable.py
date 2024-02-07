class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c = len(matrix)+1,len(matrix[0])+1
        self.prefMat = [[0]*c for i in range(r)]

        for i in range(1,r):
            for j in range(1,c):
                self.prefMat[i][j] = self.prefMat[i-1][j]+self.prefMat[i][j-1]-self.prefMat[i-1][j-1] + matrix[i-1][j-1]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
  
        return self.prefMat[row2+1][col2+1] - self.prefMat[row2+1][col1] - self.prefMat[row1][col2+1] + self.prefMat[row1][col1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)