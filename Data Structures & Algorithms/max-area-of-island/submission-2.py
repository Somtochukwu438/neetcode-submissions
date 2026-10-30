class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        if not grid:
            return o
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = 0
                area = 1
                area += dfs(i+1, j)
                area += dfs(i-1, j)
                area += dfs(i, j-1)
                area += dfs(i, j+1)
                return area
            return 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area
        