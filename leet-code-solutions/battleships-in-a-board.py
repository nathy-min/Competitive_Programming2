class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    up = left = False
                    if i > 0 and board[i - 1][j] == "X":
                        up = True
                    if j > 0 and board[i][j - 1] == "X":
                        left = True
                    if not (left or up):
                        count += 1

        return count                        