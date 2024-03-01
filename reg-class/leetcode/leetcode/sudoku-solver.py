class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False]*9 for _ in range(9)]
        cols = [[False]*9 for _ in range(9)]
        box  = [[[False]*9 for i in range(3)] for j in range(3)]
        empty = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empty.append((row,col))
                else:
                    value = int(board[row][col])-1
                    rows[row][value] = cols[col][value] = box[row//3][col//3][value] = True
        
        self.issolved = False

        def backtrack(idx):
            if idx == len(empty):
                self.issolved = True
                return 
            
            r,c = empty[idx]
            for val in range(9):
                
                if not self.issolved and not rows[r][val] and not cols[c][val] and not box[r//3][c//3][val]:
                    board[r][c] = str(val+1)
                    rows[r][val] = cols[c][val] = box[r//3][c//3][val] = True
                    backtrack(idx+1)
                    rows[r][val] = cols[c][val] = box[r//3][c//3][val] = False
                    
            
        backtrack(0)
