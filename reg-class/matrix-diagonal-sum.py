class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        primary_dig  = 0
        l,r = 0,0
        
        while l< n and r< n:
            primary_dig+=mat[l][r]
            l+=1
            r+=1
        
        l,r = 0,n-1
        second_dig = 0


        while l < n and r >= 0:
            second_dig+= mat[l][r]
            l+=1
            r-=1
        
        if n%2==0:
            result = primary_dig + second_dig
        else:
            result = primary_dig + second_dig - mat[n//2][n//2]

        return result
