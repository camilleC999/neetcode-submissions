class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        big_isl = 0
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, row, col):
            nonlocal big_isl
            if not (0 <= row < ROWS) or not (0 <= col < COLS) or grid[row][col] == 0:
                return 0

            count = 1
            grid[row][col] = 0

            for dr, dc in directions:
                count += dfs(grid, row + dr, col + dc)

            print("row, col: ", (row, col))
            print("count: ", count)
            return count

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    big_isl = max(big_isl, dfs(grid, row, col))

        return big_isl
                