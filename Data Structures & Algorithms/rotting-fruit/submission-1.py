class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        time = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque()
        fresh = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                left, right = queue.popleft()
                for dy, dx in directions:
                    new_left = left + dy
                    new_right = right + dx
                    if 0 <= new_left < r and 0 <= new_right < c and grid[new_left][new_right] == 1:
                        grid[new_left][new_right] = 2
                        fresh -= 1
                        queue.append((new_left, new_right))
            time += 1

        return time if fresh == 0 else -1