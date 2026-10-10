class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = [[False] * len(board[0]) for _ in range(len(board))]
        def dfs(i,j,z):
            if min(i,j) < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or seen[i][j] or word[z] != board[i][j]:
                return False

            seen[i][j] = True
            # print(word[z], i, j)
            if z == len(word) - 1:
                return True
            res = dfs(i + 1, j , z + 1) or dfs(i - 1, j , z + 1) or dfs(i, j + 1 , z + 1) or dfs(i, j - 1, z + 1)

            ## Remove it from here, so that this spot can then be used again for another pathway search
            seen[i][j] = False
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    # Great, do dfs and check
                    if dfs(i,j,0):
                        return True
        return False
        