class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pre_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                pre_matrix[i][preferences[i][j]] = j

        seen = []
        unhappy = set()
        for a, b in pairs:
            for x, y in seen:
                if pre_matrix[a][b] > pre_matrix[a][x] and pre_matrix[x][y] > pre_matrix[x][a]:
                    unhappy.add(a)
                    unhappy.add(x)
                if pre_matrix[a][b] > pre_matrix[a][y] and pre_matrix[y][x] > pre_matrix[y][a]:
                    unhappy.add(a)
                    unhappy.add(y)  
                if pre_matrix[b][a] > pre_matrix[b][x] and pre_matrix[x][y] > pre_matrix[x][b]:
                    unhappy.add(b)
                    unhappy.add(x)
                if pre_matrix[b][a] > pre_matrix[b][y] and pre_matrix[y][x] > pre_matrix[y][b]:
                    unhappy.add(b)
                    unhappy.add(y)
            seen.append([a, b])

        return len(unhappy)