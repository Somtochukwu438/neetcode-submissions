class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        max_area = 0

        def dfs(i, j):
            if 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0

                area = 1

                area += dfs(i + 1, j)
                area += dfs(i-1, j)
                area += dfs(i, j+1)
                area += dfs(i, j-1)
                return area
            return 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        return max_area
        