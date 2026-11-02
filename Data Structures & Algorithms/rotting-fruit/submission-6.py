class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        num_fresh = 0
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue and num_fresh > 0:
            for _ in range(len(queue)):
                a, b = queue.popleft()
                for c, d in directions:
                    left, right = a + c, b + d
                    if left in range(rows) and right in range(cols) and grid[left][right] == 1:
                        grid[left][right] = 2
                        num_fresh -= 1
                        queue.append((left, right))
            time += 1

        if num_fresh == 0:
            return time
        return -1
        
        





        