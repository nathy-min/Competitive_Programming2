class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        dist = [[-1 for _ in range(col)] for _ in range(row)]
        q = deque()
        visited = set()
        moves = [[1, 0], [0, 1],[-1, 0], [0, -1]]

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            r, c = q.popleft()
            for move in moves:
                if min(r + move[0], c + move[1]) < 0 or r + move[0] >= row or                c + move[1] >= col:
                    continue

                if (r + move[0], c + move[1]) not in visited:
                    dist[r + move[0]][c + move[1]] = dist[r][c] + 1
                    q.append((r + move[0], c + move[1]))
                    visited.add((r + move[0], c + move[1]))

        return dist