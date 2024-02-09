class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        col = len(matrix[0])
        row = len(matrix)
        prefix = [[0]*(col) for _ in range(row)]
    
        for i in range(row):
            for j in range(col):
                top = prefix[i-1][j] if i > 0 else 0
                left = prefix[i][j-1] if j > 0 else 0
                top_left = prefix[i-1][j-1] if min(i,j) > 0 else 0
                prefix[i][j] = matrix[i][j] + top + left - top_left 
        
        res = 0
        for r1 in range(row):
            for r2 in range(r1,row):
                count = defaultdict(int)
                count[0] = 1
                for c in range(col):
                    sm1 = prefix[r1-1][c] if r1 >0 else 0
                    sm2 = prefix[r2][c]
                    curr_sum = sm2 - sm1
                    diff = curr_sum - target
                    res+= count[diff]
                    count[curr_sum]+=1
        
        
        return res
        