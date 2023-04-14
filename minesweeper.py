class Solution:
    def inBound(self, r, c):
        if r < 0 or r >= len(self.board) or c < 0 or c >= len(self.board[0]):
            return True

    def move(self, r, c):
        res = []
        move = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
        for path in move:
            res.append((r + path[0], c + path[1]))

        return res

    def dfs(self, r, c):
        if self.inBound(r, c) or (r, c) in self.visited:
            return
        if self.board[r][c] == "M":
            self.board[r][c] = "X"
            return
        count = 0
        moves = self.move(r, c)
        self.visited.add((r, c))

        for move in moves:
            if not self.inBound(move[0], move[1]) and self.board[move[0]][move[1]] == "M":
                count += 1

        if count:
            self.board[r][c] = str(count)
            return
        self.board[r][c] = "B"

        for move in moves:
            if (move[0], move[1]) not in self.visited:
                self.dfs(move[0], move[1])


    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.board = board
        self.visited = set()
        self.dfs(click[0], click[1])

        return self.board