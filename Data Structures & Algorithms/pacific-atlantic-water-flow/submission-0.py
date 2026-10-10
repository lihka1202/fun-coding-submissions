class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []
        def dfs(i, j, visited, prevHeight):
            if min(i,j) < 0 or i == ROWS or j == COLS or (i,j) in visited or heights[i][j] < prevHeight:
                return 
            visited.add((i,j))

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(i + di, j + dj, visited, heights[i][j])
        
        for c in range(COLS):
            dfs(0,c, pacific, heights[0][c])
            # From atlantic
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r,0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res
