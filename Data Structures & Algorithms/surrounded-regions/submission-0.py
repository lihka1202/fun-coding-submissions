class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        # So in this case if theres an O connecting the end, this can cause issues
        # So basically we find all those cases where we are connecting to the outside, and we do our best to avoid dealing with these cases
        def dfs(i,j):
            if min(i,j) < 0 or i == ROWS or j == COLS or (i,j) in visited or board[i][j] == "V" or board[i][j] == "X":
                return
            visited.add((i,j))
            board[i][j] = "V"
            for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
                dfs(i + di, j + dj)

    
        for r in range(0, ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)
        print(board)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "V":
                    board[i][j] = "O"
            

        
        