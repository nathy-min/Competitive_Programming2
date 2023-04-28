class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        visited = set()
        q.append(([0, 0, 0, 0], 0))
        visited.add((0, 0, 0, 0))
        dead = set(deadends)
        moves = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                  [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]

        while q:
            lst, length = q.popleft()
            curr_str = ''.join(str(i) for i in lst)
            
            if curr_str in dead:
                continue

            if curr_str == target:
                return length

            for move in moves:
                curr_lst = []
                for j in range(4):
                    curr_lst.append((move[j] + lst[j]) % 10)

                if tuple(curr_lst) not in visited:
                    q.append((curr_lst, length + 1))
                    visited.add(tuple(curr_lst))

        return -1