class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        seen = set()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            seen.add((r,c))
            while queue:
                l, r = queue.popleft()
                for a,b in directions:
                    dx = l + a
                    dy = r + b
                    if dx in range(len(grid)) and dy in range(len(grid[0])) and (dx, dy) not in seen and grid[dx][dy] == "1":
                        queue.append((dx,dy))
                        seen.add((dx,dy))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    count += 1
                    dfs(r, c)
        return count
        