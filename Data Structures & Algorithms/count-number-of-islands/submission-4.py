'''
BFS
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(grid, r, c):
            grid[r][c] = "0"
            queue = deque([(r, c)])

            while queue:
                for node in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(grid, row, col)
                    islands += 1
        
        return islands

