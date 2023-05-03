class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(maze)
        cols = len(maze[0])
        
        while q:
            r, c, length = q.popleft()
            
            if (r != entrance[0] or c != entrance[1]) and (min(r, c) == 0 or
                r == rows - 1 or c == cols - 1 ):
                return length
            
            for move in moves:
                if min(r + move[0], c + move[1]) < 0 or r + move[0] >= rows       or                                              c + move[1] >= cols:
                    continue
                    
                if (r + move[0], c + move[1]) not in visited and maze[r + move[0]][c + move[1]] == '.':
                    q.append((r + move[0], c + move[1], length + 1))
                    visited.add((r + move[0], c + move[1]))
        return -1