class Solution:
    def inBound(self, r, c):
        if r < 0 or r >= len(self.grid1) or c < 0 or c >= len(self.grid1[0]):
            return True

    def dfs(self, r, c):
        if  self.inBound(r, c) or not self.grid2[r][c] or (r, c) in self.visited:
            return True

        if not self.grid1[r][c]:    
            return False

        self.visited.add((r, c))    

        ans1 = self.dfs(r + 1, c)
        ans2 = self.dfs(r - 1, c)
        ans3 = self.dfs(r, c + 1)
        ans4 = self.dfs(r, c - 1)

        return ans1 and ans2 and ans3 and ans4    

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.grid1 = grid1
        self.grid2 = grid2
        self.visited = set()
        count = 0

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in self.visited and grid2[i][j]:
                    if self.dfs(i, j):
                        count += 1        

        return count