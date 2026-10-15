class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        for x in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[x][j] == 2:
                    queue.append((x, j))
                elif grid[x][j] == 1:
                    fresh += 1
        minute = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for d1, d2 in directions:
                    r, c = d1 + row, d2 + col
                    if 0 <= r and r < rows and 0 <= c and c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r,c))
            minute += 1
        if fresh == 0:
            return minute
        return -1

                    
        