class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0, 1, 0))
        visited = set()
        visited.add((0, 1))

        while q:
            p, s, length = q.popleft()
            
            if p == target:
                return length

            if (p + s, 2 * s) not in visited:
                q.append((p + s, 2 * s, length + 1))
                visited.add((p + s, 2 * s))
            if s > 0:
                if (p, -1) not in visited:
                    q.append((p, -1, length + 1))
                    visited.add((p, -1))
            else:
                if (p, 1) not in visited:
                    q.append((p, 1, length + 1))