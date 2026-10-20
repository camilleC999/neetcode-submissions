class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        def dfs(grid, row, col, visited):
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[row])) \
            or (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))

            dfs(grid, row + 1, col, visited)
            dfs(grid, row, col + 1, visited)
            dfs(grid, row - 1, col, visited)
            dfs(grid, row, col - 1, visited)

            return 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited and grid[row][col] == "1":
                    print("I'm in here")
                    count += dfs(grid, row, col, visited)




        return count
