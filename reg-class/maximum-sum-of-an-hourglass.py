class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        def hourglasses(grid,x,y):
            if x+2 < len(grid) and y+2 <len(grid[0]):
                result = grid[x][y]+grid[x][y+1]+grid[x][y+2]+grid[x+1][y+1]+grid[x+2][y+1]+grid[x+2][y]+grid[x+2][y+2]
            
            else:
                result = 0

            return result
        
        max_glasses = 0

        for x in range(len(grid)):

            for y in range(len(grid[0])):


                max_glasses = max(hourglasses(grid,x,y), max_glasses)
        
        return max_glasses