# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

from collections import deque

class Solution:
    def __init__(self):
        self.cost = []
        self.d = deque()
        self.n = 0

    def find_start(self, grid):
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j]:
                    self.d.append((i, j))
                    self.cost[i][j] = 0
                    return

    def shortestBridge(self, grid):
        self.n = len(grid)
        self.cost = [[float('inf')] * self.n for _ in range(self.n)]
        self.find_start(grid)
        first_island_found = False
        while self.d:
            x, y = self.d.popleft()
            if grid[x][y] == 0:
                first_island_found = True
            if first_island_found and grid[x][y]:
                return self.cost[x][y]
            dir = [-1, 0, 1, 0, -1]
            for i in range(len(dir) - 1):
                n_x, n_y = x + dir[i], y + dir[i + 1]
                if 0 <= n_x < self.n and 0 <= n_y < self.n and self.cost[n_x][n_y] == float('inf'):
                    self.cost[n_x][n_y] = min(self.cost[n_x][n_y], self.cost[x][y])
                    if grid[n_x][n_y] == 0:
                        self.cost[n_x][n_y] += 1
                        self.d.append((n_x, n_y))
                    else:
                        self.d.appendleft((n_x, n_y))
        return 0