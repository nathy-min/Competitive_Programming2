class Solution:
    def path(self, r, c):
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        for move in moves:
            res.append([r + move[0], c + move[1]])

        return res    

    def dfs(self, r, c):
        if r >= 0 and c >= 0 and r < self.row and c < self.col and self.board[r][c] == "O":
            self.board[r][c] = "S"
            moves = self.path(r, c)
            for move in moves:
                self.dfs(move[0], move[1])
        else:
            return

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
        
        for i in range(self.row):
            for j in range(self.col):
                if i == 0 or j == 0 or i == self.row - 1 or j == self.col - 1:
                    if board[i][j] == "O":
                        self.dfs(i, j)
        
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == "S":
                    self.board[i][j] = "O"
                elif self.board[i][j] == "O":
                    self.board[i][j] = "X"