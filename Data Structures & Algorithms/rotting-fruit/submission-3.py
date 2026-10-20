class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        queue = deque([])
        fresh = 0 
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1

        if fresh == 0:
            return time


        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            
            time += 1

        return time - 1 if fresh == 0 else -1

                
