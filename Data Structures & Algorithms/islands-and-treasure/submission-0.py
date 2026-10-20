'''
input = [[inf ,-1  ,0   ,inf],
         [inf ,inf ,inf ,-1 ],
         [inf ,-1  ,inf ,-1 ],
         [0   ,-1  ,inf ,inf]]

Start at the treasure chets and find explore all possible paths.
if not -1 and not 1 and not 0
    if the child node is inf, fill child node with parent + 1
    else: node = min(parent + 1, node.val)

    append child node
'''

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        treasure = deque()
        visit = set()
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasure.append((row, col))

        if len(treasure) == len(grid) * len(grid[0]):
            return
        
        while treasure:
            for node in range(len(treasure)):
                row, col = treasure.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visit:
                        num = grid[new_row][new_col]
                        if num not in (-1, 0):
                            grid[new_row][new_col] = min(grid[row][col] + 1, num)
                            treasure.append((new_row, new_col))
                            visit.add((new_row, new_col))


