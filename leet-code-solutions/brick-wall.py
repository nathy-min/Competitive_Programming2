class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        m = sum(wall[0])
        col = defaultdict(int)
        for i in range(n):
            prev = 0
            for j in range(len(wall[i])):
                col[prev + wall[i][j]] += 1
                prev += wall[i][j]  
        col[m] = 0
        bricks = max(v for v in col.values())
        return n - bricks
        