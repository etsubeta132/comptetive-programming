class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid_t = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid_t[j][i] = grid[i][j]
        print(grid_t)
        res = 0
        for i in range(n):
            mxr = max(grid[i])
            for j in range(n):
                mxc = max(grid_t[j])
                cur_maxr = max(grid[i])
                cur_maxc = max(grid_t[j])
                res += abs(min(cur_maxr,cur_maxc)-grid[i][j])
        
        return res