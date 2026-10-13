class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(a, b):
            stack = []
            stack.append((a,b))
            seen.add((a,b))
            area = 1
            while stack:
                c, d = stack.pop()
                for dy, dx in directions:
                    left = dy + c
                    right = dx + d
                    if left in range(len(grid)) and right in range(len(grid[0])) and (left, right) not in seen and grid[left][right] == 1:
                        stack.append((left, right))
                        seen.add((left, right))
                        area += 1
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        

        return max_area

        