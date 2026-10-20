
'''
    BFS

    This example gave you trouble bc you had  (0 < col < COLS) instead of (0 <= col < COLS).
    Make sure to double check your base cases always when things aren't coming back right.
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        big_isl = 0
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(grid, r, c):
            count = 1
            queue = deque([(r,c)])

            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    grid[row][col] = 0
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            count += 1
                            grid[nr][nc] = 0
                            queue.append((nr, nc))

            return count

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    big_isl = max(big_isl, bfs(grid, row, col))

        return big_isl


