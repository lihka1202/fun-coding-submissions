from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Think of the problem in reverse
        # Dont start from land, instead go the other way.

        q = deque()

        # Do one run to get the start points in
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        seen = [[False] * len(grid[0]) for _ in range(len(grid))]

        count = 0
        print(list(q))
        while len(q) > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if min(r + dr, c + dc) >= 0 and r + dr < len(grid) and c + dc < len(grid[0]) and grid[r+dr][c+dc] not in [0,-1] and not seen[r+dr][c+dc]:
                        grid[r+dr][c+dc] = min(1 + count, grid[r+dr][c+dc])
                        q.append((r+dr, c+dc))
                        seen[r+dr][c+dc] = True
            count += 1
        print(grid)