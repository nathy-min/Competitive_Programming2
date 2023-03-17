class Solution:
    def helper(self, visited, row, col):
        for v in visited:
            if v[0] - v[1] == row - col:
                return False
            if v[1] == col or v[0] + v[1] == row + col:
                return False
        return True
    
    def queens(self, visited, row, col):
        if len(visited) == self.n:
            self.sol.append(list(visited))
            return
        if row == self.n or col == self.n:
            return
        
        for c in range(col, self.n):
            if self.helper(visited, row, c):
                visited.append([row, c])
                self.queens(visited, row + 1, 0)
                visited.pop()

    def generate_board(self, positions):
        n = len(positions)
        board = [["."] * n for _ in range(n)]

        for row, col in positions:
            board[row][col] = "Q"

        return ["".join(row) for row in board]

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.sol = []
        self.queens([], 0, 0)
        self.board = [['.' for _ in range(n)] for _ in range(n)]   
        output = [self.generate_board(positions) for positions in self.sol]  
        
        return output