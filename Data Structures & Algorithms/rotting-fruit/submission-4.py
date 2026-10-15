class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        num_fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and num_fresh > 0:
            for x in range(len(queue)):
                r, c = queue.popleft()
                for d1, d2 in directions:
                    row, col = r+d1, c+d2
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        num_fresh -= 1
                        queue.append((row,col))
            minutes+=1
        if num_fresh == 0:
            return minutes
        return -1




        