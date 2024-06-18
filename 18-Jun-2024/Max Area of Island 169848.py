# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        islands = {(i,j):(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        rank = {(i,j):0 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        
        def find(row, col):
            if islands[(row, col)] == (row, col):
                return (row, col)
            
            row, col = islands[(row, col)]
            return find(row, col)
        
        def union(cell1, cell2):
            row1, col1 = cell1
            row2, col2 = cell2
            border1 = find(row1, col1)
            border2 = find(row2, col2)

            if border1 != border2:
                if rank[border1] > rank[border2]:
                    islands[border2] = border1
                elif rank[border2] > rank[border1]:
                    islands[border1] = border2
                else:
                    islands[border1] = border2
                    rank[border1] += 1
            
        def inbound(row, col):
            row_bound = row >= 0 and row < len(grid)
            col_bound = col >= 0 and col < len(grid[0]) 

            return  row_bound and col_bound

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:

                    for road in directions:
                        
                        x, y = road
                        if inbound(row + x, col + y) and grid[row + x][col + y] == 1:
                            union((row, col), (row + x, col + y))
        
        lands = defaultdict(list)
        for land1, land2 in islands.items():
            border = find(land2[0], land2[1])
            lands[border].append((land1[0],land1[1]))
        
     
        result = 0
        for key, island in lands.items():
            result = max(result, len(island))
        
        return result