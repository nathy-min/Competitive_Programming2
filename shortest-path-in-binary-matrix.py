class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        q.append((0, 0, 1))
        visited.add((0, 0))
        n = len(grid)
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], 
                  [-1, -1], [-1, 1], [1, -1]]

        while q:
            r, c, length = q.popleft()

            if min(r, c) < 0 or max(r, c) >=n or grid[r][c]:
                continue

            if r == n - 1 and c == n - 1:
                return length  

            for a, b in moves:
                if (r + a, c + b) not in visited:
                    q.append((r + a, c + b, length + 1))
                    visited.add((r + a, c + b))

        return -1