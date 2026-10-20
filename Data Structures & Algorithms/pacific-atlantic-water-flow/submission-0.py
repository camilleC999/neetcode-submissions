class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac = deque((0, i) for i in range(COLS))
        pac.extend((i, 0) for i in range(ROWS))
        atl = deque((ROWS - 1, i) for i in range(COLS))
        atl.extend((i, COLS-1) for i in range(ROWS))
        
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

        pacific = set(pac)
        pacific.update(bfs(ROWS, COLS, pac))
        atlantic = set(atl)
        atlantic.update(bfs(ROWS, COLS, atl))

        return [list(tup) for tup in pacific & atlantic]






        # for row in range(ROWS):
        #     pac.append((row, 0))
        #     atl.append((row, COLS - 1))

        # while pac:
        #     for i in range(len(pac)):
        #         row, col = pac.popleft()

        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc

        #             if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] >= grid[row][col]:
        #                 in_pacific.add(grid[nr][nc])
        #                 visit.add(grid[nr][nc])
        #                 pac.append((nr, nc))

        # visit.clear()
        # while atl:
        #     for i in range(len(atl)):
        #         row, col = atl.popleft()

        #         if ((row, col)) in in_pacific 

        #         for dr, dc in directions:
        #             nr, nc = row + dr, col + dc

        #             if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] >= grid[row][col]:
        #                 in_pacific.add(grid[nr][nc])
        #                 visit.add(grid[nr][nc])
        #                 pac.append((nr, nc))

        

        




        