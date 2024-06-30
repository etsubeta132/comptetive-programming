# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        board  = []
        out = []
        slope = set()
        cols = set()
        antislope = set()

        def backtrack(idx):
            if idx == n:
                out.append(board[:])
                return
            
            for i in range(n):
                if idx-i in slope or i in cols or i+idx in antislope:
                    continue

                board.append((i,idx))

                slope.add(idx-i)
                antislope.add(i+idx)
                cols.add(i)

                backtrack(idx+1)

                board.pop()

                slope.remove(idx-i)
                antislope.remove(i+idx)
                cols.remove(i)
            

        backtrack(0)

        return len(out)