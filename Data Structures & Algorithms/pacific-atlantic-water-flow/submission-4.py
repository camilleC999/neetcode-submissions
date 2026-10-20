class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac = deque((r, c) for r in range(ROWS) for c in range(COLS) if r == 0 or c == 0)
        atl = deque((r, c) for r in range(ROWS) for c in range(COLS) if r == ROWS - 1 or c == COLS - 1)
        
        def bfs(ROWS, COLS, queue):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            visit = set()
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] >= grid[row][col]:
                            visit.add((nr, nc))
                            queue.append((nr, nc))

            return visit

        pacific = set(pac).union(bfs(ROWS, COLS, pac))
        atlantic = set(atl).union(bfs(ROWS, COLS, atl))
        return [list(tup) for tup in pacific & atlantic]

        # this equals above
        # pacific = set(pac)
        # pacific.update(bfs(ROWS, COLS, pac))
        # atlantic = set(atl)
        # atlantic.update(bfs(ROWS, COLS, atl))

        # return [list(tup) for tup in pacific & atlantic]


        