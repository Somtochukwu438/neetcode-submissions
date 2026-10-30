class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(a, b):
            stack = []
            stack.append((a,b))
            grid[a][b] = 0
            area = 1
            while stack:
                c, d = stack.pop()
                for dy, dx in directions:
                    left = dy + c
                    right = dx + d
                    if 0 <= left < len(grid) and 0 <= right < len(grid[0]) and grid[left][right] == 1:
                        grid[left][right] = 0
                        stack.append((left, right))
                        area += 1
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        

        return max_area

        