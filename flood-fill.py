class Solution:
    def inbound(self, r, c):
        if r < 0 or r >= len(self.image) or c < 0 or c >= len(self.image[0]):
            return False
        return True
    
    def dfs(self, r, c):
        if not self.inbound(r, c):
            return
        if (r, c) in self.visited:
            return
        
        if self.image[r][c] == self.start:
            self.visited.add((r, c))
            self.image[r][c] = self.color
            self.dfs(r + 1, c)
            self.dfs(r - 1, c)
            self.dfs(r, c + 1)
            self.dfs(r, c - 1)
            
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.start = image[sr][sc]
        self.color = color
        self.visited = set()
        
        self.dfs(sr, sc)
        
        return self.image