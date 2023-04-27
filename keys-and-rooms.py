class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            room = q.popleft()

            for key in rooms[room]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)
        
        return len(rooms) == len(visited)