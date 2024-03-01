class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board  = [["." for _ in range(n)] for _ in range(n)]
        out = []
        slope = set()
        cols = set()
        antislope = set()

        def build(board):
            ans = []
            for row in board:
                ans.append("".join(row))
            return ans 

        def backtrack(idx):
            nonlocal n
            if idx == n:
                out.append(build(board))
                return 
            
            for i in range(n):
                if idx-i in slope or i in cols or i+idx in antislope:
                    continue

                board[idx][i] = "Q"
                slope.add(idx-i)
                antislope.add(i+idx)
                cols.add(i)
                backtrack(idx+1)
                board[idx][i] = "." 
                slope.remove(idx-i)
                antislope.remove(i+idx)
                cols.remove(i)

        backtrack(0)
        return out

        


