class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        occupied = set()
        matrix = [[0]*n for _ in range(m)]
        
        for wall in walls:
            matrix[wall[0]][wall[1]] = "W"
        
        for guard in guards:
            matrix[guard[0]][guard[1]] = "G"
        


        for guard in guards:
            
            r = guard[0]
            c = guard[1]  

            i,j = r+1,c
            while 0 <= i < m:
                if matrix[i][j] == "W" or matrix[i][j] == "G":
                    break
                else:
                    occupied.add((i,j))
                    matrix[i][j] == 1
                
                i+=1
            
            
            i,j = r-1,c
            while 0<=i<m :
                if matrix[i][j] == "W" or matrix[i][j] == "G":
                    break
                else:
                    occupied.add((i,j)) 
                    matrix[i][j] = 1
                i-=1
                
            
            
            i,j = r,c+1
            while 0<=j<n:       
                if matrix[i][j] == "W" or matrix[i][j] == "G":
                    break
                else:
                    occupied.add((i,j))
                    matrix[i][j]  = 1 
                j+=1
            

            i,j = r,c-1
            while 0<=j<n:
                if matrix[i][j] == "W" or matrix[i][j] == "G":
                    break
                else:
                    occupied.add((i,j))
                    matrix[i][j] = 1 
                j-=1

       
        return m*n - (len(occupied)+len(guards)+len(walls))
        






        