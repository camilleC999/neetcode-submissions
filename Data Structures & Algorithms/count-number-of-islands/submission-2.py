'''
DFS
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        count = 0

        def dfs(grid, row, col, visited):
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[row])) \
            or (row, col) in visited or grid[row][col] == "0":
                return

            visited.add((row, col))
            for dr, dc in directions:
                dfs(grid, row + dr, col + dc, visited)

            return 1

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in visited and grid[row][col] == "1":
                    count += dfs(grid, row, col, visited)

        return count
