class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                area = 1
                for d1, d2 in directions:
                    row, col = r + d1, c + d2
                    area += dfs(row, col)
                return area
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area
        