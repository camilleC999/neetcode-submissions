'''
DFS
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    dfs(grid, nr, nc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    islands += 1

        return islands


