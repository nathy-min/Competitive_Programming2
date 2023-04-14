class Solution:
    def inBound(self, r, c):
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
            return True
    
    def dfs(self, r, c):
        area = 0
        if (r, c) in self.visited or self.inBound(r, c) or self.grid[r][c] == 0:
            return 0
        
        self.visited.add((r, c))
        area += (self.dfs(r + 1, c) + self.dfs(r - 1, c) + self.dfs(r, c + 1) + self.dfs(r, c - 1) + 1)
        
        return area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_area = 0
        self.visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in self.visited:
                    max_area = max(max_area, self.dfs(i, j))
                    
        return max_area