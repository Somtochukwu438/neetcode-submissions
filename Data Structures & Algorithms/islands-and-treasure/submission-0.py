class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        queue = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    queue.append((x, y))
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for d1, d2 in directions:
                row, col = r + d1, c + d2
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == INF:
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))


        